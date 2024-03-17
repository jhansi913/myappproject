import pandas as pd
import streamlit as st
import numpy as np
st.title("GVCEW RESULTS DASHBOARD")
# read the dataset
sem_list=['1-1','1-2']
semester= st.selectbox("Select semester", sem_list, key="selectbox11")
if semester=='1-1':
 data = pd.read_excel('22-Res11.xlsx')
if semester=='1-2':
 data = pd.read_excel('22-Res12.xlsx')

dept_list=['CSE','IT','CSM','EEE','ECE']
selected_dept = st.selectbox("Select Department", dept_list, key="selectbox1")

 
data.dropna(subset=['BRANCH'], inplace=True)
df=data[data["BRANCH"]==selected_dept]
df=df.dropna(axis=1, how='all')

 

subjects=df.columns[3:11]
selected_subject = st.selectbox('Select a subject', subjects)

def grades_count():
        
        grades_counts = {
                'O': df[df[selected_subject] == 'O'].shape[0],
                'A+': df[df[selected_subject] == 'A+'].shape[0],
                'A': df[df[selected_subject] == 'A'].shape[0],
                'B+': df[df[selected_subject] == 'B+'].shape[0],
                'B': df[df[selected_subject] == 'B'].shape[0],
                'c':df[df[selected_subject]=='c'].shape[0],
                'P': df[df[selected_subject] == 'P'].shape[0]
        }
        grades_counts_df = pd.DataFrame(list(grades_counts.items()), columns=['Grade', 'Count'])
        st.write(f"Grades count for {selected_subject} in {selected_dept} department:")
        st.table(grades_counts_df)




def main():
    st.title("Subject Statistics")
     
    # Generate table data
    table_data = grades_count()

if __name__ == "__main__":
    main()
 






        
        


 
