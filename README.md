AI Resume Analyzer

An interactive **Streamlit** web application that helps job seekers analyze their resumes against a job description using ATS-style evaluation. Built with a stylish dark-themed purple UI, this tool provides feedback on keyword matches, grammar/spelling issues, and role-specific improvement suggestions.

🎯 Features

✅ Upload your **Resume (PDF format)**  
✅ Enter a **Job Description** you're targeting  
✅ Receive:
- ✅ ATS Score
- ✅ Keyword Coverage
- ✅ Formatting Issues
- ✅ Matched Keywords
- ✅ Grammar & Spelling Issues
- ✅ Role-Specific Keyword Suggestions


🖥️ GUI Preview

A sleek, modern UI with dark purple gradients and creative design built using Streamlit.

![Screenshot Placeholder](https://via.placeholder.com/800x400.png?text=AI+Resume+Analyzer+GUI)


🧠 Tech Stack

- **Frontend**: Streamlit
- **Styling**: Custom CSS (Dark Purple Theme)
- **Backend**: Python
- **Libraries**:
  - `streamlit`
  - `PyPDF2`
  - `sklearn`
  - `re`


📁 File Structure


├── app.py                # Main Streamlit app

├── analyzer.py           # Resume analysis logic

├── style.py              # Custom CSS for styling the GUI

├── README.md             # Project documentation


🚀 Getting Started

1. **Clone the repository**

   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer

2. **Run the app**

   streamlit run app.py


✅ To-Do

* [ ] Add PDF download of improved resume
* [ ] Resume keyword extraction from JD
* [ ] Add LinkedIn validator
* [ ] Improve grammar checking (e.g., using `language_tool_python`)


 🙌 Author
**Anbhi Thakur**

