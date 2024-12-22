import streamlit as st

# Page configuration
st.set_page_config(page_title="To-Do List", page_icon="📝", layout="centered")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a task to the list
def add_task(task):
    st.session_state.tasks.append({"task": task, "completed": False})

# Delete a task from the list
def delete_task(index):
    st.session_state.tasks.pop(index)

# Toggle task completion
def toggle_task(index):
    st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]

# Title of the app
st.title("📝 To-Do List")

# Input form to add a new task
with st.form("Add Task Form", clear_on_submit=True):
    new_task = st.text_input("Add a new task:", placeholder="Type your task here...")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        add_task(new_task)
        st.success("Task added!")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col1:
            # Checkbox to mark the task as completed
            if st.checkbox("", value=task["completed"], key=f"check-{idx}"):
                toggle_task(idx)
        with col2:
            # Display the task with a strikethrough if completed
            task_style = "line-through" if task["completed"] else "none"
            st.markdown(f"<span style='text-decoration:{task_style};'>{task['task']}</span>", unsafe_allow_html=True)
        with col3:
            # Button to delete the task
            if st.button("🗑️", key=f"delete-{idx}"):
                delete_task(idx)

# Footer
st.caption("Built with ❤️ using Streamlit.")
