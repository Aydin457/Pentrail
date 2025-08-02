# modules/portscan.py

import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

def run_port_scan(target):
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "portscan.txt"

    console.print(f"[cyan]Running port scan on {target} using nmap...[/cyan]")

    try:

        result = subprocess.run(
            ["nmap", "-sS", "-Pn", "-T4", target, "-oN", str(output_file)],
            capture_output=True,
            text=True,
            check=True
        )

        console.print(f"[green]Port scan results saved to {output_file}[/green]")

    except FileNotFoundError:
        console.print("[red]Error: nmap is not installed or not found in PATH.[/red]")
        console.print("[yellow]Please install nmap: sudo apt install nmap[/yellow]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Port scan failed: {e}[/red]")
