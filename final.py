import pandas as pd
import streamlit as st
import numpy as np
# read the dataset
data = pd.read_excel('22-Res11.xlsx')
data.dropna(subset=['BRANCH'], inplace=True)
dept_list=['CSE','IT','CSM','EEE','ECE']
selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")
df=data[data["BRANCH"]==selected_dept]
df=df.dropna(axis=1, how='all')
 

 

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
  
 table_data = []
 table_data.append({
              
            'Subject Name': sub_list,
            'Passed': passed,
            'Failed': failed,
             
    })
 
 data = []
 for name, pass_count, fail_count in zip(sub_list, passed, failed):
  data.append({"Subject Name": name, "Passed": pass_count, "Failed": fail_count})
     

 return data
 

# Main function
def main():
    st.title("Subject Statistics")
     
     
 
    

    # Generate table data
    table_data = generate_table_data()

    # Display the table
    st.dataframe(pd.DataFrame(table_data))

if __name__ == "__main__":
    main()
