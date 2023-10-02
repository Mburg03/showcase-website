import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown("<h1 style= 'text-align: center;'>About me</h1>",unsafe_allow_html=True)
st.write("-----------------------------")
st.write("")
st.write("")
col1, empty_col2, col2 = st.columns([2.0,0.2,2.0])


with col1:
    st.write("<h2></h2>",unsafe_allow_html=True)
    st.image("./images/me5.png")

with col2:
    st.write("<h2>Mario Umaña</h2>",unsafe_allow_html=True)
    st.write("")
    about_me = """
    My name is Mario, I am 19 years old, and I live in El Salvador. I am a Python specialist and currently a third-year student of Computer Engineering at José Simeón Cañas University. One of my greatest passions is technology, data, and everything that can be achieved by having knowledge of both to optimize our environment.
    \n
    I strive to learn something new whenever I can. My hobbies vary widely, including baking, reading, making music, and taking hikes in places outside the city.
    """
    st.info(about_me)

st.write("")
st.write("")

page_content_information = """
Below you can find some of the applications I have built using Python.
"""
contact_me_plain_text = "You can contact me at any time!"

st.write(f"<h5 style= 'text-align: center;color:gray;'>{page_content_information}</h5>", unsafe_allow_html=True)
st.write(f"<h5 style= 'text-align: center;color:gray;'>{contact_me_plain_text}</h5>", unsafe_allow_html=True)
st.write("")
st.write("")

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():   
        st.header(row["title"])
        st.write(row["description"])
        st.image("./images/" + row["image"])
        st.write("[Source Code](https://github.com/Mburg03?tab=repositories)")
        st.write("")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./images/" + row["image"])
        st.write("[Source Code](https://github.com/Mburg03?tab=repositories)")        
        st.write("")
                