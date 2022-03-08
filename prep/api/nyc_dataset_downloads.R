# Load Libraries
library(RSocrata)
library(aqsr)
library(usethis)
library(devtools)
library(data.table)
library(tidyverse)
library(DataExplorer)
library(filenamer)
library(validate)
library(request)

### To use New York's Air Quality System (AQS), we set up a user account.
# Store API user emails, tokens, passwords
soc_token <- Sys.getenv("SOCRATA_TOKEN")
soc_email <- Sys.getenv("SOCRATA_EMAIL")

soc_pass <- Sys.getenv("SOCRATA_PASSWORD")
aqs_key <- Sys.getenv("AQS_KEY")
aqs_email <- Sys.getenv("AQS_EMAIL")

# Create Users
aqs_user <- create_user(email=aqs_email,
                        key=aqs_key)

### Filter Parameters
# New York County Data between Jan 1, 2018 and Jan 1, 2022.

# Constants
constants <- list()
constants$BOROUGH <- "Manhattan"
constants$COUNTY <- "New York"
constants$STATE <- "New York"
constants$TIME_LIST <- data.frame(jan18 = "2018-01-01",
               dec18 = "2018-12-31",
               jan19 = "2019-01-01",
               dec19 = "2019-12-31",
               jan20 = "2020-01-01",
               dec20 = "2020-12-31",
               jan21 = "2021-01-01",
               dec21 = "2021-12-31",
               jan22 = "2022-01-01")

constants$TIME_START <- constants$TIME_LIST$jan18
constants$TIME_END <- constants$TIME_LIST$jan22

saveRDS(constants, "./api/processed/nyc_constants.csv")

# New York County Identifiers
identifiers <- list()
state_fips <- data.table(aqs_list_states(aqs_user))
identifiers$ny_fips_code <- state_fips[value_represented == constants$STATE]$code
identifiers$ny_counties <- data.table(aqs_list_counties(aqs_user, state=identifiers$ny_fips_code))
identifiers$nyCounty_fips_code <- identifiers$ny_counties[value_represented == constants$COUNTY]$code

saveRDS(identifiers, "./api/processed/nyc_identifiers.csv")

# Retrieve dataset urls
dataset <- readRDS("./api/processed/nyc_dataset_urls.csv")

# Download the URLs onto disk, to avoid storing in R memory.
# Taxi records are >100+ million, so downloading on disk would be faster.
# You can see status of download in print comments.

for (i in 1:nrow(dataset)){
  url <- dataset[i,]$feature_url
  name <- dataset[i,]$feature_name
  print(paste("Loading dataset:", name, sep = " "))

  fname <- filename(x = name, path = "./data/raw",
                     ext = ".csv", date = NA,
                     time = NA, subdir = FALSE)

  print(paste("Saving dataset:", name, sep = " "))
  dataset[i, ]$loc <- as.character(fname)
  ##download.file(url, as.character(fname))
  print("Dataset saved successfully!")
}

saveRDS(dataset, file="./api/processed/nyc_dataset_list.csv")
