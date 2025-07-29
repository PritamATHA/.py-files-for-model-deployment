import pickle
import streamlit as st

model = pickle.load(open("MultiFileN.pkl", "rb"))

def mydeploy():
    st.title("House Price Prediction (Multiple Features)")

    area = st.number_input("Enter area (sq ft):", min_value=0)
    bedrooms = st.number_input("Enter number of bedrooms:", min_value=0)
    age = st.number_input("Enter age of the property (years):", min_value=0)

    pred = st.button("Predict")

    if pred:
        prediction = model.predict([[area, bedrooms, age]])
        st.write("Predicted house price is:", round(prediction[0], 2))

mydeploy()
