import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    send_button = st.form_submit_button("Submit")
    if send_button:
        message = message + user_email
        print("I was pressed!")

st.session_state