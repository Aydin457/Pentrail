import requests
from pathlib import Path
from rich.console import Console

console = Console()

def run_cors_scanner(target):
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "cors_scan.txt"

    console.print(f"[cyan]Starting CORS Misconfiguration Scan on {target}[/cyan]")

    urls_to_test = [
        f"https://{target}",
        f"http://{target}"
    ]

    findings = []

    for url in urls_to_test:
        try:
            response = requests.options(url, timeout=10, allow_redirects=True)
            acao = response.headers.get("Access-Control-Allow-Origin", "")
            acac = response.headers.get("Access-Control-Allow-Credentials", "")

            console.print(f"[green]Testing {url}[/green]")
            console.print(f"  Access-Control-Allow-Origin: {acao}")
            console.print(f"  Access-Control-Allow-Credentials: {acac}")

            # Check common risky misconfigurations
            if acao == "*" and acac.lower() == "true":
                findings.append(f"[!] Vulnerable CORS config at {url}: ACAO='*' with credentials allowed")
            elif target in acao:
                # Good case: specific origin allowed
                pass
            elif acao and acao != "*":
                findings.append(f"[!] Potential risky ACAO header at {url}: {acao}")

        except Exception as e:
            console.print(f"[red]Failed to scan {url}: {e}[/red]")

    with open(output_file, "w") as f:
        if findings:
            for line in findings:
                f.write(line + "\n")
            console.print(f"[bold red]Potential CORS issues found! See {output_file}[/bold red]")
        else:
            console.print("[green]No obvious CORS misconfigurations found.[/green]")

