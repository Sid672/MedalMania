import streamlit as st

# Function to display the home page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

# Function to display the games page
def games_page():
    st.title("Games Page")
    st.write("This is the games page. You can list different games here.")

# Function to display the country page
def country_page():
    st.title("Country Page")

# Main function for the Streamlit app
def main():

    # Navigation bar using Streamlit native methods
    st.sidebar.title("MedalMania")
    selected_page = st.sidebar.radio("Go to", ["Home", "Games", "Country"])

    # Display the selected page based on user choice
    if selected_page == "Home":
        home_page()
    elif selected_page == "Games":
        games_page()
    elif selected_page == "Country":
        country_page()


if __name__ == "__main__":
    main()
