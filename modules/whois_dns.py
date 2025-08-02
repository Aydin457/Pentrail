import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

def run_whois_dns(target):
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "whois_dns.txt"

    console.print(f"[cyan]Gathering WHOIS and DNS info for {target}...[/cyan]")

    try:

        whois_result = subprocess.run(["whois", target], capture_output=True, text=True)
        # DNS info (A, NS, MX, TXT)
        dig_a = subprocess.run(["dig", "+short", target], capture_output=True, text=True)
        dig_ns = subprocess.run(["dig", "NS", target, "+short"], capture_output=True, text=True)
        dig_mx = subprocess.run(["dig", "MX", target, "+short"], capture_output=True, text=True)
        dig_txt = subprocess.run(["dig", "TXT", target, "+short"], capture_output=True, text=True)

        with open(output_file, "w") as f:
            f.write("=== WHOIS ===\n")
            f.write(whois_result.stdout + "\n")

            f.write("=== A Record ===\n")
            f.write(dig_a.stdout + "\n")

            f.write("=== NS Record ===\n")
            f.write(dig_ns.stdout + "\n")

            f.write("=== MX Record ===\n")
            f.write(dig_mx.stdout + "\n")

            f.write("=== TXT Record ===\n")
            f.write(dig_txt.stdout + "\n")

        console.print(f"[green]WHOIS and DNS info saved to {output_file}[/green]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
