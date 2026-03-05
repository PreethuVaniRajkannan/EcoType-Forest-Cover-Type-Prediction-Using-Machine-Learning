import pickle
import streamlit as st
import pandas as pd

#model loading
with open("rf_cover_type.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌲 Forest Cover Type Prediction")
st.write("Enter feature values below:")

Elevation = st.number_input("Elevation")
Aspect = st.number_input("Aspect")
Slope = st.number_input("Slope")
Horizontal_Distance_To_Hydrology = st.number_input("Horizontal Distance To Hydrology")
Vertical_Distance_To_Hydrology = st.number_input("Vertical Distance To Hydrology")
Horizontal_Distance_To_Roadways = st.number_input("Horizontal Distance To Roadways")
Hillshade_9am = st.number_input("Hillshade 9am")
Hillshade_Noon = st.number_input("Hillshade Noon")
Hillshade_3pm = st.number_input("Hillshade 3pm")
Horizontal_Distance_To_Fire_Points = st.number_input("Horizontal Distance To Fire Points")
Wilderness_Area = st.number_input("Wilderness Area (0-3)")
Soil_Type = st.number_input("Soil Type (0-39)")

if st.button("Predict"):

    input_data = pd.DataFrame([[ 
        Elevation,
        Aspect,
        Slope,
        Horizontal_Distance_To_Hydrology,
        Vertical_Distance_To_Hydrology,
        Horizontal_Distance_To_Roadways,
        Hillshade_9am,
        Hillshade_Noon,
        Hillshade_3pm,
        Horizontal_Distance_To_Fire_Points,
        Wilderness_Area,
        Soil_Type
        
    ]],
    columns=[
        "Elevation",
        "Aspect",
        "Slope",
        "Horizontal_Distance_To_Hydrology",
        "Vertical_Distance_To_Hydrology",
        "Horizontal_Distance_To_Roadways",
        "Hillshade_9am",
        "Hillshade_Noon",
        "Hillshade_3pm",
        "Horizontal_Distance_To_Fire_Points",
        "Wilderness_Area",
        "Soil_Type"
    ])

    prediction = model.predict(input_data)

    st.success(f"Predicted Cover Type: {prediction[0]}")