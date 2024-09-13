import streamlit as st
from nasaapi import img_of_the_day


title,explanation,date =img_of_the_day()
st.title(title)
st.write(date)
st.image('img.jpeg')
st.write(explanation)
