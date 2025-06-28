import requests
import os
from dotenv import load_dotenv
load_dotenv()


SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

def search_ip(ip):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
    res = requests.get(url)
    return res.json() if res.ok else res.text
