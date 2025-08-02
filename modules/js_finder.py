import requests
from bs4 import BeautifulSoup
from pathlib import Path
from rich.console import Console
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

console = Console()

def run_js_finder(target):
    output_dir = Path(f"output/{target}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "js_files_scan.txt"

    console.print(f"[cyan]Starting JS Files Scan on {target}[/cyan]")

    try:
        url = f"https://{target}"
        resp = requests.get(url, timeout=30, verify=False)
        resp.raise_for_status()
    except Exception as e:
        console.print(f"[red]Failed to fetch {url}: {e}[/red]")
        return

    soup = BeautifulSoup(resp.text, "html.parser")
    scripts = soup.find_all("script", src=True)
    js_urls = set()

    for script in scripts:
        src = script["src"]
        if src.startswith("http"):
            js_urls.add(src)
        elif src.startswith("/"):
            js_urls.add(url + src)
        else:
            js_urls.add(url + "/" + src)

    if not js_urls:
        console.print("[yellow]No external JS files found.[/yellow]")
        return

    findings = []

    patterns = [
        re.compile(r"apiKey", re.I),
        re.compile(r"token", re.I),
        re.compile(r"secret", re.I),
        re.compile(r"clientId", re.I),
        re.compile(r"auth", re.I),
    ]

    for js_url in js_urls:
        console.print(f"[green]Checking {js_url}[/green]")
        try:
            r = requests.get(js_url, timeout=30, verify=False)
            r.raise_for_status()
            content = r.text

            for pattern in patterns:
                if pattern.search(content):
                    findings.append(f"[!] Potential secret '{pattern.pattern}' found in {js_url}")

        except Exception as e:
            console.print(f"[red]Failed to fetch {js_url}: {e}[/red]")

    with open(output_file, "w") as f:
        for line in findings:
            f.write(line + "\n")

    if findings:
        console.print(f"[bold red]Potential secrets found! See {output_file}[/bold red]")
    else:
        console.print("[green]No potential secrets found in JS files.[/green]")
