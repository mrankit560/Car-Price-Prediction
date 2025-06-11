import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("./car_price.xlsx")

st.dataframe(cars_df.head(5))