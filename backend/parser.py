import re
import time
import requests
from bs4 import BeautifulSoup


def analyze_url(url: str):
    try:
        if not re.match(r"^https?://", url):
            return {"error": "Invalid URL. Include http:// or https://"}

        start = time.time()

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response_time = round((time.time() - start) * 1000, 2)

        # Raise exception for HTTP errors (404, 500, etc.)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return {
                "error": "Non-HTML response",
                "status_code": response.status_code
            }

        soup = BeautifulSoup(response.text, "lxml")

        # Page Title
        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "Not Found"
        )

        # Meta Description (standard + Open Graph + Twitter)
        meta = (
            soup.find("meta", attrs={"name": "description"})
            or soup.find("meta", attrs={"property": "og:description"})
            or soup.find("meta", attrs={"name": "twitter:description"})
        )

        meta_description = (
            meta.get("content").strip()
            if meta and meta.get("content")
            else "Not Found"
        )

        # First H1
        h1 = soup.find("h1")
        h1_text = h1.get_text(strip=True) if h1 else "Not Found"

        # Word Count
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())

        # Images
        images = soup.find_all("img")
        total_images = len(images)

        # Images missing alt attribute
        images_missing_alt = sum(
            1
            for img in images
            if not img.get("alt") or img.get("alt").strip() == ""
        )

        return {
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "page_title": title,
            "meta_description": meta_description,
            "h1": h1_text,
            "word_count": word_count,
            "total_images": total_images,
            "images_missing_alt": images_missing_alt
        }

    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}

    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to website"}

    except requests.exceptions.HTTPError as e:
        return {
            "error": f"HTTP Error: {response.status_code}",
            "status_code": response.status_code
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

    except Exception as e:
        return {"error": f"Unexpected Error: {str(e)}"}