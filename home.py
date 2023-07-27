# First import the pandas to load the dataset
import pandas as pd
import streamlit as st

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

st.title('Data Visualization in Table Format')
st.write("Absolute Mean Error: ", val)
st.table(df)
