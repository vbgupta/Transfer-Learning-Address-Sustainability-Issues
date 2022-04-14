# Import Libraries
import statistics
import pandas as pd
import streamlit as st


# PREDICTION FUNCTION
def predict_AQI(city, week, year, multi_week, month):
    if city == 'Chicago':
        data = pd.read_csv("pages/data/chi_actual_pred.csv")
        if multi_week:
            result = []
            actual = []
            for i in week.values():
                result_val = pd.DataFrame(data[(data["week"] == (i)) & (data["year"] == int(year))])
                result_val = result_val.iloc[:, 1].values
                actual_val = pd.DataFrame(data[(data["week"] == (i)) & (data["year"] == int(year))])
                actual_val = actual_val.iloc[:, 6].values
                result.append(result_val)
                actual.append(actual_val)
            return result, actual

        elif month != '0':
            result = pd.DataFrame(data[(data["month"] == int(month)) & (data["year"] == int(year))])
            result = statistics.mean(result.iloc[:, 1].values)
            actual = pd.DataFrame(data[(data["month"] == int(month)) & (data["year"] == int(year))])
            actual = statistics.mean(actual.iloc[:, 6].values)
            return result, actual

        else:
            result = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
            result = result.iloc[:, 1].values
            actual = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
            actual = actual.iloc[:, 6].values
            return result, actual

    if city == 'Philadelphia':
        data = pd.read_csv("pages/data/phl_actual_pred.csv")
        if multi_week:
            result = []
            actual = []
            for i in week.values():
                result_val = pd.DataFrame(data[(data["week"] == (i)) & (data["year"] == int(year))])
                result_val = result_val.iloc[:, 1].values
                actual_val = pd.DataFrame(data[(data["week"] == (i)) & (data["year"] == int(year))])
                actual_val = actual_val.iloc[:, 7].values
                result.append(result_val)
                actual.append(actual_val)
            return result, actual

        elif month != '0':
            result = pd.DataFrame(data[(data["month"] == int(month)) & (data["year"] == int(year))])
            result = statistics.mean(result.iloc[:, 1].values)
            actual = pd.DataFrame(data[(data["month"] == int(month)) & (data["year"] == int(year))])
            actual = statistics.mean(actual.iloc[:, 7].values)
            return result, actual

        else:
            result = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
            result = result.iloc[:, 1].values
            actual = pd.DataFrame(data[(data["week"] == int(week)) & (data["year"] == int(year))])
            actual = actual.iloc[:, 7].values
            return result, actual



# APPLICATION FUNCTION
def app():
    # description
    st.write("This application has been designed using transfer learning"
             " to predict the AQI values for specific cities. New York City is "
             "the source city of the model and the weights of this city were transferred to "
             "similar cities of Chicago, IL and Philadelphia, PA to predict the AQI. "
             "Below the user will get the chance to chose a city, week, and year and find out the "
             "AQI for the inputs. ")

    st.markdown("***This application has been developed as part of "
                "Pennsylvania State University DS440 Capstone Project.***")

    # user input variables
    city = st.selectbox("Please enter the city you would like to predict:",
                        ('Chicago', 'Philadelphia'))
    week = st.number_input("Please enter the week of the year you would like to predict:",
                           min_value=1, max_value=53)
    year = st.selectbox("Please enter the year you would like to predict:",
                        ('2018', '2019', '2020', '2021'))

    funct = st.selectbox("If you would rather choose multiple weeks of information or a monthly "
                     "average for a given year, please select one of the following, else keep blank",
                     ('-', 'Multiple weeks for given year', 'Average AQI for given month and year'))

    if funct == 'Multiple weeks for given year':
        week_dict = {}
        num_weeks = st.number_input("Please enter how many weeks you would like:", min_value=1, max_value=53)
        count = int(num_weeks)
        while count != 0:
            week_dict[count] = ""
            count -= 1
        for count,value in week_dict.items():
            week_dict[count] = int(st.number_input("Please enter the week of the year you"
                                                " would like to predict:",min_value=1, max_value=53, key=count))

    if funct == 'Average AQI for given month and year':
        month = st.selectbox("Please enter the month you would like to predict:", ('1', '2', '3', '4', '5', '6',
                                                                                                            '7', '8',
                                                                                   '9', '10', '11', '12'))

    if st.button('Predict'):
        if city == 'Chicago':
            if funct == 'Multiple weeks for given year':
                result = predict_AQI(city, week_dict, year, True, '0')
                d = {'lat': [41.965193], 'lon': [-87.876265]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinate the AQI was measured at")
                st.map(df)
            elif funct == 'Average AQI for given month and year':
                result = predict_AQI(city, week, year, False, month)
                d = {'lat': [41.965193], 'lon': [-87.876265]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinates the AQI was measured at")
                st.map(df)
            else:
                result = predict_AQI(city, week, year, False, '0')
                d = {'lat': [41.965193], 'lon': [-87.876265]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinate the AQI was measured at")
                st.map(df)

        if city == 'Philadelphia':
            if funct == 'Multiple weeks for given year':
                result = predict_AQI(city, week_dict, year, True, '0')
                d = {'lat': [39.988842], 'lon': [-75.207205]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinate the AQI was measured at")
                st.map(df)
            elif funct == 'Average AQI for given month and year':
                result = predict_AQI(city, week, year, False, month)
                d = {'lat': [39.988842], 'lon': [-75.207205]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinate the AQI was measured at")
                st.map(df)
            else:
                result = predict_AQI(city, week, year, False, '0')
                d = {'lat': [39.988842], 'lon': [-75.207205]}
                df = pd.DataFrame(d)
                st.write("Below is the coordinate the AQI was measured at")
                st.map(df)

        # predicted and actual aqi
        st.success('**The predicted AQI: {}**'.format(result[0]))  # predicted AQI for inputted row_num week and year
        st.success('**The actual AQI: {}**'.format(result[1]))  # actual AQI for inputted row_num week and year

        # figure of AQI measurements / description
        st.image("./pages/images/PM2017.png")

        # input visual graph created by model and RMSE
        st.header('Plot of True Values to Predicted Values')
        if city == 'Chicago':
            st.image('pages/images/chi_plot.png')
            st.metric('Normalized RMSE', 0.24682464)
            st.write("Normalized RMSE is measuring the standard deviation of the residuals (prediction errors)."
                     " In general, a RMSE between 0.2 - 0.5 indicates the model relatively predicts accurately.")

        else:
            st.image('pages/images/philly_plot.png')
            st.metric('Normalized RMSE', 0.20027714)
            st.write("Normalized RMSE is measuring the standard deviation of the residuals (prediction errors)."
                     " In general, a RMSE between 0.2 - 0.5 indicates the model relatively predicts accurately.")

        # feature row used in modeling
        st.header("Features used in predicting the AQI value")
        if city == 'Chicago':
            chi_data = pd.read_csv('pages/data/Chicago-Sample.csv')
            chi_data = chi_data.iloc[:, 5:]
            st.dataframe(chi_data)
        else:
            phl_data = pd.read_csv('pages/data/Philly-Sample.csv')
            phl_data = phl_data.iloc[:, 5:]
            st.dataframe(phl_data)
