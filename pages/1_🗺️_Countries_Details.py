import streamlit as st
import pickle
import pandas as pd
import numpy as np

# To extract country name
st.set_page_config(page_title="Countries Details", page_icon="🗺️")
st.sidebar.header("Countries Details")
# Title of page
st.title("Countries Details")

# Loading dictionary of countries dataset
country_dict = pickle.load(open('countries_dict.pkl', 'rb'))
results = pickle.load(open('results.pkl', 'rb'))


def make_list(dF, col_name):
    l = []
    for i in country_dict[col_name].values():
        l.append(i)
    return l


def make_list2(dictionary):
    l = []
    for i in dictionary.values():
        l.append(i)
    return l


def Details_of(ct, medal_data):
    st.write(" " + ct.upper())
    gold = medal_data[ct][0]
    silver = str(medal_data[ct][1])
    bronze = str(medal_data[ct][2])
    total = medal_data[ct][3]

    table_data = {
        'Gold Medal 🥇': [gold],
        'Silver Medal 🥈': [silver],
        'Bronze Medal 🥉': [bronze],
        'Total Medals 🏅': [total]
    }
    df = pd.DataFrame(table_data)

    st.dataframe(df, hide_index=True)
    return


# Country name list
country_list = make_list(country_dict, 'countries ')
# Country code list
code_list = make_list(country_dict, 'ioc_code ')
# Country gold list
gold_list = make_list(country_dict, 'total_gold')
# Country silver list
silver_list = make_list(country_dict, 'total_silver')
# Country bronze list
broze_list = make_list(country_dict, 'total_bronze')
# Country total medal
total_medal = make_list(country_dict, 'total_total ')
# Country code list
country_code_2 = make_list2(results['country_code'])
country_code_3 = make_list2(results['country_3_letter_code'])


code_list1 = {}
for i in range(0, len(country_code_2)):
    code_list1[country_code_3[i]] = country_code_2[i]

# Creating combine data of country
medal_data = {}
for i in range(0, len(country_list)):
    medal_data[country_list[i]] = [gold_list[i], int(
        silver_list[i]), int(broze_list[i]), total_medal[i], code_list[i]]

# SearchBox
selected_ct = st.selectbox('Search country', country_list)

if st.button('Details'):
    tab1, tab2, tab3 = st.tabs(
        ["Medal Tally 🏅", "Medal Details 📜", "Athlete Profiles ⛹️"])

    with tab1:
        st.header("Medal Tally 🏅")
        st.markdown(
            f'<img src="https://flagsapi.com/{code_list1[medal_data[selected_ct][4][1:4]]}/flat/64.png">', unsafe_allow_html=True)
        Details_of(selected_ct, medal_data)

    with tab2:
        st.header("Medal Details 📜")

    with tab3:
        st.header("Athlete Profiles ⛹️")
