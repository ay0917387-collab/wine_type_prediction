# -*- coding: utf-8 -*-
"""wine_deployment.ipynb"""

#import libraries
import numpy as np
import joblib
import streamlit as st

# wine_type_prediction.pkl
model = joblib.load('wine_type_prediction.pkl')

st.set_page_config(page_title='Wine Type Prediction')
st.title('Wine Type Prediction')
st.write("Predict whether the is **Red** or **White** using chemical properties")

fixed_acidity = st.number_input("Value of fixed acidity", value=0.0)
volatile_acidity = st.number_input("Value of volatile acidity", value=0.0)
citric_acid = st.number_input("Value of citric acid", value=0.0)
residual_sugar = st.number_input("Value of residual sugar", value=0.0)
chlorides = st.number_input("Value of chlorides", value=0.0)
free_sulfur_dioxide = st.number_input("Value of free sulfur dioxide", value=0.0)
total_sulfur_dioxide = st.number_input("Value of total sulfur dioxide", value=0.0)
density = st.number_input("Value of density", value=0.0)
pH = st.number_input("Value of pH", value=0.0)
sulphates = st.number_input("Value of sulphates", value=0.0)
alcohol = st.number_input("Value of alcohol", value=0.0)
quality = st.number_input("Value of quality", value=0.0)

if st.button('Predict'):
    input_data = np.array([[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol,
        quality
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success(" ** White Wine **")
    else:
        st.success(" ** Red Wine **")
