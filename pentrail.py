import argparse
from argparse import RawTextHelpFormatter
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
import importlib.util

console = Console()

def import_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def show_banner():
    fig = Figlet(font="slant")
    banner = fig.renderText("Pentrail")
    console.print(f"[bold green]{banner}[/bold green]")
    console.print(Panel.fit(
        "[cyan]Terminal-based Recon Tool[/cyan]\n"
        "[bold white]by Aydın Yasinov[/bold white]",
        border_style="bright_magenta",
        title="Welcome",
        subtitle="github.com/Aydin457"
    ))

def parse_args():
    parser = argparse.ArgumentParser(
        prog="Pentrail",
        description="""
Pentrail – Terminal-Based Recon Tool

A lightweight, scriptable recon tool for ethical hackers & bug bounty hunters.
Modules are customizable and results are saved under the `output/` folder.
""",
        epilog="""
Examples:

    python3 pentrail.py -t example.com
    python3 pentrail.py -t hackerone.com -m subdomain,portscan,jsfinder,cors,direnum,whois

Available Modules:
    subdomain       -> Passive subdomain enumeration (subfinder)
    portscan        -> Port scanning with Nmap
    jsfinder        -> JavaScript files finder and secret scanner
    cors            -> CORS misconfiguration scanner
    direnum         -> Directory/File Enumerator using ffuf
    whois           -> WHOIS & DNS information gathering

Output Directory:
    All results are stored in output/<target>/ by default.
""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "-t", "--target",
        help="Target domain or IP address (required)",
        required=True
    )
    parser.add_argument(
        "-m", "--modules",
        help="Modules to run (comma-separated). Default: subdomain",
        default="subdomain"
    )
    return parser.parse_args()

def main():
    show_banner()
    args = parse_args()
    target = args.target
    modules = [m.strip().lower() for m in args.modules.split(",")]

    console.print(f"[bold yellow]Starting reconnaissance on:[/] [bold cyan]{target}[/]")
    console.print(f"[bold yellow]Modules enabled:[/] [bold cyan]{', '.join(modules)}[/]")

    if "subdomain" in modules:
        sub_enum = import_module_from_file("subdomain_enum", "modules/subdomain_enum.py")
        sub_enum.run_subdomain_enum(target)

    if "portscan" in modules:
        portscan = import_module_from_file("portscan", "modules/portscan.py")
        portscan.run_port_scan(target)

    if "jsfinder" in modules:
        jsfinder = import_module_from_file("js_finder", "modules/js_finder.py")
        jsfinder.run_js_finder(target)

    if "cors" in modules:
        cors_scanner = import_module_from_file("cors_scanner", "modules/cors_scanner.py")
        cors_scanner.run_cors_scanner(target)

    if "direnum" in modules:
        dir_enum = import_module_from_file("dir_enum", "modules/dir_enum.py")
        dir_enum.run_dir_enum(target)

    if "whois" in modules:
        whois_dns = import_module_from_file("whois_dns", "modules/whois_dns.py")
        whois_dns.run_whois_dns(target)


if __name__ == "__main__":
    main()
