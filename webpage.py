import streamlit as st

def main():
    st.title("Embedding HTML in Streamlit")

    # Read the HTML files
    with open("home.html", "r", encoding="utf-8") as file1:
        html_content1 = file1.read()
    
     

    # Display HTML content in Streamlit app
    st.subheader("Page 1")
    st.components.v1.html(html_content1, height=600, scrolling=True)
    
     

if __name__ == "__main__":
    main()
