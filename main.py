import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/me4.png")
    pass

with col2:
    st.title("Mario Umaña")
    about_me = """
    Mi nombre es Mario. Soy un programador de Python, actualmente estudiante de tercer año de Ingenieria informática en la Universidad José Simeón Cañas. Una de mis mayores pasiones es la tecnología, los datos y todo lo que se puede llegar a lograr teniendo conocimientos de ambos para optimizar nuestro entorno.
    """
    st.write(about_me)