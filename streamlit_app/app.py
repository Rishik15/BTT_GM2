import streamlit as st
import numpy as np
from model_inference import model_prediction

st.title("Personality-Based Survey Prediction App")

st.write("Please answer each scenario-based question on a scale of 1–5 (5 = most positive).")

def likert(question):
    return st.slider(question, 1, 5, 3)

age_group = st.selectbox(
    "Which age group do you belong to?",
    ["18–30", "Other"]
)

age_group_18_30 = 1 if age_group == "18–30" else 0

C8  = likert("You are working on a group project. How likely are you to complete your assigned task without reminders?")
C9  = likert("Your week is fully planned. How closely do you follow your scheduled routine?")
C1  = likert("Before an important meeting or event, how prepared are you?")
C10 = likert("When assigned a task requiring precision, how thorough are you?")
C5  = likert("When you have chores to do, how quickly do you complete them?")
C4  = likert("While working on a project, how well do you keep your space organized?")
N7  = likert("During a typical week, how stable are your moods?")
C3  = likert("While proofreading a document, how well do you catch mistakes and details?")
A10 = likert("When meeting someone new, how good are you at making them feel at ease?")
C2  = likert("How well do you keep your belongings organized in daily life?")
N5  = likert("When interrupted during work, how difficult is it to disturb or stress you?")
A8  = likert("If a friend needs help while you're busy, how likely are you to make time for them?")
O2  = likert("How well do you understand abstract or theoretical ideas?")
E10 = likert("At a networking event, how comfortable are you speaking with strangers?")


if st.button("Predict"):
    X = np.array([
        C8, C9, C1, C10, C5, C4, N7, C3, A10, C2, N5, A8, O2, E10,
        age_group_18_30
    ]).reshape(1, -1)

    pred = model_prediction(X)

    st.success(f"Prediction: {pred}")