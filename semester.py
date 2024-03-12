import streamlit as st
import pandas as pd

grades_data = {
    '1-2': {
        'CSE': ['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']
             
        'ECE':['MATHEMATICS-II(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING AND NUMERICAL METHODS(4)','ELECTRONIC CIRCUIT ANALYSIS(5)','ENGLISH LANGUAGE LAB(6)','ELECTRONIC CIRCUIT ANALYSIS LAB(7)', 'COMPUTER PROGRAMMING AND NUMERICAL METHODS LAB(8)']

        'IT':['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']

        'EEE':['MATHEMATICS-II(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING AND NUMERICAL METHODS(4)','ELECTRONIC CIRCUIT ANALYSIS(5)','ENGLISH LANGUAGE LAB(6)','ELECTRONIC CIRCUIT ANALYSIS LAB(7)', 'COMPUTER PROGRAMMING AND NUMERICAL METHODS LAB(8)']

        'CSM':['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']
         
    }
    '1-1': {
        'CSE':['MATHEMATICS-I(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING USING C(4)','IT ESSENTIALS(5)']
        
        'ECE':['MATHEMATICS-I(1)','PHYSICS(2)','DIGITAL LOGIC DESIGN(3)','ELECTRONICS DEVICE AND CIRCUITS(4)','NETWORK THEORY AND MACHINES(5)']
        
        'IT':['MATHEMATICS-I(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING USING C(4)','IT ESSENTIALS(5)']
        
        'EEE':['MATHEMATICS-I(1)','PHYSICS(2)','INTRODUCTION TO PYTHON(3)','FUNDAMENTALS OF ELECTRICAL ENGINEERING(4)','BASIC ELECTRONICS ENGINEERING(5)']
        
        'CSM':['MATHEMATICS-I(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING USING C(4)','IT ESSENTIALS(5)']
        
}
 
# Define options for dropdowns
semesters = list(grades_data.keys())
departments = ['CSE', 'ECE', 'IT' , 'EEE']

# Create the dropdowns
selected_semester = st.selectbox('Select a semester', semesters)
selected_department = st.selectbox('Select a department', departments)

# Display the dropdowns
if selected_semester=='1-2' and selected_department:
    data = pd.read_excel('/content/22-Res12.xlsx')
    data.dropna(subset=['BRANCH'], inplace=True)
 
    selected_subject = st.selectbox('Select a subject', list(grades_data[selected_semester][selected_department].keys()))

    # Display the table
    if selected_subject:
        filtered_data = data[data['BRANCH'] == selected_department]
        grades_counts = {
                'O': filtered_data[filtered_data[selected_subject] == 'O'].shape[0],
                'A+': filtered_data[filtered_data[selected_subject] == 'A+'].shape[0],
                'A': filtered_data[filtered_data[selected_subject] == 'A'].shape[0],
                'B+': filtered_data[filtered_data[selected_subject] == 'B+'].shape[0],
                'B': filtered_data[filtered_data[selected_subject] == 'B'].shape[0],
                'P': filtered_data[filtered_data[selected_subject] == 'P'].shape[0]
        }
        grades_counts_df = pd.DataFrame(list(grades_counts.items()), columns=['Grade', 'Count'])
        st.write(f"Grades count for {selected_subject} in {selected_department} department:")
        st.table(grades_counts_df)


if selected_semester=='1-1' and selected_department:
    data = pd.read_excel(' ')
    data.dropna(subset=['BRANCH'], inplace=True)
 
    selected_subject = st.selectbox('Select a subject', list(grades_data[selected_semester][selected_department].keys()))

    # Display the table
    if selected_subject:
        filtered_data = data[data['BRANCH'] == selected_department]
        grades_counts = {
                'O': filtered_data[filtered_data[selected_subject] == 'O'].shape[0],
                'A+': filtered_data[filtered_data[selected_subject] == 'A+'].shape[0],
                'A': filtered_data[filtered_data[selected_subject] == 'A'].shape[0],
                'B+': filtered_data[filtered_data[selected_subject] == 'B+'].shape[0],
                'B': filtered_data[filtered_data[selected_subject] == 'B'].shape[0],
                'P': filtered_data[filtered_data[selected_subject] == 'P'].shape[0]
        }
        grades_counts_df = pd.DataFrame(list(grades_counts.items()), columns=['Grade', 'Count'])
        st.write(f"Grades count for {selected_subject} in {selected_department} department:")
        st.table(grades_counts_df)

 






        
        


 
