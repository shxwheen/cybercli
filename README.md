# CyberCLI

A command-line cybersecurity toolkit for IP analysis and threat intelligence gathering.

## Features

- **VirusTotal Integration**: Comprehensive IP reputation analysis using 70+ security engines
- **Shodan Integration**: Internet-connected device discovery and banner grabbing
- **Log Analysis**: Security log parsing and analysis capabilities
- **Multiple Output Formats**: Results saved in both JSON (raw data) and human-readable text formats

## Installation

1. Clone the repository:
```bash
git clone https://github.com/[USERNAME]/cybercli.git
cd cybercli
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API keys in a `.env` file:
```bash
VT_API_KEY=your_virustotal_api_key_here
SHODAN_API_KEY=your_shodan_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

Enter an IP address when prompted to get comprehensive threat intelligence data.

## Output Files

- **JSON files**: Complete raw API data for automated processing
- **TXT files**: Human-readable reports with organized summaries

## API Keys Required

- **VirusTotal**: Get your free API key at [virustotal.com](https://www.virustotal.com/)
- **Shodan**: Get your API key at [shodan.io](https://www.shodan.io/) (paid membership recommended)

## File Structure

```
cybercli/
├── main.py              # Main application entry point
├── vt_client.py         # VirusTotal API integration
├── shodan_client.py     # Shodan API integration
├── log_analyzer.py      # Log analysis utilities
├── .env                 # API keys (not tracked in git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Security Note

Never commit your `.env` file or API keys to version control. The `.gitignore` file is configured to prevent this.

## License

This project is open source and available under the [MIT License](LICENSE). 