import streamlit as st

def analyze_resume():
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
