import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("GVCEW RESULTS DASHBOARD")
# read the dataset
sem_list=['1-1','1-2']
semester= st.selectbox("Select semester", sem_list, key="selectbox11")
if semester=='1-1':
 data = pd.read_excel('22-Res11.xlsx')
if semester=='1-2':
 data = pd.read_excel('22-Res12.xlsx')
 
data.dropna(subset=['BRANCH'], inplace=True)
dept_list=['CSE','IT','CSM','EEE','ECE']
selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")
df=data[data["BRANCH"]==selected_dept]
df=df.dropna(axis=1, how='all')
def total_list():
 tpassed=df[(df['SGPA'] != 0) & (df['BRANCH'] == selected_dept)].shape[0]
 tfailed=df[(df['SGPA'] == 0) & (df['BRANCH'] == selected_dept)].shape[0]
 tpasspercentage=(tpassed/(tpassed+tfailed))*100;
 table_data1 = []
 table_data1.append({"Department": selected_dept, "TotalPassed": tpassed, "TotalFailed": tfailed,"pass%":tpasspercentage})
 total_strength=tpassed+tfailed
 
 fig, ax = plt.subplots()
 ax.pie([tpassed, tfailed, total_strength], labels=['Passed', 'Failed', 'Total Strength'], autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
 ax.axis('equal')
 plt.figure(figsize=(10,10))

# Adding a title
 plt.title('Pass/Fail/Total Strength Pie Chart')

# Showing the plot in Streamlit
 st.write("Pie Chart:")
 st.pyplot(fig)
 

 return table_data1
 
 
   
 
 

 

def count_failed(selected_dept):
    passed=[]
    failed=[]
     
    for i in range(3,11):
        passed.append(df[(df[df.columns[i]] != 'F')].shape[0])
        failed.append(df[(df[df.columns[i]] == 'F')].shape[0])
    return passed,failed


def generate_table_data():
 passed,failed=count_failed(selected_dept)
 sub_list=[]
 for i in range(3,11):
  sub_list.append(df.columns[i])
 data = []
 for name, pass_count, fail_count in zip(sub_list, passed, failed):
  passpercentage=(pass_count/(pass_count+fail_count))*100;
  data.append({"Subject Name": name, "Passed": pass_count, "Failed": fail_count,"Pass%":passpercentage})
 
     
 return data
 

# Main function
def main():
 
    st.title("Result Statistics")
    st.subheader("Department Pass/Fail Summary")
     
    
    table_data1=total_list()
    st.dataframe(pd.DataFrame(table_data1))
    
 
     
     
 
    
    st.subheader("Subject Pass/Fail Summary")
    # Generate table data
    table_data = generate_table_data()

    # Display the table
    st.dataframe(pd.DataFrame(table_data))

if __name__ == "__main__":
    main()
