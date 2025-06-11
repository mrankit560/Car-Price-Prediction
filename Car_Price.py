import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("./car_price.csv")

st.write('''
    # Cars24 used for Car prediction        
 ''')

st.dataframe(cars_df)

col1, col2 = st.columns(2)

year = col2.slider(
    "Select the Year",
    1991, 2021, value=2015, step=1)

seller_type = col1.selectbox(
    "Select the Seller Type",
    ("Dealer", "Individual", "Trustmark Dealer"))

km_driven = col2.slider(
    "Select the KM driven",
    10000, 3800000, step=5000)

fuel_type = col1.selectbox(
    "Select the fuel type",
    ("Diesel", "Petrol", "CNG", "Electric"))


transmission_type = col1.selectbox(
    "Select the transmission type",
    ("Manual", "Automatic"))

mileage = col2.slider(
    "Select the Mileage",
    5, 120, value = 70,  step=1)

engine = col1.slider("Set the engine size", 500, 5000, value = 1800, step=100)

max_power = col2.slider(
    "Select the Maximum Power",
    5, 626,value =100, step=5)

seats = col1.selectbox(
    "Enter the number of seats",
    (4,5,7,9,11))


# input_features = [[2018, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
encode_dict = {
    'fuel_type': { "Diesel" : 1, "Petrol" : 2, "CNG": 3, "LPG" : 4, "Electric" : 5},
    "seller_type" : {"Dealer" : 1, "Individual" : 2, "Trustmark Dealer" : 3},
    "transmission_type" : {"Manual" : 1, "Automatic" : 2} 
            }

def model_pred(year,seller_type, km_driven, fuel_type,\
                transmission_type, mileage, engine, max_power, seats):

    #load the model pickle
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
        input_features = [[year,seller_type, km_driven, fuel_type,\
                transmission_type, mileage, engine, max_power, seats]]
        return reg_model.predict(input_features)

if st.button("Predict Price"):

    fuel_type = encode_dict["fuel_type"][fuel_type]
    transmission_type = encode_dict["transmission_type"][transmission_type]
    seller_type = encode_dict["seller_type"][seller_type]

    price = model_pred(year,seller_type, km_driven, fuel_type,\
                transmission_type, mileage, engine, max_power, seats)

    st.text(f"The price of the car is {price[0].round(2)} lakhs") #price variable return in list format, so use price[0]
