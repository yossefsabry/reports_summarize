# Annual Report Summarizer
A tool to extract and summarize key information from SEC 10-K annual 
reports (PDF format) using Google's Gemini AI model.

## Features
- Extracts structured data from 10-K PDFs
- Generates clean PDF summaries
- Includes financial data, risk factors, and management discussion
- Uses Pydantic for data validation

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yossefsabry/reports_summarize.git
cd reports_summarize
uv pip install -r requirements.txt
```

3. Set up environment variables:
```bash  
cp .env.example .env
GEMINI_API_KEY=your_api_key_here # in your .env
```

### for running the model:
```bash
uv run main.py
```


## file strcuture: 
```bash
reports_summarize/
├── annual_report_Meta_Platforms,_Inc._2024.pdf  # Example output
├── counter.py                                  # Token counter utility
├── main.py                                     # Main processing script
├── meta_10k.pdf                                # Example input PDF
├── pyproject.toml                              # Project configuration
├── README.md                                   # This file
└── uv.lock                                     # UV lock file
```


## Dependencies
```txt
Python 3.10+
Google Generative AI (google-genai)
Pydantic (v2+)
PyPDF2
WeasyPrint
markdown2
python-dotenv
```


### How It Works
1. The script loads a PDF file using PyPDF2
2. Extracted text is sent to Gemini AI with a structured prompt
3. Response is validated against a Pydantic model
4. Results are converted to Markdown then PDF


## Token Counting Utility
> The counter.py script helps estimate token usage:
```bash
uv run counter.py
```


