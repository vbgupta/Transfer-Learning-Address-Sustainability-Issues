

####### TO RUN IN TERMINAL: streamlit run app_v2.py #######

# Import Libraries
import csv

import pandas as pd
import streamlit as st
import tensorflow as tf

# load models
'''
@st.cache(allow_output_mutation=True)
def load_model_chi():
    model_chi = tf.keras.models.load_model('./models/src/modeling/build/Models/Model_5')
    return model_chi

@st.cache(allow_output_mutation=True)
def load_model_phl():
    model_phl = tf.keras.models.load_model('./models/src/modeling/build/Models/Model_6')
    return model_phl

@st.cache(allow_output_mutation=True)
def load_model_haz():
    model_haz = tf.keras.models.load_model('./models/src/modeling/build/Models/Model_7')
    return model_haz

'''

def predict_AQI(city, ran_num):
    pass
'''
    if city == 'Chicago':
        result = model_chi.predictions4[ran_num]
        actual = scaled_chicago_y_test[ran_num]
    elif city == 'Philadelphia':
        result = model_phl.predictions4[ran_num]
        actual = scaled_chicago_y_test[ran_num]
    else:
        result = model_haz.predictions4[ran_num]
        actual = scaled_chicago_y_test[ran_num]
    return [result, actual]
    '''

# title output
st.title("Prediction of Air Quality Index (AQI)")

# user input variables
city = st.selectbox("Please enter the city you would like to predict:",
                    ('Chicago', 'Philadelphia', 'Hazleton'))
row_num = st.number_input("Please enter a number:", min_value=1, max_value=212)  # row of data to predict
st.caption("This number will be used in predicting the AQI for the week of a year between 2018-2021")

if st.button('Predict'):
    if city == 'Chicago':
        result = predict_AQI(city, row_num)
        d = {'lat': [41.8781], 'lon': [-87.6298]}
        df = pd.DataFrame(d)
        st.map(df)
    if city == 'Hazleton':
        result = predict_AQI(city, row_num)
        d = {'lat': [40.9584], 'lon': [-75.9746]}
        df = pd.DataFrame(d)
        st.map(df)
    if city == 'Philadelphia':
        result = predict_AQI(city, row_num)
        d = {'lat': [39.9526], 'lon': [-75.1652]}
        df = pd.DataFrame(d)
        st.map(df)
    # change result to [0] and[1]
    st.success('The predicted AQI is {}'.format(result))  # predicted AQI for inputted row_num week and year
    st.warning('The actual AQI is {}'. format(result)) # actual AQI for inputted row_num week and year

    # input visual graph created by model and RMSE
    st.header('Plot of True Values to Predicted Values')
    if city == 'Chicago':
        st.image('./plot_images/Chi_plot.png')
        st.header('Overall RMSE of Chicago model: ')
    elif city == 'Philadelphia':
        st.image('./plot_images/Chi_plot.png')
        st.header('Overall RMSE of Philadelphia model: {}'.format('0.77534'))
    else:
        st.image('./plot_images/Chi_plot.png')
        st.header('Overall RMSE of Hazleton model: {}'.format('0.77534'))
