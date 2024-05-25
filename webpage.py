import streamlit as st

def main():
    st.title("Embedding HTML in Streamlit")

    # Read the HTML files
   with open('home.html', 'r', encoding='utf-8') as html_file:
       html_content = html_file.read()

     
# Display the HTML file in Streamlit
  st.markdown(html_content, unsafe_allow_html=True)
     

if __name__ == "__main__":
    main()
