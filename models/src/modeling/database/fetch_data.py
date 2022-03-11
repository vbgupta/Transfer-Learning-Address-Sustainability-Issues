import pandas as pd
import pyodbc
import keys
from keys import username, password, server, driver, database
import os


conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

# AQI Chicago
rows1 = conn.cursor().execute("SELECT County, AQI_Weekly_Measurement, AQI_week, AQI_month, AQI_year, AQI_lat, AQI_long, City FROM dbo.Chicago_AQI").fetchall() 

# Features Chicago
rows2 = conn.cursor().execute("SELECT feature_week, feature_month, feature_year, feature_lat, feature_long, feature_name, feature_val FROM dbo.ChicagoFeatures").fetchall() 

#Convert to df AQI
dfAQI = pd.DataFrame([tuple(t) for t in rows1], columns=['County', 'AQI_Weekly_Measurement', 'AQI_week', 'AQI_month', 'AQI_year', 'AQI_lat', 'AQI_long', 'City']) 

#Convert to df features
dfFeatures = pd.DataFrame([tuple(t) for t in rows2], columns=['feature_week', 'feature_month', 'feature_year', 'feature_lat', 'feature_long', 'feature_name', 'feature_val'])
dfFeatures['AQI_week'] = dfFeatures['feature_week']
dfFeatures['AQI_month'] = dfFeatures['feature_month']
dfFeatures['AQI_year'] = dfFeatures['feature_year']

data_dir = './data/'
dfAQI.to_csv(data_dir + 'ChicagoAQI.csv', index = False)
dfFeatures.to_csv(data_dir + 'ChicagoFeatures.csv', index = False)



