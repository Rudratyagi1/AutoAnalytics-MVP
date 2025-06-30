import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AutoAnalytics E-Commerce", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("📊 AutoAnalytics")
section = st.sidebar.radio("Go to", [
    "📁 Upload Data",
    "📄 Data Summary",
    "🧹 Cleaning",
    "⚙️ Feature Engg.",
    "📈 ML Metrics",
    "❓ FAQ Viewer",
    "🤖 Q&A Chat",
    "🔍 Logs"
])

# --- Upload Data ---
if section == "📁 Upload Data":
    st.header("📁 Upload Your E-Commerce Dataset")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df  # Store in session
        st.success("✅ File successfully uploaded!")
        st.dataframe(df.head())

# --- Data Summary ---
elif section == "📄 Data Summary":
    st.header("📄 Dataset Overview")
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.write("🔢 Shape:", df.shape)
        st.write("📊 Summary Stats:")
        st.write(df.describe())
        st.write("🧩 Null Values:")
        st.write(df.isnull().sum())
    else:
        st.warning("⚠️ Please upload a CSV file in the 'Upload Data' section first.")

# --- Cleaning Section ---
elif section == "🧹 Cleaning":
    st.header("🧹 Data Cleaning Options")
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.write("⚙️ NA & Outlier Handling (Coming Soon)")
        st.dataframe(df.head())
    else:
        st.warning("⚠️ Please upload data first.")

# --- Feature Engineering ---
elif section == "⚙️ Feature Engg.":
    st.header("⚙️ Feature Engineering Tools")
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.write("🔧 Placeholder for feature transformations:")
        st.markdown("- Extract date parts (month, weekday)")
        st.markdown("- Calculate customer frequency")
        st.markdown("- Generate basket size")
        st.dataframe(df.head())
    else:
        st.warning("⚠️ Please upload data first.")

# --- ML Metrics Visualization ---
elif section == "📈 ML Metrics":
    st.header("📈 Model Metrics Dashboard")
    if 'df' in st.session_state:
        st.write("✅ Placeholder for model evaluation metrics (AUC, F1, Confusion Matrix)")
        sample_data = pd.DataFrame({'Metric': ['AUC', 'F1 Score'], 'Score': [0.89, 0.77]})
        fig = px.bar(sample_data, x='Metric', y='Score', title="Model Performance")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Upload dataset before viewing metrics.")

# --- FAQ Viewer ---
elif section == "❓ FAQ Viewer":
    st.header("❓ YAML-based FAQ Viewer")
    st.markdown("""
    **Q1: What kind of datasets are supported?**  
    Only e-commerce CSV files with columns like `OrderID`, `CustomerID`, `Product`, `Sales`, etc.

    **Q2: How is data validated?**  
    Schema check + keyword match in columns.

    _More FAQs will be auto-loaded from YAML in P3..._
    """)

# --- Q&A Chat Interface ---
elif section == "🤖 Q&A Chat":
    st.header("🤖 Ask Anything About Your Data")
    st.text_input("Type your question below:")
    st.markdown("_Q&A module via LangChain + PandasAI coming in Phase 4._")

# --- Logs Viewer ---
elif section == "🔍 Logs":
    st.header("🔍 Logs + Monitoring")
    st.markdown("_This will connect to AWS CloudWatch logs using Boto3 in P5._")
    st.code(">>> Log polling, status updates, error alerts will appear here.")

# --- Footer ---
st.markdown("---")
st.markdown("🚀 Built by Team AutoAnalytics • MVP v1.0 • E-Commerce Edition • © 2025")


