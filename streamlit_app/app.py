import streamlit as st
import numpy as np
from model_inference import model_prediction

st.set_page_config(
    page_title="Personality Survey",
    layout="centered"
)

st.markdown("""
<style>
body {
    font-family: 'Inter', sans-serif;
}
.block-container {
    padding-top: 2rem;
}
.question {
    margin-top: 25px;
    margin-bottom: 25px;
    padding: 18px 22px;
    background: #C4C0BE;
    border-radius: 12px;
    border: 1px solid #e0e6ed;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Personality-Based Survey Prediction App")

st.write("""
Welcome to the **Personality Scenario Assessment**.  
Each question presents a situation where you can select how likely you are to respond.

**Scale: 1 = least likely, 5 = most likely.**

Choose a prediction type and answer honestly for best results.
""")

def likert(question, key):
    st.markdown(f"<div class='question'>{question}</div>", unsafe_allow_html=True)
    return st.slider("", 1, 5, 1, key=key)

st.subheader("Prediction Type")

prediction_mode = st.radio(
    "Select prediction mode:",
    ["Regression", "Classification"],
    horizontal=True
)

st.subheader("Basic Information")

age_group = st.selectbox(
    "Which age group do you belong to?",
    ["18–30", "31 or Older"]
)

age_group_18_30 = 1 if age_group == "18–30" else 0


QUESTIONS = [
    ("C8", "Your class assigns a long project that requires steady progress over several weeks. Each student is responsible for different tasks, and the group counts on everyone to keep things moving. As the weeks go by, other commitments come up, and no one checks in on whether you are keeping up with your share. How likely are you to let your tasks slide or put them off even though the group is depending on you, with 5 being the most likely?"),

    ("C9", "You set up a detailed weekly plan that spells out your study sessions, errands, meals, breaks, and the times you want to relax. As the week unfolds, unexpected invitations, tiring days, and extra assignments appear. How likely are you to continue following your planned schedule instead of adjusting things freely as you go, with 5 being the most likely?"),

    ("C1", "You have an important meeting or event coming up that could influence something meaningful for you. In the days leading to it, you have the chance to organize everything, check your materials, and rehearse what you need to do. How likely are you to arrive feeling fully prepared rather than relying on last-minute effort, with 5 being the most likely?"),

    ("C10", "You are given a task that requires careful attention, such as formatting a document, assembling something correctly, or organizing data. Even small errors would affect the outcome. How likely are you to work slowly and precisely so that every detail is correct, with 5 being the most likely?"),

    ("C5", "You have several chores waiting for you at home, such as cleaning, laundry, or organizing something that has piled up. You have time to do them now, but you could also relax or put them off until later. How likely are you to take care of these chores right away rather than delaying them, with 5 being the most likely?"),

    ("C4", "You begin working on a project that involves papers, tools, devices, or multiple files. As you get deeper into the work, items build up around you. How likely are you to let your workspace grow more scattered and disorganized instead of keeping things neat, with 5 being the most likely?"),

    ("N7", "Over the course of a normal week, you deal with school, work, friends, and unexpected situations. Some days feel easy while others feel stressful. How likely are you to experience noticeable shifts in your mood from one moment to the next, with 5 being the most likely?"),

    ("C3", "You review a document, assignment, or message before submitting it. It contains small formatting issues, grammar mistakes, or unclear phrases that require careful review to catch. How likely are you to notice these small details and fix them, with 5 being the most likely?"),

    ("A10", "You join a group where someone new seems quiet or unsure of themselves. Conversation begins, and there is a chance to include them. How likely are you to help them feel comfortable and welcomed rather than leaving them on the outside of the discussion, with 5 being the most likely?"),

    ("C2", "Throughout an average day, you use items like jackets, notebooks, chargers, and water bottles. As you move from place to place, you set things down and switch tasks frequently. How likely are you to leave your belongings scattered in different spots rather than keeping them together and organized, with 5 being the most likely?"),

    ("N5", "You are concentrating on something important when small interruptions occur, such as noises, messages, or people asking quick questions. How likely are you to lose focus or feel unsettled by these interruptions, with 5 being the most likely?"),

    ("A8", "You are in the middle of something you want to finish when a friend reaches out asking for help with a problem. Assisting them would require pausing what you are doing. How likely are you to set aside your own plans to make time for them, with 5 being the most likely?"),

    ("O2", "You encounter an idea that is theoretical and not tied to a concrete example, such as a philosophical concept or a complex model. How likely are you to find it confusing or difficult to grasp compared to more practical ideas, with 5 being the most likely?"),

    ("E10", "You arrive at a social gathering where most of the people are unfamiliar to you. Small groups begin forming, and conversations start to flow. How likely are you to stay mostly quiet and observe rather than joining in, with 5 being the most likely?")
]


st.subheader("Scenario-Based Questions")

responses = {}

if prediction_mode == "Regression":
    st.caption("These questions are used for numerical score prediction.")
    for code, question in QUESTIONS:
        responses[code] = likert(question, key=code)

else:
    st.caption("These questions are used for category-based prediction.")
    for code, question in QUESTIONS:
        responses[code] = likert(question, key=code)


if st.button("Predict"):
    if prediction_mode == "Regression":
        task_type = prediction_mode.lower()  
        feature_order = [code for code, _ in QUESTIONS]
        X = np.array(
            [responses[c] for c in feature_order] + [age_group_18_30]
        ).reshape(1, -1)

        pred = model_prediction(X, "regression")
        st.success(f"Your predicted score is: {pred:.2f}")

    else:
        feature_order = [code for code, _ in QUESTIONS]
        X = np.array(
            [responses[c] for c in feature_order] + [age_group_18_30]
        ).reshape(1, -1)

        pred_class = model_prediction(X, "classification")

        st.success(f"Predicted class: {pred_class}")