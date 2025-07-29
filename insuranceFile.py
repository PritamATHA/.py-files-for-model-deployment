import pickle
import streamlit as st

model = pickle.load(open("insuranceFile.pkl", "rb"))

def mydeploy():
    st.title("Insurance Cost Prediction")

    age = st.number_input("Enter your age: ", min_value=0)

    pred = st.button("Predict")

    if pred:
        x = model.predict([[age]])
        st.write("Predicted insurance cost is:", round(x[0], 2))

mydeploy()
