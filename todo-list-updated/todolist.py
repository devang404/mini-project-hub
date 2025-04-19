import streamlit as st
import functions
# load existing tasks
tdos=functions.get_tdos()
def add_todo():
    todo=st.session_state['new_todo']+"\n"
    tdos.append(todo)
    functions.write_tdos(tdos)

def mark_todo_complete(index):
    tdos[index]=tdos[index].replace('\n','')+"[completed]\n"
    functions.write_tdos(tdos)

def delete_completed_tasks():
    tdos[:]=[todo for todo in tdos if "[completed]"not in todo]
    functions.write_tdos(tdos)
st.title("Do's")
st.subheader("BOOST YOUR PRODUCTIVITY")
#input for new task
new_todo=st.text_input(label="New Task",placeholder="Enter new task",on_change=add_todo,key="new_todo")

#display active task
st.subheader("Active Task")
for index,todo in enumerate(tdos):
    complete="[completed]"in todo
    if not complete:
        chx=st.checkbox(todo,key=f"todo_{index}")
        if chx:
            mark_todo_complete(index)
            st.write("")
#display completed tasks
st.subheader("Completed Tasks")
for index ,todo in enumerate(tdos):
    complete="[completed]"in todo
    if complete:
        # Display completed tasks with strikethrough
        st.markdown(f"<del>{todo}</del>",unsafe_allow_html=True )
if any("[completed]"in todo for todo in tdos):
    st.button("Delete All Completed Tasks",on_click=delete_completed_tasks)


