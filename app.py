import streamlit as st
import pickle
import pandas as pd

# importing the module to split the data
from sklearn.model_selection import train_test_split

# importing models
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Dataset path is saved in the variable
file_path = "olympics_medals_country_wise.csv"

# Dataset is stored in data variable
data = pd.read_csv(file_path)

# function to convert string data into integer


def convert_data(data, feature):
    l = []
    for i in data[feature]:
        if ',' in str(i):
            val = 0
            for j in i:
                if j != ',':
                    val *= 10
                    val += int(j)
            l.append(val)
        else:
            l.append(int(i))

    # updating the data:
    data[feature] = l


# Converting string data into int
convert_data(data, 'total_total ')
convert_data(data, 'total_gold')
convert_data(data, 'total_silver')
convert_data(data, 'total_bronze')
convert_data(data, 'winter_participations')


# Creating a simple model
y = data['total_total ']

# Printing columns information to select features:
# print(data.columns)

# features used for predictions
features = ['winter_participations',
            'total_gold', 'total_silver', 'total_bronze']

X = data[features]


# split data into training and validation data:
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)


# Using a randomforest model
forest_model = RandomForestRegressor(random_state=1)

# Fitting the model
forest_model.fit(train_X, train_y)

# Predicting output
prediction = forest_model.predict(val_X).round()

val = mean_absolute_error(val_y, prediction)

new_pre = []
for i in prediction:
    new_pre.append(int(i))
# print(new_pre)


l1 = []
for i in val_y:
    l1.append(i)
l2 = []
for i in new_pre:
    l2.append(i)

table_data = {
    'Actual Values': l1,
    'Predicted Values': l2
}

df = pd.DataFrame(table_data)

# Function to display the home page


def home_page():
    st.title("Home Page")
    st.write("Absolute Mean Error: ", val)
    st.table(df)


# Function to display the games page


def games_page():
    st.title("Games Page")
    st.write("This is the games page. You can list different games here.")

# Function to display the country page


def country_page():
    # To extract country name
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

    # Loading dictionary of countries dataset
    country_dict = pickle.load(open('countries_dict.pkl', 'rb'))

    # print(country_dict.keys())

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

    # Creating combine data of country
    medal_data = {}
    for i in range(0, len(country_list)):
        medal_data[country_list[i]] = [gold_list[i], int(
            silver_list[i]), int(broze_list[i]), total_medal[i], code_list[i]]

    # Title of page
    st.title("Countries")

    # SearchBox
    selected_ct = st.selectbox('Search country', country_list)

    if st.button('Details'):
        st.markdown(
            f'<img src="https://flagsapi.com/{medal_data[selected_ct][4][1:3]}/flat/64.png">', unsafe_allow_html=True)
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
