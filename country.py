import streamlit as st
import pickle 
import pandas as pd

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

# print(medal_data)

# print(medal_data['India'][4][1:3])

#Title of page
st.title("Countries")

#SearchBox
selected_ct = st.selectbox('Search country', country_list)

if st.button('Details'):
	st.markdown(f'<img src="https://flagsapi.com/{medal_data[selected_ct][4][1:3]}/flat/64.png">', unsafe_allow_html = True)
	Details_of(selected_ct, medal_data)

