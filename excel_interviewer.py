import random
import streamlit as st
# Step 1: Define Interview Questions

questions = [
{
"question": "How would you use VLOOKUP in Excel?",
"keywords": ["VLOOKUP", "lookup", "table"]
},
{
"question": "What is the difference between Absolute and Relative cell references?",
"keywords": ["absolute", "relative", "$", "cell reference"]
},
{
"question": "Explain how Pivot Tables are useful in data analysis.",
"keywords": ["pivot", "summarize", "aggregate", "group"]
},
{
"question": "How would you handle missing values in an Excel dataset?",
"keywords": ["NA", "missing", "clean", "replace"]
},
]

# Step 2: Evaluation Function

def evaluate_answer(answer, keywords):
    score = 0
    for kw in keywords:
        if kw.lower() in answer.lower():
            score += 1
    return score / len(keywords)


# -------------------------------
# Step 3: Streamlit App
# -------------------------------
def main():
    st.title("🧑‍💻 AI Excel Mock Interviewer")

    # Initialize session state safely
    if "stage" not in st.session_state:
        st.session_state.stage = "intro"   # intro → questions → summary
        st.session_state.step = 0
        st.session_state.results = []

    # -------------------------------
    # Stage 1: Introduction
    # -------------------------------
    if st.session_state.stage == "intro":
        st.subheader(" Welcome!")
        st.write(
            """
            I am your AI-powered Excel Mock Interviewer.  
            Here how this session will go:
            1. I will ask you a series of Excel-related questions.  
            2. Please answer each question in detail.  
            3. At the end, I will provide feedback and a performance summary.  
            """
        )
        if st.button("Start Interview ▶️"):
            st.session_state.stage = "questions"
            st.experimental_rerun()

    # Initialize session state safely
    if "step" not in st.session_state:
        st.session_state["step"] = 0
    if "results" not in st.session_state:
        st.session_state["results"] = []

    # Ask questions
    if st.session_state["step"] < len(questions):
        q = questions[st.session_state["step"]]
        st.subheader(f"Q{st.session_state['step']+1}: {q['question']}")

        answer = st.text_area("Your Answer:", key=f"answer_{st.session_state['step']}")

        if st.button("Submit Answer", key=f"btn_{st.session_state['step']}"):
            score = evaluate_answer(answer, q["keywords"])
            st.session_state["results"].append((q["question"], score))
            st.session_state["step"] += 1
            st.experimental_rerun()

    # Show summary
    else:
        st.success("Interview Complete!")
        st.subheader("📊 Performance Summary")
        total_score = sum([s for _, s in st.session_state["results"]]) / len(st.session_state["results"])

        for q, s in st.session_state["results"]:
            st.write(f"**Question:** {q}")
            st.write(f"Score: {round(s*100)}%\\n")

        st.write(f"### Overall Performance: {round(total_score*100)}%")
        if total_score > 0.75:
            st.success("Excellent! You seem very strong in Excel.")
        elif total_score > 0.5:
            st.info("Good job! Some areas need improvement.")
        else:
            st.error("Needs more practice. Focus on Excel fundamentals.")

if __name__ == "__main__":
    main()