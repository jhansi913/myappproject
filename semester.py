import streamlit as st
import pandas as pd

# Sample data
grades_data = {
    'Semester 1': {
        'CSE': {
            'Maths': ['A+', 'A', 'B', 'A+', 'B+', 'O', 'A', 'A', 'B+', 'A+'],
            'Physics': ['A', 'B+', 'O', 'A', 'A+', 'A+', 'B', 'A+', 'A', 'B+'],
            'Chemistry': ['A', 'B+', 'A+', 'B+', 'O', 'B', 'A+', 'A+', 'A+', 'A']
        },
        'ECE': {
            'Maths': ['A+', 'A', 'B', 'A+', 'B+', 'O', 'A', 'A', 'B+', 'A+'],
            'Physics': ['A', 'B+', 'O', 'A', 'A+', 'A+', 'B', 'A+', 'A', 'B+'],
            'Chemistry': ['A', 'B+', 'A+', 'B+', 'O', 'B', 'A+', 'A+', 'A+', 'A']
        },
        'Mechanical': {
            'Maths': ['A+', 'A', 'B', 'A+', 'B+', 'O', 'A', 'A', 'B+', 'A+'],
            'Physics': ['A', 'B+', 'O', 'A', 'A+', 'A+', 'B', 'A+', 'A', 'B+'],
            'Chemistry': ['A', 'B+', 'A+', 'B+', 'O', 'B', 'A+', 'A+', 'A+', 'A']
        }
    }
}

# Define options for dropdowns
semesters = list(grades_data.keys())
departments = ['CSE', 'ECE', 'Mechanical']

# Create the dropdowns
selected_semester = st.selectbox('Select a semester', semesters)
selected_department = st.selectbox('Select a department', departments)

# Display the dropdowns
if selected_semester and selected_department:
    selected_subject = st.selectbox('Select a subject', list(grades_data[selected_semester][selected_department].keys()))

    # Display the table
    if selected_subject:
        grades = grades_data[selected_semester][selected_department][selected_subject]
        grades_counts = {grade: grades.count(grade) for grade in ['O', 'A+', 'A', 'B+', 'B', 'P']}
        df = pd.DataFrame(list(grades_counts.items()), columns=['Grade', 'Count'])
        st.write(df)
