import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("./car_price.csv")

st.write('''
    # Cars24 used for Car prediction        
 ''')

st.dataframe(cars_df.head(5))

col1, col2 = st.columns(2)

fuel_type = col1.selectbox(
    "Select the fule type",
    ("Diesel", "Petrol", "CNG", "Electric"))

engine = col1.slider("Set the engine size", 500, 5000, step=100)

transmission_type = col2.selectbox(
    "Select the transmission type",
    ("Manual", "Automatic"))
seats = col2.selectbox(
    "Enter the number of seats",
    (4,5,7,9,11))


# input_features = [[2018, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
encode_dict = {
    'fuel_type': { "Diesel" : 1, "Petrol" : 2, "CNG": 3, "LPG" : 4, "Electric" : 5},
    "seller_type" : {"Dealer" : 1, "Individual" : 2, "Trustmark Dealer" : 3},
    "transmission_type" : {"Manual" : 1, "Automatic" : 2} 
            }

def model_pred(fuel_type, transmission_type, engine, seats):

    #load the model pickle
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
        input_features = [[2018, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
        return reg_model.predict(input_features)

if st.button("Predict Price"):

    fuel_type = encode_dict["fuel_type"][fuel_type]
    transmission_type = encode_dict["transmission_type"][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)

    st.text(f"The price of the car is {price[0].round(2)} lakhs") #price variable return in list format, so use price[0]