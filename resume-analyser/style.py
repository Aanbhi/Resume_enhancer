import streamlit as st

def set_custom_styles():
    st.markdown("""
        <style>
            html, body, [class*="css"] {
                background: linear-gradient(to right, #1a152e, #2d124d);
                color: #e0d9ff;
                font-family: 'Segoe UI', sans-serif;
            }

            .dark-purple {
                color: #7e22ce !important;
            }

            .stFileUploader {
                background-color: #2d124d !important;
                color: white !important;
                border: 2px dashed #c084fc;
                padding: 10px;
                border-radius: 10px;
            }

            textarea, input {
                background-color: #36154e !important;
                color: #f3e8ff !important;
                border: 1px solid #c084fc !important;
                border-radius: 6px;
                font-weight: bold;
            }

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

