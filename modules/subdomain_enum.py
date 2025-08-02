# modules/subdomain_enum.py

import subprocess
from pathlib import Path
from rich.console import Console
from rich.progress import SpinnerColumn, TextColumn, Progress

console = Console()

def run_subfinder(domain):
    try:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task(f"Enumerating subdomains for {domain}...", start=False)
            progress.start_task(task)
            result = subprocess.run(["subfinder", "-d", domain, "-silent"], capture_output=True, text=True)
            progress.stop_task(task)

        subs = result.stdout.strip().split('\n')
        subs = [sub for sub in subs if sub]
        return subs
    except Exception as e:
        console.print(f"[red][!] Error during subdomain enumeration: {e}[/red]")
        return []

def run_subdomain_enum(target):
    subs = run_subfinder(target)
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "subdomains.txt"

    if not subs:
        console.print(f"[red]No subdomains found for {target}.[/red]")
        return

    with open(output_file, "w") as f:
        for sub in subs:
            f.write(sub + "\n")

    console.print(f"[green]Subdomains saved to {output_file}[/green]")
