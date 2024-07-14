import streamlit as st
from modules import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is a simple To-Do App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter your task",
              on_change=add_todo, key="new_todo")