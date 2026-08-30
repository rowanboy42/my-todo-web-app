import streamlit as st
from modules import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize() + "\n")
    f.write_todos(todos)
    st.session_state['new_todo'] = ''

st.title("My To-do App")
st.subheader("This is my To-do App")
st.write("This app is to increase your productivity!")
#st.write(st.context.headers["User-Agent"])

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#st.session_state
