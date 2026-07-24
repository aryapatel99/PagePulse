import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/audit"

st.set_page_config(
    page_title="Page Pulse",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Page Pulse")
st.write("Audit any website for key SEO and accessibility metrics.")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("🔍 Audit Website", use_container_width=True):

    if not url.strip():
        st.warning("Please enter a website URL.")
    else:
        with st.spinner("Analyzing website..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"url": url},
                    timeout=20
                )

                data = response.json()

                if "error" in data:
                    st.error(data["error"])

                else:

                    st.success("Audit completed successfully!")

                    st.divider()

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("Status Code", data["status_code"])
                        st.metric("Response Time", f"{data['response_time_ms']} ms")
                        st.metric("Total Images", data["total_images"])

                    with col2:
                        st.metric("Missing ALT Tags", data["images_missing_alt"])
                        st.metric("Word Count", data["word_count"])

                    st.divider()

                    st.subheader("Page Information")

                    st.write("### 📝 Title")
                    st.info(data["page_title"])

                    st.write("### 📄 Meta Description")
                    st.info(data["meta_description"])

                    st.write("### 📰 First H1")
                    st.info(data["h1"])

                    score = 0

                    if data["page_title"] != "Not Found":
                        score += 25

                    if data["meta_description"] != "Not Found":
                        score += 25

                    if data["h1"] != "Not Found":
                        score += 25

                    if data["images_missing_alt"] == 0:
                        score += 25

                    st.divider()

                    st.subheader("SEO Score")

                    st.progress(score / 100)

                    if score >= 90:
                        st.success(f"{score}/100 - Excellent")

                    elif score >= 70:
                        st.info(f"{score}/100 - Good")

                    elif score >= 50:
                        st.warning(f"{score}/100 - Average")

                    else:
                        st.error(f"{score}/100 - Needs Improvement")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to FastAPI backend.")

            except Exception as e:
                st.error(str(e))

st.divider()
st.caption("Built for Digital Heroes Training Task")
