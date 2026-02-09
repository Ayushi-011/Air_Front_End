import streamlit as st 
import requests 
import json
from streamlit_javascript import st_javascript

x = 'await fetch("https://api.ipify.org?format=json").then(res=>res.json())'
mob_ip = st_javascript(x).get("ip")

url = "https://air-aware-dun.vercel.app/aqi"

st.title("AIR Awareness App")
st.write("Want to know your location's AQI ???")
st.text("Let's get started by entring your location : ")
st.set_page_config(page_title = "Air Air Air",page_icon = "👽")

@st.cache_resource(ttl=900)
def ip_as_string( ip:str ):
     res = requests.get(f"{url}?ip2={mob_ip}",timeout=7)
     res.raise_for_status() #returns the error code if any kind of error occurs
     return res.json()

if st.button("Click"):
    with st.spinner("finding your AQI soon ...."):
        try:
            st.success(f"Your IP is : {mob_ip}")
            res1 = ip_as_string(mob_ip)
            loc = res1["location"]
            aqi = res1["aqi"]
            st.subheader(f"Location : {loc['city']},{loc['region']},{loc['country']}")
            st.metric(label = "Your Location's AQI : ",value = aqi['value'],delta = aqi['category'],delta_color = "inverse")
            st.map({"lat":[loc['lat']],"lon":[loc['lon']]})
            st.caption(f"src = {res1['src']}, Ip = {mob_ip}")
        
        except Exception as e:
            st.error(f"Sorry for your loss.{e}")#for host error handling 

            
