# 🌐 Page Pulse

Page Pulse is a web application that audits websites and extracts key SEO and accessibility metrics.

## Features

- Website Status Code
- Response Time
- Page Title
- Meta Description
- First H1 Heading
- Word Count
- Total Images
- Images Missing ALT Text
- Invalid URL Handling
- Timeout Handling
- Non-HTML Detection

## Tech Stack

### Backend
- FastAPI
- Requests
- BeautifulSoup4

### Frontend
- Streamlit

### Testing
- Pytest

## Project Structure

```
PagePulse
│
├── backend
│   ├── main.py
│   ├── parser.py
│   ├── models.py
│   └── utils.py
│
├── frontend
│   └── app.py
│
├── tests
│   └── test_parser.py
│
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd PagePulse
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

## Run Frontend

```bash
cd frontend
streamlit run app.py
```

## Running Tests

```bash
pytest
```

## Design Decisions

- FastAPI was chosen for its speed and automatic API documentation.
- BeautifulSoup was used for reliable HTML parsing.
- Streamlit provides a lightweight and interactive user interface.
- The parser is separated from the API for better maintainability and testing.

## Future Improvements

- JavaScript rendering using Playwright/Selenium.
- SEO scoring with more metrics.
- Export reports as PDF.
- Historical audit storage.

---

Built for Digital Heroes Training Task

https://digitalheroesco.com