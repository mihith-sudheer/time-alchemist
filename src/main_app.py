"""
main_app.py

Streamlit frontend for Time Alchemist.
"""

import streamlit as st
from bucketing import get_time_bucket
from recommender import load_tasks, recommend_tasks


# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(
    page_title="Time Alchemist",
    page_icon="⏳",
    layout="centered",
)

st.title("⏳ Time Alchemist")
st.subheader("Turn free minutes into gold ✨")

st.write(
    "Enter how much time you have, and Time Alchemist will suggest meaningful "
    "micro-tasks to help you make the most of it."
)

st.divider()

# ---------------------------
# Load Tasks
# ---------------------------
@st.cache_data
def get_task_data():
    return load_tasks()

tasks = get_task_data()

# ---------------------------
# User Input
# ---------------------------
minutes = st.slider(
    "How much time do you have?",
    min_value=1,
    max_value=240,
    value=15,
    step=1,
)

# ---------------------------
# Recommendation Logic
# ---------------------------
bucket = get_time_bucket(minutes)
recommendations = recommend_tasks(bucket, tasks)

# ---------------------------
# Display Output
# ---------------------------
st.markdown(f"### ⏱ Time bucket: **{bucket.replace('_', ' ').title()}**")

if recommendations:
    st.markdown("### ✨ Suggested tasks:")
    for i, task in enumerate(recommendations, start=1):
        st.markdown(f"**{i}.** {task}")
else:
    st.info("No tasks available for this time range yet.")

st.divider()

# ---------------------------
# Refresh Button
# ---------------------------
if st.button("🔁 Give me different suggestions"):
    st.experimental_rerun()


