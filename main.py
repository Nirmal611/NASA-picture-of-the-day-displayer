import streamlit as st
from nasaapi import img_of_the_day
import datetime

max_date = datetime.datetime.now()
min_date = datetime.date(2023,1,1)
st.title('NASA astronomy image of the day '.title())
date = st.date_input('Select a day', key='date', value=None, format='YYYY-MM-DD', max_value=max_date, min_value=min_date)
print(date)
if date :
    title, explanation = img_of_the_day(date)
    st.subheader(title)
    st.write(date)
    st.image('img.jpeg')
    st.write("\t"+explanation)
