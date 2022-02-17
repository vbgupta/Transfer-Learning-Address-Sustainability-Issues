---
  title: "New York City Data Exploration"
output: html_notebook
---

  # Load Libraries
library(RSocrata)

token <- "4Jrp0nApWrWTccxWBdfilSWwq"

#Store user email and password
socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "dpr5375@psu.edu")
socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "ds440@Capstone")


# Retrieve Dataset from Socrata API
# noise311  <- read.socrata(
#   "https://data.cityofnewyork.us/resource/h9gi-nx95.json?$limit=200000",
#   email     = socrataEmail,
#   password  = socrataPassword
# )
# nrow(noise311)

# saveRDS(noise311, file = "noise311.csv")

noise311 <- readRDS("noise311.csv")

head(noise311)
str(noise311)


# Open Parking and Camera Violations

trafficDatasets <- "https://data.cityofnewyork.us/browse?category=Transportation&limitTo=datasets&sortBy=last_modified&undefined=&page=2"

url <-"https://data.cityofnewyork.us/resource/nc67-uf89.json?$limit=10000"

traffic <- "https://data.cityofnewyork.us/resource/i4gi-tjb9.json"

streetLightsDOT <- "https://data.cityofnewyork.us/Transportation/DOT-Street-Lights-and-Traffic-Signals-311-Service-/jwvp-gyiq"

biannualPedsCounts <- "https://data.cityofnewyork.us/resource/cqsj-cfgu.json"

motorCrashes <- "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

streetConstructionPermits <- "https://data.cityofnewyork.us/resource/tqtj-sjs8.json"

bridgeHoldLocStipulations <- "https://data.cityofnewyork.us/resource/ge3f-inui.json"

busBreakdownsDelays <- "https://data.cityofnewyork.us/Transportation/Bus-Breakdown-and-Delays/ez4e-fazm"

speedReducerTracking <- "https://data.cityofnewyork.us/Transportation/Speed-Reducer-Tracking-System-SRTS-/9n6h-pt9g"

commercialBicycleInspections <- "https://data.cityofnewyork.us/resource/tg3t-nh4h.json"

streetPavementRating <- "https://data.cityofnewyork.us/resource/gjkm-nzmg.json"

aqi <- "https://data.cityofnewyork.us/resource/c3uy-2p5r.json"

parkingViolations  <- read.socrata(url = url,  email  = socrataEmail,password = socrataPassword)
nrow(parkingViolations)
str(parkingViolations)

# Water Consumption


# factors
historicLandUse <- "https://data.cityofnewyork.us/Environment/Historic-Land-Use-Data/r9ca-6t4q"

waterSewerPermits <- "https://data.cityofnewyork.us/resource/4k4u-823g.json"

watershedWaterQualitySites <- "https://data.cityofnewyork.us/resource/kw4v-6nqf.json"

watershedWaterQualityWastewater <- "https://data.cityofnewyork.us/resource/icbf-663g.json"

# new branch
# helpful for pre-covid to post

