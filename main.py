from vt_client import check_ip, save_vt_results, display_vt_table
from log_analyzer import analyze_log_entry
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
import datetime
load_dotenv()

console = Console()

def main():
    # Welcome message with style
    welcome_text = Text("🔍 CyberCLI - Cybersecurity Intelligence Toolkit", style="bold blue")
    console.print(welcome_text)
    console.print("=" * 60)
    
    ip = input("\n🎯 Enter IP to scan: ")
    
    console.print(f"\n🔄 Scanning IP: [bold cyan]{ip}[/bold cyan]")
    console.print("⏳ Fetching VirusTotal data...\n")
    
    # Get VirusTotal results
    vt_results = check_ip(ip)
    
    if isinstance(vt_results, dict) and 'data' in vt_results:
        # Display beautiful table
        display_vt_table(ip, vt_results)
        
        # Save results to files
        filename = save_vt_results(ip, vt_results)
        console.print(f"💾 Results saved to: [green]{filename}[/green]\n")
        
    else:
        console.print(f"[red]❌ Error: {vt_results}[/red]\n")

    # Log analysis section
    console.print("=" * 60)
    console.print("📊 [bold]Log Analysis Section[/bold]")
    console.print("=" * 60)
    
    while True:
        entry = input("\n📝 Paste a log entry (or 'q' to quit): ")
        if entry.lower() == 'q':
            break
        result = analyze_log_entry(entry)
        console.print(f"📋 Analysis: {result}")

if __name__ == "__main__":
    main()
