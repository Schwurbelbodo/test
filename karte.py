import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium


st.set_page_config(layout="wide")

"## Test"

m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
Draw(export=True).add_to(m)
output = st_folium(m, width=700, height=500)
    
