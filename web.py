import streamlit as st
from modules import functions

todos=functions.get_todos()

st.title("My To-Do App")
st.subheader("This is a simple To-Do App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter your task")