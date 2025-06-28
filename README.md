# CyberCLI

A comprehensive command-line cybersecurity toolkit for IP threat intelligence analysis and AI-powered log analysis. Transform raw security data into actionable insights with beautiful terminal displays and automated threat detection.

## 🎯 What CyberCLI Does

**CyberCLI** is a complete cybersecurity analysis pipeline that helps security professionals, researchers, and system administrators quickly assess IP addresses and analyze security logs. The tool combines multiple data sources and AI analysis to provide comprehensive threat intelligence in an easy-to-read format.

### **Core Workflow:**
1. **🔍 IP Analysis**: Query VirusTotal's database of 70+ security engines
2. **📊 Data Visualization**: Display results in beautiful, organized tables
3. **💾 Multi-Format Output**: Save detailed reports in JSON and human-readable formats
4. **🤖 AI Log Analysis**: Leverage OpenAI GPT-4 to analyze security logs for threats
5. **📋 Comprehensive Reporting**: Generate professional reports for documentation

## ✨ Features

### **🛡️ VirusTotal Integration**
- **Multi-Engine Analysis**: Comprehensive IP reputation checking using 70+ security vendors
- **Real-Time Scanning**: Live threat intelligence data from VirusTotal's global network
- **Detailed Attribution**: Country, ISP, network information, and SSL certificate details
- **Historical Context**: Access to past analysis data and community intelligence

### **🎨 Beautiful Terminal Interface**
- **Rich Table Displays**: Color-coded, organized tables using the Rich library
- **Visual Threat Indicators**: Red/yellow/green color coding for instant risk assessment
- **Responsive Layout**: Properly formatted tables that adapt to terminal width
- **Professional Presentation**: Clean, modern interface suitable for client presentations

### **📁 Multi-Format Output**
- **JSON Reports**: Complete raw data for automated processing and integration
- **Human-Readable Reports**: Professional text summaries for documentation
- **Timestamped Files**: Organized file naming for easy tracking and archival
- **Batch Processing Ready**: Structured output perfect for bulk analysis workflows

### **🤖 AI-Powered Log Analysis** (Optional)
- **GPT-4 Integration**: Advanced AI analysis of security logs and events
- **Threat Detection**: Intelligent identification of malicious patterns and indicators
- **Natural Language Explanations**: Human-readable threat assessments
- **Interactive Analysis**: Real-time log entry examination with contextual insights

### **🔒 Security-First Design**
- **API Key Protection**: Secure credential management with environment variables
- **No Data Persistence**: Raw scan data excluded from version control
- **Clean Git History**: Comprehensive .gitignore prevents accidental key exposure

## 🏗️ Project Architecture

### **System Overview**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   CyberCLI Core  │───▶│   Data Output   │
│                 │    │                  │    │                 │
│ • IP Address    │    │ • API Routing    │    │ • JSON Reports  │
│ • Log Entries   │    │ • Data Processing│    │ • Text Reports  │
└─────────────────┘    │ • Table Rendering│    │ • Terminal UI   │
                       └──────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   External APIs  │
                    │                  │
                    │ • VirusTotal     │
                    │ • OpenAI GPT-4   │
                    └──────────────────┘
```

### **Module Architecture**

#### **📁 Core Components**

**`main.py`** - Application Entry Point
- User interface and interaction handling
- Workflow orchestration and error management
- Terminal display coordination using Rich console
- Input validation and sanitization

**`vt_client.py`** - VirusTotal Integration Engine
- API communication and authentication
- Data extraction and normalization
- Rich table generation and formatting
- Multi-format report generation (JSON/TXT)
- Error handling and rate limiting

**`log_analyzer.py`** - AI Analysis Engine
- OpenAI GPT-4 integration for log analysis
- Intelligent threat pattern recognition
- Natural language threat explanations
- Interactive analysis workflow

#### **📊 Data Flow Architecture**

```
Input Data
    ├── IP Address
    │   ├── VirusTotal API Query
    │   ├── JSON Response Processing
    │   ├── Table Rendering (Rich)
    │   └── File Output (JSON + TXT)
    │
    └── Log Entry
        ├── OpenAI API Query
        ├── GPT-4 Analysis
        └── Threat Assessment Output
```

#### **🎨 UI Architecture (Rich Library)**

```
Terminal Interface
├── Header Panel (IP Information)
├── Basic Information Table
│   ├── Country/Continent
│   ├── Network Details
│   └── Analysis Timestamps
├── Security Analysis Summary
│   ├── Color-coded Categories
│   ├── Percentage Breakdowns
│   └── Total Engine Counts
├── Detailed Results Tables
│   ├── Malicious Detections (Priority)
│   ├── Suspicious Detections 
│   ├── Clean Engine Sample
│   └── Undetected Engine Panel
└── Status Messages & File Paths
```

## 🚀 Installation & Setup

### **1. Clone & Navigate**
```bash
git clone https://github.com/shxwheen/cybercli.git
cd cybercli
```

### **2. Environment Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure API Keys**
Create a `.env` file in the project root:
```bash
# Required: VirusTotal API Key
VT_API_KEY=your_virustotal_api_key_here

# Optional: OpenAI API Key (for AI log analysis)
OPENAI_API_KEY=your_openai_api_key_here
```

## 🔑 API Keys & Accounts

### **Required APIs**

**VirusTotal** (Free Tier Available)
- **Purpose**: IP reputation analysis and threat intelligence
- **Cost**: Free tier: 1,000 requests/day
- **Sign up**: [virustotal.com](https://www.virustotal.com/)
- **Features**: 70+ security engine analysis, historical data, community intelligence

### **Optional APIs**

**OpenAI** (Pay-per-use)
- **Purpose**: AI-powered log analysis and threat detection
- **Cost**: ~$0.03 per 1K tokens (GPT-4)
- **Sign up**: [platform.openai.com](https://platform.openai.com/)
- **Features**: Natural language threat analysis, pattern recognition, detailed explanations

## 💻 Usage Examples

### **Basic IP Analysis**
```bash
python main.py
# Enter IP when prompted: 8.8.8.8
```

### **Batch Analysis** (Coming Soon)
```bash
python main.py --file ip_list.txt
```

### **AI Log Analysis**
1. Run the main script: `python main.py`
2. Complete IP analysis
3. Enter log entries when prompted
4. Receive AI-powered threat assessments

## 📁 File Structure

```
cybercli/
├── 📄 main.py              # Application entry point & UI
├── 📄 vt_client.py         # VirusTotal API & table rendering
├── 📄 log_analyzer.py      # OpenAI integration & log analysis
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env                 # API keys (not tracked)
├── 📄 .gitignore          # Security & cleanup rules
├── 📄 README.md           # This documentation
├── 📁 output/             # Generated reports (auto-created)
│   ├── vt_scan_IP_TIMESTAMP.json
│   └── vt_scan_IP_TIMESTAMP.txt
└── 📁 venv/               # Virtual environment (not tracked)
```

## 🛡️ Security & Privacy

### **Data Handling**
- **No Local Storage**: Scan results are saved locally only, never transmitted elsewhere
- **API Key Protection**: Environment variables prevent accidental exposure
- **Clean Git History**: Comprehensive .gitignore excludes sensitive data
- **Secure Defaults**: All security configurations follow best practices

### **Privacy Considerations**
- VirusTotal may retain query data according to their privacy policy
- OpenAI processes log data according to their data usage policies
- No personally identifiable information is required for basic functionality

## 🔧 Dependencies

```
requests>=2.32.0      # HTTP API communication
python-dotenv>=1.0.0  # Environment variable management  
colorama>=0.4.6       # Cross-platform colored terminal text
rich>=13.0.0          # Beautiful terminal tables and formatting
openai>=1.0.0         # AI-powered log analysis (optional)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### **Development Setup**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

**⚡ CyberCLI** - Transform cybersecurity data into actionable intelligence. 