import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

def run_dir_enum(target, wordlist_path=None):
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "dir_enum.txt"

    console.print(f"[cyan]Starting Directory Enumeration on {target}[/cyan]")

    if not wordlist_path:
        wordlist_path = console.input("[bold yellow]Enter path to wordlist (e.g. /usr/share/seclists/...): [/bold yellow]")

    if not Path(wordlist_path).exists():
        console.print(f"[red]Wordlist not found at {wordlist_path}. Exiting.[/red]")
        return

    cmd = [
        "ffuf",
        "-u", f"https://{target}/FUZZ",
        "-w", wordlist_path,
        "-t", "40",
        "-mc", "200,204,301,302,307,401,403",
        "-o", str(output_file),
        "-of", "json"
    ]

    try:
        subprocess.run(cmd, check=True)
        console.print(f"[green]Directory enumeration results saved to {output_file}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error running ffuf: {e}[/red]")
    except FileNotFoundError:
        console.print("[red]ffuf is not installed or not found in PATH. Please install ffuf.[/red]")
