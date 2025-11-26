import streamlit as st
import pandas as pd

#no supe como quitar app, sin que me diera error,
st.set_page_config(
    page_title="Dashboard Examen",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    return pd.read_csv("datos/exam_data.csv")

if "data" not in st.session_state:
    st.session_state.data = load_data()

