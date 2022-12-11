import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for Happiness")
option_x = st.selectbox("Select the data to for x-axis", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data to for y-axis", ("GDP", "Happiness", "Generosity"))


d = pd.read_csv("happy.csv")

match option_x:
    case "Happiness":
        x_array = d["happiness"]
    case "GDP":
        x_array = d["gdp"]
    case "Generosity":
        x_array = d["generosity"]

match option_y:
    case "Happiness":
        y_array = d["happiness"]
    case "GDP":
        y_array = d["gdp"]
    case "Generosity":
        y_array = d["generosity"]


st.subheader(f"{option_x} and {option_y} Analysis")


figure = px.scatter(x=x_array, y=y_array, labels={"x": "option1", "y": "option2"})
st.plotly_chart(figure)
