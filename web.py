import streamlit as st
import datetime
from modules import functions


def add():
    task = functions.get_tasks()
    date = str(st.session_state["date"])
    time = str(st.session_state["time"])
    new_task = st.session_state["todo"] + " " + "(" + date + "; " + time + ")" + "\n"
    task.append(new_task)
    functions.write_tasks(task)


st.title("PJ's ToDo App")
st.header("An App to keep track of PJ's daily tasks")
st.subheader("All Your Tasks, In one Place")

tasks = functions.get_tasks()

for index, todo in enumerate(tasks):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        tasks.remove(tasks[index])
        functions.write_tasks(tasks)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter New Task...", key="todo")
st.date_input(label="", key="date")
st.time_input(label="", key="time")
st.button(label="Add Task", on_click=add, key="button")


