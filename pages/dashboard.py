# Import Libraries
import pandas as pd
import streamlit as st
import tensorflow as tf


# PREDICTION FUNCTION
def predict_AQI(city, week, year):

    if city == 'Chicago':
        '''
        if week == week_dict:
            result = []
            actual = []
            for i in week_dict.values():
                result_val = model.predict(data)
                result_val = result.loc[(data['week'] == i) & data['year'] == year]
                actual_val = data.loc[(data['week'] == i) & data['year'] == year]
                result.append(result_val)
                actual.append(actual_val)
            return result, actual
        '''
        data = pd.read_csv("./pages/data/chi_actual_pred.csv")
        result = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
        result = result.iloc[:,1].values
        actual = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
        actual = actual.iloc[:,6].values
        return result, actual

    if city == 'Philadelphia':
        '''
        if week == week_dict:
            result = []
            actual = []
            for i in week_dict.values():
                result_val = model.predict(data)
                result_val = result.loc[(data['week'] == i) & data['year'] == year]
                actual_val = data.loc[(data['week'] == i) & data['year'] == year]
                result.append(result_val)
                actual.append(actual_val)
            return result, actual
        '''
        data = pd.read_csv("./pages/data/phl_actual_pred.csv")
        result = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
        result = result.iloc[:, 1].values
        actual = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
        actual = actual.iloc[:, 7].values
        return result, actual
    '''
    if city == 'Hazleton':
     
            result = model_haz.predictions4
            result = result.loc[(scaled_haz_y_test['week'] == week) & scaled_haz_y_test['year'] == year]
            actual = scaled_haz_y_test.loc[(scaled_haz_y_test['week'] == week) & scaled_haz_y_test['year'] == year]
            return [result, actual]
    '''


# APPLICATION FUNCTION
def app():
    # description
    st.write("This application has been designed using transfer learning"
             " to predict the AQI values for specific cities. Initially, New York City was "
             "the source city of the model and the weights of this city were transferred to "
             "predict on similar cities of Chicago, IL, Philadelphia, PA, and Hazleton, PA. "
             "Below the user will get the chance to chose a city, week, and year and find out the "
             "AQI for the inputs. ")

    st.markdown("***This application has been developed as part of "
                "Pennsylvania State University DS440 Capstone Project.***")

    # user input variables
    city = st.selectbox("Please enter the city you would like to predict:",
                        ('Chicago', 'Philadelphia', 'Hazleton'))
    week = st.number_input("Please enter the week of the year you would like to predict:",
                           min_value=1, max_value=53)
    year = st.selectbox("Please enter the year you would like to predict:",
                        ('2018', '2019', '2020', '2021'))

    multi_week = st.checkbox("If you would like multiple weeks of data for a year, please check here")
    if multi_week:
        week_dict = {}
        num_weeks = st.number_input("Please enter how many weeks you would like:", min_value=1, max_value=53)
        for i in range(1, num_weeks):
            week_dict[i] = st.number_input("Please enter the week of the year you would like to predict:",
                                           min_value=1, max_value=53)

    if st.button('Predict'):
        if city == 'Chicago':
            '''
            if multi_week:
                result = predict_AQI(city, week_dict, year, 
                                     tf.keras.models.load_model('./models/src/modeling/build/Models/Chicago_Model_V1'))
            '''
            result = predict_AQI(city, week, year)
            d = {'lat': [41.8781], 'lon': [-87.6298]}
            df = pd.DataFrame(d)
            st.map(df)
        if city == 'Hazleton':
            '''
            if multi_week:
                result = predict_AQI(city, week_dict, year,tf.keras.models.load_model('./models/src/modeling/build/Models/Hazleton_Model_V1'))
            '''
            result = predict_AQI(city, week, year,
                                 tf.keras.models.load_model('./models/src/modeling/build/Models/Hazleton_Model_V1'))
            d = {'lat': [40.9584], 'lon': [-75.9746]}
            df = pd.DataFrame(d)
            st.map(df)
        if city == 'Philadelphia':
            '''
            if multi_week:
                result = predict_AQI(city, week_dict, year, tf.keras.models.load_model('./models/src/modeling/build/Models/Philly_Model_V1'))
            '''
            result = predict_AQI(city, week, year)
            d = {'lat': [39.9526], 'lon': [-75.1652]}
            df = pd.DataFrame(d)
            st.map(df)

        # predicted and actual aqi
        st.success('The predicted AQI: {}'.format(result[0]))  # predicted AQI for inputted row_num week and year
        st.warning('The actual AQI: {}'.format(result[1]))  # actual AQI for inputted row_num week and year

        # figure of AQI measurements / description
        st.image("./pages/images/PM2017.png")

        # feature row used in modeling
        st.header("Features used in predicting the AQI value")
        if city == 'Chicago':
            chi_data = pd.read_csv('./pages/data/Chicago-Sample.csv')
            chi_data = chi_data.iloc[:, 5:]
            st.dataframe(chi_data)
        elif city == 'Philadelphia':
            phl_data = pd.read_csv('./pages/data/Philly-Sample.csv')
            phl_data = phl_data.iloc[:, 5:]
            st.dataframe(phl_data)
        else:
            data = pd.read_csv('./pages/data/Haz-Sample.csv')
            st.dataframe(data.iloc[:,5:])

        # input visual graph created by model and RMSE
        st.header('Plot of True Values to Predicted Values')
        if city == 'Chicago':
            st.image('pages/images/chi_plot.png')
            st.metric('Normalized RMSE', 0.24682464)

        elif city == 'Philadelphia':
            st.image('pages/images/philly_plot.png')
            st.metric('Normalized RMSE', 0.20027714)

        else:
            st.image('pages/images/haz_plot.png')
            st.metric('Normalized RMSE', 0.4365)
