import streamlit as st
#from streamlit_elements import elements, mui, html

#import pandas as pd
from datetime import datetime

###################################################

st.title("Massband-App - Wie lange noch? :sunglasses:")

datum_start = datetime(2023, 11, 11)
datum_heute = datetime.today()
datum_ende = datetime(2023, 12, 15)

tag_delta_1 = datum_ende - datum_start
tag_delta_2 = tag_delta_1 - (datum_ende - datum_heute) + 1
tag_delta_3 = datum_ende - datum_heute

col1, col2 = st.columns(2)


col21, col22, col23 = st.columns(3)
with col21:
    st.markdown("*Heutiges Datum*")
    st.write(datum_heute.strftime("%d.%m.%Y"))

with col21:
    st.empty()

with col22:
    st.metric("Tage verbleibend", 
          tag_delta_3.days,
    )

with col23:
    st.markdown("*Enddatum*")
    st.write(datum_ende.strftime("%d.%m.%Y"))

st.progress(
    tag_delta_2.days/tag_delta_1.days,
    text="Schon rum..."
    )
