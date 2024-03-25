import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("GVCEW RESULTS DASHBOARD")
# read the dataset
sem_list=['1-1','1-2']
 
 
 
data.dropna(subset=['BRANCH'], inplace=True)
dept_list=['CSE','IT','CSM','EEE','ECE']
 
df=data[data["BRANCH"]==selected_dept]
df=df.dropna(axis=1, how='all')
def welcome_page():
    st.title("Welcome to GVPCEW Dashboard")
    
    st.image("gvpcew.jpg")

def total_list():
 tpassed=df[(df['SGPA'] != 0) & (df['BRANCH'] == selected_dept)].shape[0]
 tfailed=df[(df['SGPA'] == 0) & (df['BRANCH'] == selected_dept)].shape[0]
 tpasspercentage=(tpassed/(tpassed+tfailed))*100;
 table_data1 = []
 table_data1.append({"Department": selected_dept, "TotalPassed": tpassed, "TotalFailed": tfailed,"pass%":tpasspercentage})
 total_strength=tpassed+tfailed
 fig, ax = plt.subplots()
 plt.pie([tpassed, tfailed, total_strength], labels=['Passed', 'Failed', 'Total Strength'], autopct='%1.1f%%', startangle=90)
 plt.axis('equal')
 plt.title('Pass/Fail/Total Strength Pie Chart')
 st.write("Pie Chart:")
 st.pyplot(fig)
 return table_data1

def grades_count():
 semester= st.selectbox("Select semester", sem_list, key="selectbox11")
 selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")
 if semester=='1-1':
  data = pd.read_excel('22-Res11.xlsx')
 if semester=='1-2':
  data = pd.read_excel('22-Res12.xlsx')
 subjects=df.columns[3:11]
 selected_subject = st.selectbox('Select a subject', subjects)
    
 grades_counts = {
                'O': df[df[selected_subject] == 'O'].shape[0],
                'A+': df[df[selected_subject] == 'A+'].shape[0],
                'A': df[df[selected_subject] == 'A'].shape[0],
                'B+': df[df[selected_subject] == 'B+'].shape[0],
                'B': df[df[selected_subject] == 'B'].shape[0],
                'C':df[df[selected_subject]=='C'].shape[0],
                'P': df[df[selected_subject] == 'P'].shape[0]
        }
 grades_counts_df = pd.DataFrame(list(grades_counts.items()), columns=['Grade', 'Count'])
  
 fig, ax = plt.subplots()  # Create a figure and axis object
 ax.bar(grades_counts_df['Grade'], grades_counts_df['Count'])

# Adding labels and title
 ax.set_xlabel('Grades')
 ax.set_ylabel('Count')
 ax.set_title('Grade Distribution')

# Showing the plot in Streamlit
 st.write("Bar Chart:")
 st.pyplot(fig) 
 st.write(f"Grades count for {selected_subject} in {selected_dept} department:")
 st.table(grades_counts_df)

 
 
   
 
 

 

def count_failed(selected_dept):
    passed=[]
    failed=[]
     
    for i in range(3,11):
        passed.append(df[(df[df.columns[i]] != 'F')].shape[0])
        failed.append(df[(df[df.columns[i]] == 'F')].shape[0])
    return passed,failed


def generate_table_data():
 semester= st.selectbox("Select semester", sem_list, key="selectbox11")
 selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")
 if semester=='1-1':
  data = pd.read_excel('22-Res11.xlsx')
 if semester=='1-2':
  data = pd.read_excel('22-Res12.xlsx')
 passed,failed=count_failed(selected_dept)
 sub_list=[]
 for i in range(3,11):
  sub_list.append(df.columns[i])
 data = []
 for name, pass_count, fail_count in zip(sub_list, passed, failed):
  passpercentage=(pass_count/(pass_count+fail_count))*100;
  data.append({"Subject Name": name, "Passed": pass_count, "Failed": fail_count,"Pass%":passpercentage})
 
     
 return data


def main():
    page = st.sidebar.radio("Navigation", ["welcome_page", "generate_table_data","grades_count"])

    if page==welcome_page:
        welcome_page()

    elif page=="generate_table_data":
        st.title("Result Statistics")
        st.subheader("Department Pass/Fail Summary")
        table_data1=total_list()
        st.dataframe(pd.DataFrame(table_data1))
        st.subheader("Subject Pass/Fail Summary")
        table_data = generate_table_data()
        st.dataframe(pd.DataFrame(table_data))

    elif page=="grades_count":
        st.title("Subject Statistics")
        table_data = grades_count()

        
        
 
 
 


if __name__ == "__main__":
    main()
