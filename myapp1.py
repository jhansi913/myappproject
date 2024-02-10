import streamlit as st

def welcome_page():
    st.title("Welcome to My App")
    st.write("Please log in to continue.")

def login_page():
    st.title("Login Page")

    # User input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check credentials (for demonstration purposes, hardcoded)
        if username == "admin" and password == "password":
            st.success("Logged in as {}".format(username))
            # Redirect to home page or some other page after successful login
        else:
            st.error("Invalid username or password. Please try again.")

def main():
    page = st.sidebar.radio("Navigation", ["Welcome", "Login"])

    if page == "Welcome":
        welcome_page()
    elif page == "Login":
        login_page()

if __name__ == "__main__":
    main()
