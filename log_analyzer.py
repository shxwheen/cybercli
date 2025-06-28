from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_log_entry(log_entry):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Analyze this log entry and tell me if it's malicious or not:\n{log_entry}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
