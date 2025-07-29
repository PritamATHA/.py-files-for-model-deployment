import pickle
import streamlit as st

model = pickle.load(open("irisFile.pkl", "rb"))

def mydeploy():
    st.title("Iris Flower Species Prediction")

    sepal_length = st.number_input("Enter sepal length (cm):", min_value=0.0)
    sepal_width = st.number_input("Enter sepal width (cm):", min_value=0.0)
    petal_length = st.number_input("Enter petal length (cm):", min_value=0.0)
    petal_width = st.number_input("Enter petal width (cm):", min_value=0.0)

    pred = st.button("Predict")

    if pred:
        x = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        st.write("Predicted Iris species is:", x[0])

mydeploy()
