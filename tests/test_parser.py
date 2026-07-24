import sys
import os

# Add backend folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from parser import analyze_url


def test_valid_website():
    result = analyze_url("https://www.python.org")

    assert "status_code" in result
    assert result["status_code"] == 200
    assert result["page_title"] != "Not Found"
    assert result["word_count"] > 0


def test_invalid_url():
    result = analyze_url("invalid-url")

    assert "error" in result
    assert "Invalid URL" in result["error"]


def test_non_html_response():
    result = analyze_url(
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    )

    assert "error" in result
    assert result["error"] == "Non-HTML response"