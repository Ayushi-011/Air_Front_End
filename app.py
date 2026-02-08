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




if st.button("Click"):
    with st.spinner("finding your AQI soon ...."):
        try:
            st.success(f"Your IP is : {mob_ip}")
            res = requests.get(f"{url}?ip2={mob_ip}")
            res1 = res.json()
            if res.status_code == 200:
                loc = res1["location"]
                aqi = res1["aqi"]
                st.subheader(f"Location : {loc['city']},{loc['region']},{loc['country']}")
                st.metric(label = "Your Location's AQI : ",value = aqi['value'],delta = aqi['category'],delta_color = "inverse")
                st.map({"lat":[loc['lat']],"lon":[loc['lon']]})
                st.caption(f"src = {res1['src']}, Ip = {mob_ip}")
            else:
                st.error("Page Not Found.")#for backend error handling
        except Exception as e:
            st.error(f"Sorry for your loss.{e}")#for host error handling 
            