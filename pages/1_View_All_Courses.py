import streamlit as st
import json
import pandas as pd

filepath = './data/courses-full.json'

st.write("Available courses")

def load_json_to_table(file_path):

    with open(file_path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    st.dataframe(df)  

load_json_to_table(filepath)