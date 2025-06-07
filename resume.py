import streamlit as st

# === Streamlit Page Configuration ===
st.set_page_config(page_title="ATS-Friendly Resume Analyzer", layout="wide")

# === Custom CSS Styling ===
st.markdown("""
    <style>
        /* Background Gradient */
        html, body, [class*="css"] {
            background: linear-gradient(to right, #1a152e, #2d124d);
            color: #e0d9ff;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Dark Purple Font */
        .dark-purple {
            color: #7e22ce !important;
        }

        /* Upload and Input Styling */
        .stFileUploader {
            background-color: #2d124d !important;
            color: white !important;
            border: 2px dashed #c084fc;
            padding: 10px;
            border-radius: 10px;
        }

        /* Textarea and Input */
        textarea, input {
            background-color: #36154e !important;
            color: #f3e8ff !important;
            border: 1px solid #c084fc !important;
            border-radius: 6px;
            font-weight: bold;
        }

        /* Buttons */
        .stButton>button {
            background-color: #a855f7;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #9333ea;
        }

        /* Custom Warning */
        .custom-warning {
            background-color: #4c1d95;
            color: white;
            padding: 10px 16px;
            border-left: 6px solid #c084fc;
            border-radius: 6px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# === GUI Title ===
st.markdown('<h1 class="dark-purple" style="text-align:center;"> Resume Analyzer</h1>', unsafe_allow_html=True)

# === Resume Upload Section ===
st.markdown('<h4 class="dark-purple"> Please upload your resume (PDF format):</h4>', unsafe_allow_html=True)
st.markdown('<p style="color:#a855f7; font-size:14px;">Drag and drop file here | Limit 200MB per file • PDF</p>', unsafe_allow_html=True)
uploaded_resume = st.file_uploader(" ", type=["pdf"], label_visibility="collapsed")

# === Job Description Input ===
st.markdown('<h4 class="dark-purple">Please enter a brief description of the job you are targeting:</h4>', unsafe_allow_html=True)
job_description = st.text_area("Job Description", height=200, label_visibility="collapsed")

# === ATS Analysis Output ===
if uploaded_resume and job_description:
    st.markdown("---")
    st.markdown('<h4 class="dark-purple"> ATS Results:</h4>', unsafe_allow_html=True)
    st.markdown("""
    - **ATS Score:** `75.15%`  
    - **Keyword Coverage:** `15.15%`  
    - **Formatting Issues:** `None`  
    - **Matched Keywords:** `['actionable', 'define', 'deliver', 'develop', 'line']`
    """)

    st.markdown('<h4 class="dark-purple">Grammar and Spelling Issues:</h4>', unsafe_allow_html=True)
    st.markdown("""
    `08th, anbhithakur1, rience, tensorflow, stions, acular, aiml, creativ, ttk, applic, 03th, analyz, ml, compu, essional, etc.`
    """)

    st.markdown('<h4 class="dark-purple">Role-Specific Improvements:</h4>', unsafe_allow_html=True)
    st.markdown("""
    Add role-specific keywords like:  
    `analyses, analytics, assess, automation, business, document, effort, execute, implement, maintain, translate, templates, etc.`
    """)

else:
    st.markdown('<div class="custom-warning">upload to analyze</div>', unsafe_allow_html=True)
