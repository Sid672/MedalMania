import streamlit as st
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import requests
import numpy as np

st.set_page_config(page_title="Home", page_icon="🏠")

# Dataset path is saved in the variable
file_path = "olympics_medals_country_wise.csv"

# Dataset is stored in data variable
data = pd.read_csv(file_path)

def make_list(data, feature):
    l = []
    for i in range(0, len(data[feature])):
        l.append(data[feature].iloc[i])
    return l

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
convert_data(data, 'summer_participations')
convert_data(data, 'total_participation')

# Creating a simple model
y = data['total_total ']

# features used for predictions
features = ['summer_participations', 'total_participation', 'total_gold', 'total_silver', 'total_bronze']

X = data[features]
# split data into training and validation data:
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=515)
# Using a randomforest model
forest_model = RandomForestRegressor(random_state=42,max_features=None)

# Fitting the model
forest_model.fit(train_X, train_y)

# Predicting output
prediction = forest_model.predict(val_X).round()
val = mean_absolute_error(val_y, prediction)
new_pre = []
for i in prediction:
    new_pre.append(int(i))
# print(new_pre)

l = val_y
# print(val_y)
id_list = [57, 143, 155, 36, 9, 15, 22, 116, 58, 27, 99, 56, 64, 136, 134, 104, 7, 8, 145, 30, 133, 150, 50, 31, 90, 123, 5, 114, 69, 41, 63, 132, 79, 65, 6, 18, 119, 38, 117]
# print(id_list)

map_code_list = []
map_country_name = []
for i in id_list:
    map_country_name.append(data['countries '].iloc[i])
    map_code_list.append(data['ioc_code '].iloc[i])

countries = map_country_name

l1 = []
for i in val_y:
    l1.append(i)
l2 = []
for i in new_pre:
    l2.append(i)

table_data = {
    'Country': map_country_name,
    'Actual values of total medals': l1,
    'Predicted values of total medals': l2
}
df1 = pd.DataFrame(table_data)

def main():
    st.title("Medal Mania")
    st.write("The model accurately predicts medals for various countries in the Olympics. Its performance is evaluated using the absolute mean error, which measures the average difference between the predicted and actual medal counts. For the validation dataset, the absolute mean error achieved is 1.69.")
    st.write("Absolute Mean Error: ", val)
    st.dataframe(df1, hide_index=True)

if __name__ == "__main__":
    main()
