
# Import Libraries
import csv

import pandas as pd
import streamlit as st
import tensorflow as tf

def app():
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

    def predict_AQI(city, week, year):
        pass
    '''
         if city == 'Chicago':
            result = model_chi.predictions4
            result = result.loc[(scaled_chicago_y_test['week'] == week) & scaled_chicago_y_test['year'] == year]
            actual = scaled_chicago_y_test.loc[(scaled_chicago_y_test['week'] == week) & scaled_chicago_y_test['year'] == year]
            
        elif city == 'Philadelphia':
            result = model_phl.predictions4
            result = result.loc[(scaled_philly_y_test['week'] == week) & scaled_philly_y_test['year'] == year]
            actual = scaled_philly_y_test.loc[(scaled_philly_y_test['week'] == week) & scaled_philly_y_test['year'] == year]
            
        else:
            result = model_haz.predictions4
            result = result.loc[(scaled_haz_y_test['week'] == week) & scaled_haz_y_test['year'] == year]
            actual = scaled_haz_y_test.loc[(scaled_haz_y_test['week'] == week) & scaled_haz_y_test['year'] == year]
        return [result, actual]
        '''

    # description
    st.write("This application has been designed using transfer learning"
             " to predict the AQI values for specific cities. Initially, New York City was the source city of the model "
             "and the weights of this city were transferred to predict on similar cities of"
             " Chicago, IL, Philadelphia, PA, and Hazleton, PA. Below the user will get the chance to chose a city, "
             "week, and year and find out the AQI for the inputs. ")
    st.markdown("***This application has been developed as part of Pennsylvania State University DS440 Capstone Project.***")

    # user input variables
    city = st.selectbox("Please enter the city you would like to predict:",
                        ('Chicago', 'Philadelphia', 'Hazleton'))
    week = st.number_input("Please enter the week of the year you would like to predict:",
                           min_value=1, max_value=53)
    year = st.selectbox("Please enter the year you would like to predict:",
                        ('2018', '2019', '2020', '2021'))

    if st.button('Predict'):
        if city == 'Chicago':
            result = predict_AQI(city, week, year)
            d = {'lat': [41.8781], 'lon': [-87.6298]}
            df = pd.DataFrame(d)
            st.map(df)
        if city == 'Hazleton':
            result = predict_AQI(city, week, year)
            d = {'lat': [40.9584], 'lon': [-75.9746]}
            df = pd.DataFrame(d)
            st.map(df)
        if city == 'Philadelphia':
            result = predict_AQI(city, week, year)
            d = {'lat': [39.9526], 'lon': [-75.1652]}
            df = pd.DataFrame(d)
            st.map(df)
        # change result to [0] and[1]
        st.success('The predicted AQI is {}'.format(result))  # predicted AQI for inputted row_num week and year
        st.warning('The actual AQI is {}'. format(result)) # actual AQI for inputted row_num week and year

        # feature row
        st.header("Features used in predicting the AQI value")


        # input visual graph created by model and RMSE
        st.header('Plot of True Values to Predicted Values')
        if city == 'Chicago':
            st.image('./Chi_plot.png')
            st.header('Overall RMSE of Chicago model: ')
        elif city == 'Philadelphia':
             st.header('Overall RMSE of Philadelphia model:')
        else:
            st.header('Overall RMSE of Hazleton model: {}'.format('0.77534'))


    # add in row of features
    # add page with visualizations/stats