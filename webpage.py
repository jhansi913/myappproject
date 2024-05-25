import streamlit as st
import streamlit.components.v1 as components
 

st.header("test html import")

HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
 
components.html(source_code)

     
# Display the HTML file in Streamlit
   
     

if __name__ == "__main__":
    main()
