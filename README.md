# Air_Front_End
A frontend application that consumes the AirAware backend APIs to display air quality information in a user-friendly interface. The frontend is implemented using Streamlit. 
**Air Aware (Front End)** is a Streamlit-based user interface that visualizes real-time **air quality and weather information** fetched from the backend services. The app focuses on simplicity, responsiveness, and fast data access.

---

##  Features
- Interactive Streamlit UI  
- Displays current weather and air quality data  
- Optimized performance using caching  
- Deployed for direct browser access  

---

##  Run the App (Using Hosted Link)

1. Open the **deployed Streamlit app link** provided in the repository description. Using the link : https://find-your-aqi.streamlit.app/
2. View real-time air quality and weather details directly in your browser.

 No local setup or installation required.

---

##  Design Choices

###  Caching Strategy
- Frequently accessed data is cached to minimize repeated API calls  
- Improves load time and reduces server/API overhead  
- Ensures a smoother user experience  

###  Timeout Handling
- API requests use predefined timeouts  
- Prevents the UI from hanging during slow or failed network calls  
- Enhances reliability and responsiveness of the app  

---

##  Tech Stack
- **Python**
- **Streamlit**

---

##  Future Improvements
- Enhanced UI styling
- User-selectable locations
- Historical air quality visualization

---

