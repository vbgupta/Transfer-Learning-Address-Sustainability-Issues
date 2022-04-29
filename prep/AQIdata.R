#load libraries
library("jsonlite")

#########################
# Philadelphia AQI
##########################

#philly 2018 aqi 
result <- fromJSON("./Philly/Data/PhillyAQI2018.json")
phillyAQI2018 <- as.data.frame(result)

#philly 2019 aqi 
result <- fromJSON("./Philly/Data/PhillyAQI2019.json")
phillyAQI2019 <- as.data.frame(result)

#philly 2021 aqi
result <- fromJSON("./Philly/Data/PhillyAQI2020.json")
phillyAQI2020 <- as.data.frame(result)

#philly 2020 aqi
result <- fromJSON("./Philly/Data/PhilllyAQI2021.json")
phillyAQI2021 <- as.data.frame(result)

#combine all years to one dataset
df_list <- list(phillyAQI2018, phillyAQI2019, phillyAQI2020, phillyAQI2021)
PhillyAQI <- Reduce(function(x,y)merge(x,y,all = TRUE), df_list, accumulate = FALSE)
write.csv(PhillyAQI, "./Philly/Data/PhillyAQI.csv")


#########################
# Chicago AQI
##########################
#chicago 2018 aqi
result <- fromJSON("./Chicago/Data/ChicagoAQI2018.json")
chicagoAQI2018 <- as.data.frame(result)

#chicago 2019 aqi
result <- fromJSON("./Chicago/Data/ChicagoAQI2019.json")
chicagoAQI2019 <- as.data.frame(result)

#chicago 2020 aqi
result <- fromJSON("./Chicago/Data/ChicagoAQI2020.json")
chicagoAQI2020 <- as.data.frame(result)

#chicago 2021 aqi
result <- fromJSON("./Chicago/Data/ChicagoAQI2021.json")
chicagoAQI2021 <- as.data.frame(result)

#combine all years to one dataset
df_list <- list(chicagoAQI2018, chicagoAQI2019, chicagoAQI2020, chicagoAQI2021)
ChicagoAQI <- Reduce(function(x,y)merge(x,y,all = TRUE), df_list, accumulate = FALSE)
write.csv(ChicagoAQI, "./Chicago/Data/ChicagoAQI.csv")
