import streamlit as st
from services.auth.login_wall import render_login_wall


def main():
    st.set_page_config(
    page_icon="🏋️‍♀️",
    page_title="AI Real-time GYM Coach",
    initial_sidebar_state="expanded",
    layout="centered"

    )

st.title("AI Real-time GYM Coach")
st.write("Setup done!")
