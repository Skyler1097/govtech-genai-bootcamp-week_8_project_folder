import streamlit as st

st.write("# Welcome to my Streamlit App! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
"""
)

with st.expander("How to use this app"):
    st.write('''
        1. Enter your prompt in the text area
        2. Click the 'Submit' button
        3. The app will generate a text completion based on your prompt
    ''')