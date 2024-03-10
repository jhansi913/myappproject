import pandas as pd
import streamlit as st

# Sample data
data = pd.read_csv("your_data.csv")  # Assuming you have your data in a CSV file

# Function to calculate pass percentage
def calculate_pass_percentage(passed, failed):
    total = passed + failed
    if total == 0:
        return 0
    else:
        return (passed / total) * 100

# Function to generate data for the table
def generate_table_data():
    table_data = []
    for index, row in data.iterrows():
        subject_code = row['Subject_Code']
        subject_name = row['Subject_Name']
        registered = row['Registered']
        passed = row['Passed']
        failed = row['Failed']
        pass_percentage = calculate_pass_percentage(passed, failed)
        table_data.append({
            'S.No': index + 1,
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
