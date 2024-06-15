import streamlit as st
from database import insert_record, get_records, update_record, delete_record

# Create a Streamlit app
st.title("CRUD App with SQLite and Streamlit")

# Create
st.header("Add a new record")
with st.form(key='insert_form'):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    insert_button = st.form_submit_button(label='Add Record')
    if insert_button:
        insert_record(name, age)
        st.success("Record added successfully!")

# Read
st.header("View all records")
records = get_records()
for record in records:
    st.write(record)

# Update
st.header("Update a record")
with st.form(key='update_form'):
    record_id = st.number_input("Record ID to update", min_value=1, step=1)
    name = st.text_input("New Name")
    age = st.number_input("New Age", min_value=0, max_value=120, step=1)
    update_button = st.form_submit_button(label='Update Record')
    if update_button:
        update_record(record_id, name, age)
        st.success("Record updated successfully!")

# Delete
st.header("Delete a record")
with st.form(key='delete_form'):
    record_id = st.number_input("Record ID to delete", min_value=1, step=1)
    delete_button = st.form_submit_button(label='Delete Record')
    if delete_button:
        delete_record(record_id)
        st.success("Record deleted successfully!")

# Refresh records to display updated data
st.header("Updated Records")
records = get_records()
for record in records:
    st.write(record)
