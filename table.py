import pandas as pd
import streamlit as st

# Sample data
data = pd.read_csv("C:\Users\jhans\Downloads\22-Res12.xlsx")  # Assuming you have your data in a CSV file

# Function to calculate pass percentage
def calculate_pass_percentage(passed, failed):
    total = passed + failed
    if total == 0:
        return 0
    else:
        return (passed / total) * 100


def count_passed(BRANCH):
    j=BRANCH
    sub_list_CIM= ['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']
    sub_list_EEE=['MATHEMATICS-II(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING AND NUMERICAL METHODS(4)','ELECTRONIC CIRCUIT ANALYSIS(5)','ENGLISH LANGUAGE LAB(6)','ELECTRONIC CIRCUIT ANALYSIS LAB(7)', 'COMPUTER PROGRAMMING AND NUMERICAL METHODS LAB(8)']
    countp =[]
    if j=='CSE' or j=='IT' or j=='CSM':
        for i in sub_list_CIM:
            countp.append(data[(data['BRANCH'] == j) & (data[i] != 'F')].shape[0])
    elif j=='EEE' or j=='ECE':
        for i in sub_list_EEE:
            countp.append(data[(data['BRANCH'] == j) & (data[i] != 'F')].shape[0])
    return countp


def count_failed(BRANCH):
    j=BRANCH
    sub_list_CIM= ['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']
    sub_list_EEE=['MATHEMATICS-II(1)','GREEN CHEMISTRY(2)','ENGLISH(3)','COMPUTER PROGRAMMING AND NUMERICAL METHODS(4)','ELECTRONIC CIRCUIT ANALYSIS(5)','ENGLISH LANGUAGE LAB(6)','ELECTRONIC CIRCUIT ANALYSIS LAB(7)', 'COMPUTER PROGRAMMING AND NUMERICAL METHODS LAB(8)']
    countf = []
    if j=='CSE' or j=='IT' or j=='CSM':
        for i in sub_list_CIM:
            countf.append(data[(data['BRANCH'] == j) & (data[i] == 'F')].shape[0])
    elif j=='EEE' or j=='ECE':
        for i in sub_list_EEE:
            countf.append(data[(data['BRANCH'] == j) & (data[i] == 'F')].shape[0])
    return countf

def generate_table_data():
    passed[]
    failed=[]
    table_data = []
    departments = ['CSE', 'ECE', 'IT' , 'EEE','CSM']
    subject_code=[]
     
    subject_name=['MATHEMATICS-II(1)', 'PHYSICS(2)', 'ELEMENTS OF ELECTRONICS ENGINEERING(3)' , 'DATA STRUCTURES USING C(4)','DIGITAL LOGIC DESIGN(5)','LINUX ADMINISTRATION LAB(6)','PHYSICS LAB(7)','DATA STRUCTURES LAB(8)']
    selected_department = st.selectbox('Select a department', departments)
    registered=data[(data['BRANCH'] == selected_department)].shape[0]
    passed = count_passed(selected_department)
    faied = count_failed(selected_department)
    pass_percentage = calculate_pass_percentage(passed, failed)
    table_data.append({
            'Subject Code': subject_code,
            'Subject Name': subject_name,
            'Registered': registered,
            'Passed': passed,
            'Failed': failed,
            'Pass Percentage': pass_percentage
        })
    return table_data
 

 
 

       
      
       

 

# Main function
def main():
    st.title("Subject Statistics")

    # Generate table data
    table_data = generate_table_data()

    # Display the table
    st.table(pd.DataFrame(table_data))

if __name__ == "__main__":
    main()
