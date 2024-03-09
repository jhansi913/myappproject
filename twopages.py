import streamlit as st

# Page 1 content
def page1():
    st.title("Page 1")
    st.write("This is page 1")
    if st.button("Go to Page 2"):
        page = "page2"
    else:
        page = "page1"
    return page

# Page 2 content
def page2():
    st.title("Page 2")
    st.write("This is page 2")
    if st.button("Go back to Page 1"):
        page = "page1"
    else:
        page = "page2"
    return page

# Main function
def main():
    page = "page1"
    while True:
        if page == "page1":
            page = page1()
        elif page == "page2":
            page = page2()

if __name__ == "__main__":
    main()
