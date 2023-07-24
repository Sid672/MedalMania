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
    # Add custom CSS for the navigation bar
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

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
