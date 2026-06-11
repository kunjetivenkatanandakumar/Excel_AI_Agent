# 🚀 Excel AI Agent

An AI-powered Excel and CSV Data Cleaning Tool built with Python, Streamlit, Pandas, and Gemini AI.

The application automatically analyzes datasets, identifies data quality issues, cleans data, generates reports, and exports cleaned files.

---

## 📌 Features

### Data Import

* Upload Excel (.xlsx)
* Upload CSV (.csv)
* Multiple Sheet Support
* Large Dataset Support (100,000+ Rows)

### Data Profiling

* Row Count
* Column Count
* Missing Value Analysis
* Duplicate Detection
* Data Type Analysis
* Dataset Summary

### Data Cleaning

* Remove Duplicate Records
* Handle Missing Values
* Standardize Text Fields
* Remove Extra Spaces
* Fix Data Types
* Date Format Standardization
* Numeric Data Validation
* Outlier Detection

### AI-Powered Analysis

* Gemini AI Recommendations
* Dataset Insights
* Cleaning Suggestions
* Data Quality Improvements

### Reporting

* Data Quality Score
* Cleaning Summary
* Outlier Report
* Downloadable Reports

### Export

* Cleaned Excel File
* Cleaned CSV File
* Data Quality Report

---

## 🏗️ Project Architecture

```text
Excel/CSV File
        ↓
Excel Reader
        ↓
Data Profiling Agent
        ↓
Cleaning Agent
        ↓
Outlier Detection Agent
        ↓
Validation Agent
        ↓
Gemini AI Agent
        ↓
Report Generator
        ↓
Cleaned File Export
```

---

## 📂 Project Structure

```text
ExcelAIAgent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── agents/
│   ├── profiler.py
│   ├── cleaner.py
│   ├── outlier.py
│   ├── validator.py
│   ├── reporter.py
│   └── gemini_agent.py
│
├── utils/
│   ├── excel_reader.py
│   ├── excel_writer.py
│   └── helper.py
│
├── input/
├── output/
├── reports/
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/excel-ai-agent.git

cd excel-ai-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Setup

Get your API Key:

https://aistudio.google.com

Create:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## 📊 Supported File Types

| File Type       | Supported |
| --------------- | --------- |
| XLSX            | ✅         |
| CSV             | ✅         |
| Multiple Sheets | ✅         |
| Large Files     | ✅         |
| Text Data       | ✅         |
| Numeric Data    | ✅         |
| Date Data       | ✅         |

---

## 🧪 Testing

Test the application using:

* Sales Dataset
* Customer Dataset
* HR Dataset
* Inventory Dataset
* Financial Dataset

Verify:

* Missing Value Detection
* Duplicate Detection
* Outlier Detection
* Data Cleaning
* Report Generation
* File Export

---

## 📈 Future Enhancements

### Version 2

* LangGraph Multi-Agent Workflow
* PDF Reports
* Advanced Data Validation
* Email Validation
* Phone Validation
* Address Standardization
* Data Quality Dashboard

### Version 3

* Excel Add-in
* Power BI Integration
* Batch File Processing
* AutoML Integration
* Business Rule Engine
* Cloud Deployment

---

## 🛠️ Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* OpenPyXL
* XlsxWriter
* Google Gemini AI
* LangChain (Future)
* LangGraph (Future)

---

## 🎯 Use Cases

* Data Cleaning
* Data Analytics
* Business Intelligence
* Data Science Projects
* Machine Learning Preprocessing
* Excel Automation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push changes
5. Create a Pull Request

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed as an AI-powered Excel Data Cleaning and Analysis Project using Python, Streamlit, and Gemini AI.
