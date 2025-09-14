# Excel_interview_chatbot
“An AI-powered Streamlit app that simulates Excel mock interviews — structured Q&amp;A, automatic evaluation, and performance feedback.”
**🧑‍💻 AI-Powered Excel Mock Interviewer**

This project is a Streamlit-based AI chatbot that simulates a structured Excel mock interview. It introduces itself, explains the process, asks multiple Excel-related questions, evaluates the candidate’s answers, and provides a performance summary with feedback.

**🚀 Features**

Multi-turn interview flow (Intro → Questions → Summary).

Keyword-based evaluation of answers (PoC stage).

Performance summary with scores and feedback.

Built with Python + Streamlit for interactivity.

Easily extendable to Large Language Models (LLMs) in the future.

**📂 Project Structure**
Excel-Mock-Interviewer/
│── excel_interviewer.py      # Streamlit app
│── requirements.txt          # Dependencies
│── README.md                 # Project overview & instructions
│── samples/                  # Sample interview transcripts (optional)

**🛠️ Tech Stack**

Python 3.7+

Streamlit (UI & deployment)

Rule-based NLP (keyword matching for evaluation)

**🔧 Installation & Running Locally**

**Clone the repository:**

git clone https://github.com/Jateen786/Excel_interview_chatbot
cd Excel-Mock-Interviewer


Install dependencies:

pip install -r requirements.txt


Run the **Streamlit** app:

streamlit run excel_interviewer.py
**##You have to add you file name here**


Open the local URL shown in the terminal (e.g., http://localhost:8501
).

**🌍 Deployment**

You can deploy this app easily on:

Streamlit Cloud
 (recommended).



**📊 Sample Output (Transcript)**
**👋 Welcome to the Excel Mock Interviewer!**
**Q1: How would you use VLOOKUP in Excel?**
Candidate: You can use VLOOKUP to search a value in the first column and return data from another column.
➡️ Evaluation: 100% relevant.

**Q2: What is the difference between Absolute and Relative cell references?**
Candidate: Relative changes when copied, Absolute ($A$1) does not.
➡️ Evaluation: 100% relevant.

**===== Interview Summary =====**
Overall Performance: **95%**
Feedback:** Excellent! **You seem very strong in Excel.

**📌 Deliverables**

✅ Design Document & Approach Strategy

✅ Working Proof-of-Concept (this repository)

✅ Deployed Link (via Streamlit Cloud)

✅ Sample Transcripts
