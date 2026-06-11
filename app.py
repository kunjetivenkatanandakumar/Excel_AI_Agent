import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Excel AI Agent",
    layout="wide"
)

st.title("📊 Excel AI Agent")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["xlsx","csv"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("Rows",len(df))

    with col2:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with col3:
        st.metric(
            "Duplicates",
            int(df.duplicated().sum())
        )

    if st.button("Clean Data"):

        df = df.drop_duplicates()

        for col in df.columns:

            if df[col].dtype == "object":
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                )

        st.success("Cleaning Complete")

        output = BytesIO()

        df.to_excel(
            output,
            index=False,
            engine="openpyxl"
        )

        st.download_button(
            "Download Cleaned File",
            output.getvalue(),
            "cleaned.xlsx"
        )