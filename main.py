import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/me4.png")

with col2:
    st.title("Mario Umaña")
    st.write("")
    about_me = """
    Mi nombre es Mario, tengo 19 años y vivo en El Salvador. Soy un programador especializado en Python, actualmente estudiante de tercer año de Ingenieria informática en la Universidad José Simeón Cañas. Una de mis mayores pasiones es la tecnología, los datos y todo lo que se puede llegar a lograr teniendo conocimientos de ambos para optimizar nuestro entorno. 
    \n
    Trato de aprender algo nuevo siempre que puedo, mis hobbies varian mucho, incluyendo pasteleria, leer, hacer música y hacer caminatas en lugares fuera de la ciudad.
    """
    st.info(about_me)

st.write("")
st.write("")
page_content_information = """
Abajo puedes encontrar algunas de las aplicaciones que he construido con Python -
¡Puedes contactarme en cualquier momento!
"""
st.write(f"<h5 style= 'text-align: center;color:gray;'>{page_content_information}</h5>", unsafe_allow_html=True)
st.write("")

col3, col4 = st.columns(2)
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        