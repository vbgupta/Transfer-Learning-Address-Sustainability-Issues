############################################################################################################
  #THE FOLLOWING CODE HAS BEEN MODIFIED AND FOUND ON https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030
###################################################################################################
  #To run the following code and deploy streamlit application type "streamlit run ./pages/app.py" in terminal
##########################################################################################################


import streamlit as st

# Custom imports
from multipage import MultiPage
import dashboard, philly_info, chi_info

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Prediction of Air Quality Index (AQI)")

# Add all your applications (pages) here
app.add_page("Dashboard", dashboard.app)
app.add_page("Philadelphia Info", philly_info.app)
app.add_page("Chicago Info", chi_info.app)

# The main app
app.run()
