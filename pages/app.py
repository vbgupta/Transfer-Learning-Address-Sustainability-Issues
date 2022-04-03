**THE FOLLOWING CODE HAS BEEN MODIFIED AND FOUND ON https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030**

import streamlit as st

# Custom imports
from multipage import MultiPage
import dashboard

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Prediction of Air Quality Index (AQI)")

# Add all your applications (pages) here
app.add_page("Dashboard", dashboard.app)

# The main app
app.run()
