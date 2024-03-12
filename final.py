import pandas as pd
# read the dataset
data = pd.read_excel('22-Res12.xlsx')
data.dropna(subset=['BRANCH'], inplace=True)

def count_failed(selected_dept):
    passed=[]
    failed=[]
    df=data[data['BRANCH'] == selected_dept]
    df = df.dropna(axis=1, how='all')
    for i in range(3,11):
        passed.append(df[(df[df.columns[i]] != 'F')].shape[0])
        failed.append(df[(df[df.columns[i]] == 'F')].shape[0])
    return passed,failed


def generate_table_data():
    dept_list=data['BRANCH'].unique()
    selected_dept = st.selectbox('Select a department', dept_list)
    passed,failed=count_failed(selected_dept)
    sub_list=[]
    for i in range(3,11):
        sub_list.append(df.columns[i]])
    table_data = []
    table_data.append({
              
            'Subject Name': sub_list,
            'Passed': passed,
            'Failed': failed,
             
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
