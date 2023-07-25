import streamlit as st
import pickle 
import pandas as pd


def run_streamlit_app(app_file):
    subprocess.Popen(["streamlit", "run", app_file])

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
    #To extract country name
    def make_list(dF, col_name):
        l = []
        for i in country_dict[col_name].values():
            l.append(i)
        return l

    def Details_of(ct, medal_data):
        st.write(ct.upper())
        st.write("Total gold medal: ", medal_data[ct][0])
        st.write("Total silver medal: ", str(medal_data[ct][1]))
        st.write("Total bronze medal: ", str(medal_data[ct][2]))
        st.write("Total medal: ", medal_data[ct][3])
        return

    #Loading dictionary of countries dataset
    country_dict = pickle.load(open('countries_dict.pkl', 'rb'))

    # print(country_dict.keys())

    #Country name list
    country_list = make_list(country_dict, 'countries ')

    #Country code list
    code_list = make_list(country_dict, 'ioc_code ')

    #Country gold list
    gold_list = make_list(country_dict, 'total_gold')

    #Country silver list
    silver_list = make_list(country_dict, 'total_silver')

    #Country bronze list
    broze_list = make_list(country_dict, 'total_bronze')

    #Country total medal
    total_medal = make_list(country_dict, 'total_total ')

    #Creating combine data of country
    medal_data = {}
    for i in range(0, len(country_list)):
        medal_data[country_list[i]] = [gold_list[i], int(silver_list[i]), int(broze_list[i]), total_medal[i], code_list[i]]

    #Title of page
    st.title("Countries")

    #SearchBox
    selected_ct = st.selectbox('Search country', country_list)

    if st.button('Details'):
        st.markdown(f'<img src="https://flagsapi.com/{medal_data[selected_ct][4][1:3]}/flat/64.png">', unsafe_allow_html = True)
        Details_of(selected_ct, medal_data)

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
