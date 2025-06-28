from shodan_client import search_ip
from vt_client import check_ip, save_vt_results
from log_analyzer import analyze_log_entry
from dotenv import load_dotenv
import datetime
load_dotenv()


def main():
    ip = input("Enter IP to scan: ")
    
    print(f"\n🔍 Scanning IP: {ip}")
    print("=" * 50)
    
    # Get VirusTotal results
    vt_results = check_ip(ip)
    
    if isinstance(vt_results, dict):
        # Save results to file
        filename = save_vt_results(ip, vt_results)
        print(f"✅ VirusTotal results saved to: {filename}")
        
        # Show summary in terminal
        if 'data' in vt_results:
            attributes = vt_results['data'].get('attributes', {})
            last_analysis = attributes.get('last_analysis_results', {})
            
            # Count detections
            malicious = sum(1 for engine in last_analysis.values() if engine.get('category') == 'malicious')
            suspicious = sum(1 for engine in last_analysis.values() if engine.get('category') == 'suspicious')
            total_engines = len(last_analysis)
            
            print(f"\n📊 Detection Summary:")
            print(f"   🔴 Malicious: {malicious}/{total_engines}")
            print(f"   🟡 Suspicious: {suspicious}/{total_engines}")
            print(f"   🌍 Country: {attributes.get('country', 'Unknown')}")
            print(f"   🏢 AS Owner: {attributes.get('as_owner', 'Unknown')}")
    else:
        print(f"❌ Error: {vt_results}")

    print("\n--- Log Analysis ---")
    while True:
        entry = input("Paste a log entry (or 'q' to quit): ")
        if entry.lower() == 'q':
            break
        print(analyze_log_entry(entry))

if __name__ == "__main__":
    main()
