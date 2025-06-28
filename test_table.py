"""
Test script to demonstrate the new table functionality
Run this after installing rich: pip install rich>=13.0.0
"""

from vt_client import display_vt_table
import json

# Load one of your existing scan results to test
def test_with_existing_data():
    try:
        # Try to load the Google DNS scan
        with open('vt_scan_8.8.8.8_20250627_220318.json', 'r') as f:
            data = json.load(f)
            scan_data = data.get('results', {})
            ip = data.get('scan_info', {}).get('ip', '8.8.8.8')
            
        print("Testing table display with your 8.8.8.8 scan data...")
        display_vt_table(ip, scan_data)
        
    except FileNotFoundError:
        print("JSON file not found. Please run a scan first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_with_existing_data() 