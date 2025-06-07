# app.py
import streamlit as st
from analyzer import analyze_resume
from style import set_custom_styles

# === Streamlit Page Configuration ===
st.set_page_config(page_title="💼 AI Resume Analyzer", layout="wide")

# === Apply Custom Styles ===
set_custom_styles()

# === GUI Title ===
st.markdown('<h1 class="dark-purple" style="text-align:center;"> Resume Analyzer</h1>', unsafe_allow_html=True)

# === Resume Upload Section ===
st.markdown('<h4 class="dark-purple"> Please upload your resume (PDF format):</h4>', unsafe_allow_html=True)
st.markdown('<p style="color:white; font-size:14px;">Drag and drop file here<br>Limit 200MB per file • PDF</p>', unsafe_allow_html=True)
uploaded_resume = st.file_uploader(" ", type=["pdf"], label_visibility="collapsed")

# === Job Description Input ===
st.markdown('<h4 class="dark-purple">Please enter a brief description of the job you are targeting:</h4>', unsafe_allow_html=True)
job_description = st.text_area("Job Description", height=200, label_visibility="collapsed")

# === Run Analyzer ===
if uploaded_resume and job_description:
    analyze_resume()
else:
    st.markdown('<div class="custom-warning">upload to analyze</div>', unsafe_allow_html=True)
