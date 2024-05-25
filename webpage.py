import streamlit as st

def main():
    st.title("Embedding HTML in Streamlit")
    with open('home.html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    st.markdown(html_content, unsafe_allow_html=True)

    # Read the HTML files
    

     
# Display the HTML file in Streamlit
   
     

if __name__ == "__main__":
    main()
