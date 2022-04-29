# DS440-Transfer-Learning-Address-Sustainability-Issues

UPDATE: *Latest Version **New York Version 2** is now available in Azure SQL as `newyork_v2`.* \n
*Latest Version **Philadelphia Version 2** is now available in Azure SQL as `PhillyFeatures_V2`.* \n
*Latest Version **Chicago Version 2** is now available in Azure SQL as `ChicagoFeatures_V2`.* \n
*Latest Version **Hazleton Version 1** is now available in Azure SQL as `HazletonFeatures`.* \n
*Streamlit app source code and video of application running available in 'pages' folder*

### Datasets

*Versions*

`newyork_v2` changes - Added 1 new variable AQI weekly values as **"aqi"**

`newyork_v1` changes - Added 34 new variables listed below

    year, week, new_york_city_diesel_average_gal, new_york_city_gas_average_gal, tempmax, tempmin, temp, feelslikemax, feelslikemin, feelslike, humidity, dew, precip, precipcover, snow, snowdepth, windgust, windspeed, winddir, sealevelpressure, cloudcover, visibility, License Class, Trips Per Day, Unique Drivers, Unique Vehicles, Vehicles Per Day, Avg Days Vehicles on Road, Avg Hours Per Day Per Vehicle, Avg Days Drivers on Road, Avg Hours Per Day Per Driver, Avg Minutes Per Trip, pm25, aqi

`PhillyFeatures_V2` changes - Redid dataset layout to ensure 212 records (made each feature its own column rather than one column with feature name), took weekly average for columns if multiple values given per week, variables now as follows
    
    week, month, year, county, city, AQI_Weekly_Measurement, Weather_TMAX, Weather_TMIN, Weather_AWND, Weather_PRCP, Pollution_pm25, Pollution_o3, Pollution_no2, Pollution_so2, Pollution_co, traffic_bike_counts, traffic_ped_counts, traffic_vehicle_counts

`PhillyFeatures` changes - Added 7 variables listed below
    
    feature_year, feature_week, feature_month, feature_name, feature_lat, feature_long, feature_val

`ChicagoFeatures_V2` changes - Redid dataset layout to ensure 212 records (made each feature its own column rather than one column with feature name), took weekly average for columns if multiple values given per week, variables now as follows
    
    week, month, year, county, city, AQI_Weekly_Measurement, Weather_TMAX, Weather_TMIN, Weather_AWND, Weather_PRCP, Pollution_pm25, Pollution_o3, avg_weekday_rides, avg_saturday_rides, avg_sunday_holiday_rides, traffic_taxi_trip_miles, traffic_taxi_trip_totals, traffic_rideshare_miles, traffic_speed, traffic_bus_count

`ChicagoFeatures` changes - Added 7 variables listed below
    
    feature_year, feature_week, feature_month, feature_name, feature_lat, feature_long, feature_val
               
`HazletonFeatures` changes - Added 11 variables listed below (information on last 5 variables can be viewed at: https://docs-pennshare.hub.arcgis.com/pages/traffic-volumes)

    week, month, year, county, city, Weather_PRCP, DLY_TRK_VMT, DLY_VMT, WKDY_TRK_CUR, CUR_AADT, ADTT_CUR 

*Overview*
* **Database**: Master datasets are injected into Azure SQL database named *sustainability*.
* **Observations**: Each record is an aggregated weekly value *v* of feature *x* observed in week *w* of year *y* at latitude *lat* and longitude *long* of county *c*. 
* **Response Variable**: Target variable, *AQI* is weekly Air Quality Index (AQI). 
* **Spatial**: For NYC, we have selected Manhattan / New York county for collecting datasets. 
* **Temporal**: All datasets are between Jan 1, 2018 and Jan 1, 2022, aggregated at a minimum granularity of *weekly*.

*Number of Records*
* Number of records per feature for 4 years = 53 weeks * 4 years = 212 records
* Each dataset has *n1* features *x* with *n2* number of subfeatures *s*, so total records we expect in our dataset = 212 * n1 * n2
* We are still considering predicting particulate matter and air quality index together as (PM2.5, AQI), and the AQI range bands. 

*Scale by US Environmental Protection Agency (EPA)*

![image](https://user-images.githubusercontent.com/49132244/157559174-ec5cb151-64b4-47c5-b325-421464a5a958.png)

### Tools For Database Management
**Install Git Large File Storage (LFS)**

This is an open source Git extension for versioning large files. It will help us upload datasets to GitHub. 

<img src="https://git-lfs.github.com/images/graphic.gif" width="450" height="280">

Download and install the Git command line extension. Full instructions can be found [here.](https://git-lfs.github.com/)
```
git lfs install
```

**Exploring Microsoft Azure SQL**

Azure Data Studio is a cross-platform database tool for data professionals who use on-premises and cloud data platforms on Windows, macOS, and Linux. Use Azure Data Studio to query, design, and manage your databases and data warehouses wherever they are, on your local computer or in the cloud.

[Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database/) is an always-up-to-date relational database service built for the cloud. 

Download [Azure Data Studio](https://docs.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver15#download-azure-data-studio).

*@Vaibhav and @Ally have been added to the shared resource. I will share server link via email. Please create an Azure Account using PSU ID and accept request to join Resource Group. Navigate to `prediction` SQL Database.*

### Tools For Exploratory Data Analysis (EDA)

Use packages to automate EDA of datasets. Please read *References* to explore other available tools for data exploration.

For Primary Analysis
* (R) [DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/vignettes/dataexplorer-intro.html)
* (Python) [Pandas-Profiling](https://pypi.org/project/pandas-profiling/)

References
* (R) [4 R-Packages For Automated EDA by Towards Data Science](https://towardsdatascience.com/four-r-packages-for-automated-exploratory-data-analysis-you-might-have-missed-c38b03d4ee16#aba1)
* (Python) [4 Libraries To Perform EDA in One Line of Python Code by Towards Data Science](https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae)

### Interim Github Instructions
* Please create your individual branch for committing changes. 
* Create a [pull request to merge your commits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) onto `master`.

### Set Up Environment
* Download `Anaconda Navigator` to install essential Python and R libraries. 
* Refer to [Anaconda Navigator Cheatsheet](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf) to follow best-practices.

### Accessing AQI in R - Package
https://cran.r-project.org/web/packages/RAQSAPI/index.html
walk through -> https://github.com/USEPA/RAQSAPI

### Accessing Open Data Datasets in R
Install [RSocrata in R](https://github.com/Chicago/RSocrata) to retrieve datasets from Open Data. 

To get the current released version from CRAN:
```
install.packages("RSocrata")
```

The most recent beta with soon-to-be-released changes can be installed from GitHub:
```
# install.packages("devtools")
devtools::install_github("Chicago/RSocrata")
```
Mapping spatial data using `Leaflet` 
* Use GeoJSONs as explained [here](https://dev.socrata.com/docs/formats/geojson.html).

