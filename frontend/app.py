import streamlit as st
import requests

# Render Backend API
API_URL = "https://pagepulse-2.onrender.com/audit"

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
                    timeout=30
                )

                # Check for HTTP errors
                response.raise_for_status()

                data = response.json()

                # Backend returned an error
                if "error" in data:
                    st.error(data["error"])

                else:
                    st.success("✅ Audit completed successfully!")

                    st.divider()

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("Status Code", data.get("status_code", "-"))
                        st.metric(
                            "Response Time",
                            f"{data.get('response_time_ms', '-') } ms"
                        )
                        st.metric(
                            "Total Images",
                            data.get("total_images", "-")
                        )

                    with col2:
                        st.metric(
                            "Missing ALT Tags",
                            data.get("images_missing_alt", "-")
                        )
                        st.metric(
                            "Word Count",
                            data.get("word_count", "-")
                        )

                    st.divider()

                    st.subheader("📄 Page Information")

                    st.markdown("### 📝 Title")
                    st.info(data.get("page_title", "Not Found"))

                    st.markdown("### 📑 Meta Description")
                    st.info(data.get("meta_description", "Not Found"))

                    st.markdown("### 📰 First H1")
                    st.info(data.get("h1", "Not Found"))

                    # SEO Score
                    score = 0

                    if data.get("page_title") != "Not Found":
                        score += 25

                    if data.get("meta_description") != "Not Found":
                        score += 25

                    if data.get("h1") != "Not Found":
                        score += 25

                    if data.get("images_missing_alt") == 0:
                        score += 25

                    st.divider()

                    st.subheader("📈 SEO Score")

                    st.progress(score / 100)

                    if score >= 90:
                        st.success(f"{score}/100 - Excellent")

                    elif score >= 70:
                        st.info(f"{score}/100 - Good")

                    elif score >= 50:
                        st.warning(f"{score}/100 - Average")

                    else:
                        st.error(f"{score}/100 - Needs Improvement")

            except requests.exceptions.HTTPError as e:
                st.error(f"HTTP Error: {e}")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend server.")

            except requests.exceptions.Timeout:
                st.error("The request timed out.")

            except Exception as e:
                st.error(f"Unexpected Error: {e}")

st.divider()
st.caption("Built for Digital Heroes Training Task")
