import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next 5 days")
place = st.text_input("place: ")
days = st.slider(label='Forecast Days', max_value=5, min_value=1, help="select the number of days")
option = st.selectbox("Select date to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in '{place}'")

if place:

    try:

        filtered_data = get_data(place, days)
        if option == "Temperature":
            temp = [i["main"]["temp"] / 10 for i in filtered_data]
            dates = [k["dt_txt"] for k in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images2/clear.png", "Clouds": "images2/cloud.png", "Rain": "images2/rain.png",
                      "Snow": "images2/snow.png"}
            sky_cond = [j["weather"][0]["main"] for j in filtered_data]
            image_path = [images[condition] for condition in sky_cond]
            st.image(image_path, width=113)

    except KeyError:
        st.write("Enter a correct city name")
