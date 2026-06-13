import streamlit as st
import pandas as pd
import os
from PIL import Image

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Smart Exam Proctoring Dashboard",
    layout="wide"
)

st.title("🎓 Smart Exam Proctoring Dashboard")

# =========================
# AUTO REFRESH
# =========================

if "refresh_count" not in st.session_state:
    st.session_state.refresh_count = 0

# =========================
# VIOLATION LOGS
# =========================

st.header("📋 Violation Logs")

csv_file = "logs/violations.csv"

if os.path.exists(csv_file):

    if os.path.getsize(csv_file) > 0:

        try:

            df = pd.read_csv(csv_file)

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader("📊 Violation Statistics")

            if "Violation" in df.columns:

                st.bar_chart(
                    df["Violation"].value_counts()
                )

        except Exception as e:

            st.error(f"CSV Error: {e}")

    else:

        st.warning("violations.csv is empty")

else:

    st.error("logs/violations.csv not found")

# =========================
# SCREENSHOTS
# =========================

st.header("📸 Evidence Screenshots")

folder = "screenshots"

if os.path.exists(folder):

    images = sorted(
        os.listdir(folder),
        reverse=True
    )

    if len(images) > 0:

        cols = st.columns(3)

        for i, img_name in enumerate(images):

            img_path = os.path.join(
                folder,
                img_name
            )

            try:

                image = Image.open(img_path)

                cols[i % 3].image(
                    image,
                    caption=img_name,
                    use_container_width=True
                )

            except:

                pass

    else:

        st.info("No screenshots found")

else:

    st.error("screenshots folder not found")

# =========================
# TOTAL COUNTS
# =========================

st.header("📈 Dashboard Summary")

if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:

    try:

        df = pd.read_csv(csv_file)

        total = len(df)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Violations",
                total
            )

        with col2:

            screenshot_count = 0

            if os.path.exists(folder):
                screenshot_count = len(
                    os.listdir(folder)
                )

            st.metric(
                "Screenshots",
                screenshot_count
            )

    except:
        pass

# =========================
# FOOTER
# =========================

st.markdown("---")
st.success("✅ Smart Exam Proctoring System Running")