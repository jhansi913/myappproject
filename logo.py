import streamlit as st
st.set_page_config(layout="wide")
# Custom HTML/CSS for the banner"C:\Users\jhans\Desktop\rseume]\logophoto.jpeg"
custom_html = """
<div class="banner">
    <img src="logophoto.jpeg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 160%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
st.components.v1.html(custom_html)

 

# Main content
st.title("Main Content")
st.write("Welcome to my Streamlit app!")
st.write("This is the main content area.")
