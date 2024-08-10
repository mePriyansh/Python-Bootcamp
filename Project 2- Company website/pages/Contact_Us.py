import streamlit as st
from send_email import send_email
import pandas

df=pandas.read_csv("topics.csv")

st.title("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email")
    options = st.selectbox("Enter topics you want to discuss?",df["topic"])
    raw_message = st.text_area("Enter your message")
    message=f"""\
Subject:New email fom {user_email}

From: {user_email}
Topic: {options}
{raw_message} 
"""
    button=st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Email sent successfully")
    