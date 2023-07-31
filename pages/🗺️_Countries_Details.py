import streamlit as st
import pickle
import pandas as pd
import numpy as np

# To extract country name
st.set_page_config(page_title="Countries Details", page_icon="🗺️")
# st.sidebar.header('''Countries Details
#                   Medal Tally
#                   Medal Details''')
# Title of page
st.title("Countries Details")
st.write("The country details encompass comprehensive information, including the medal tally, detailed breakdown of medals won, and in-depth athlete profiles.")

# Loading dictionary of countries dataset
country_dict = pickle.load(open("countries_dict.pkl", 'rb'))
results = pickle.load(open("Results.pkl", 'rb'))

# print(results.keys())


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
# SearchBox
selected_ct = st.selectbox('Search country', country_list)

# Country code list
code_list = make_list(country_dict, 'ioc_code ')
event_dis = make_list2(results['discipline_title'])
event_title = make_list2(results['event_title'])
medal_type = make_list2(results['medal_type'])
athletes_url = make_list2(results['athlete_url'])
athlete_name = make_list2(results['athlete_full_name'])
country_code_2 = make_list2(results['country_code'])
country_code_3 = make_list2(results['country_3_letter_code'])
country_name = make_list2(results['country_name'])

code_list1 = {}
for i in range(0, len(country_code_2)):
    code_list1[country_code_3[i]] = country_code_2[i]


country_name_code = {}
for i in range(0, len(country_list)):
    country_name_code[country_list[i].upper()] = code_list[i][1:4]

# print(country_name_code)
code_id = code_list1[country_name_code[selected_ct.upper()]]
# print(code_id)
medal_details = []

for i in range(0, len(medal_type)):
    if (medal_type[i] == 'GOLD'):
        medal_details.append(
            [country_code_2[i], event_dis[i], event_title[i], medal_type[i], athlete_name[i], athletes_url[i]])
    elif (medal_type[i] == 'SILVER'):
        medal_details.append(
            [country_code_2[i], event_dis[i], event_title[i], medal_type[i], athlete_name[i], athletes_url[i]])
    elif (medal_type[i] == 'BRONZE'):
        medal_details.append(
            [country_code_2[i], event_dis[i], event_title[i], medal_type[i], athlete_name[i], athletes_url[i]])

# print(medal_details)


# print(event_dis)

if st.button('Details'):
    tab1, tab2, tab3 = st.tabs(
        ["Medal Tally 🏅", "Medal Details 📜", "Athlete Profiles ⛹️"])

    with tab1:

        # Country gold list
        gold_list = make_list(country_dict, 'total_gold')
        # Country silver list
        silver_list = make_list(country_dict, 'total_silver')
        # Country bronze list
        broze_list = make_list(country_dict, 'total_bronze')
        # Country total medal
        total_medal = make_list(country_dict, 'total_total ')

        # Creating combine data of country
        medal_data = {}
        for i in range(0, len(country_list)):
            medal_data[country_list[i]] = [gold_list[i], int(
                silver_list[i]), int(broze_list[i]), total_medal[i], code_list[i]]

        st.header("Medal Tally 🏅")
        st.markdown(
            f'<img src="https://flagsapi.com/{code_id}/flat/64.png">', unsafe_allow_html=True)
        Details_of(selected_ct, medal_data)

    with tab2:
        st.header("Medal Details 📜")
        l1 = []
        l2 = []
        l3 = []
        for i in range(0, len(medal_details)):
            if code_id == medal_details[i][0]:
                l1.append(medal_details[i][1])
                l2.append(medal_details[i][2])
                l3.append(medal_details[i][3])

        table_data = {
            'Event Discipline': l1,
            "Event title": l2,
            "Medal": l3
        }

        df = pd.DataFrame(table_data)
        st.dataframe(df, hide_index=True)

    with tab3:
        st.header("Athlete Profiles ⛹️")
        l1 = []
        l2 = []
        l3 = []
        for i in range(0, len(medal_details)):
            if code_id == medal_details[i][0]:
                l1.append(medal_details[i][3])
                l2.append(medal_details[i][4])
                l3.append(medal_details[i][5])

        table_data = {
            'Medal': l1,
            "Athlete Name": l2,
            "Athlete Profile Id": l3
        }

        df = pd.DataFrame(table_data)
        st.dataframe(df, hide_index=True)
