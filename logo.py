import streamlit as st
st.set_page_config(layout="wide")
# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.shiksha.com%2Fcollege%2Fgayatri-vidya-parishad-college-of-engineering-for-women-visakhapatnam-46521&psig=AOvVaw2CRCtiJMD7sthv3TAp2yCQ&ust=1710517637640000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMCqyvSM9IQDFQAAAAAdAAAAABAE" alt="Banner Image">
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
