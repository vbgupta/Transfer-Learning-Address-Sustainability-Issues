# Empty list to store urls
dataset <- list()

# Store urls
dataset$bridgeHoldLocStipulations <- "https://data.cityofnewyork.us/resource/ge3f-inui.json?boroughname=MANHTTAN"

dataset$busBreakdownsDelays <- "https://data.cityofnewyork.us/resource/ez4e-fazm.json?boro=Manhattan&$where=created_on between '2018-01-01' and '2022-01-01'"

dataset$commercialBicycleInspections <- "https://data.cityofnewyork.us/resource/tg3t-nh4h.json?borough=Manhattan&$where=inspectiondate between '2018-01-01' and '2022-01-01'"

dataset$streetConstructionPermits <- "https://data.cityofnewyork.us/resource/tqtj-sjs8.json?boroughname=MANHATTAN&$where=createdon between'2018-01-01' and '2022-01-01'"

dataset$motorCrashes <- "https://data.cityofnewyork.us/resource/h9gi-nx95.json?borough=MANHATTAN&$where=crash_date between '2018-01-01' and '2022-01-01'"

dataset$speedReducerTracking <- "https://data.cityofnewyork.us/resource/9n6h-pt9g.json?borough=Manhattan"

dataset$serviceRequests311 <- "https://data.cityofnewyork.us/resource/erm2-nwe9.json?borough=MANHATTAN"

dataset$gasRetailPriceWeekly <- "https://data.ny.gov/resource/nqur-w4p7.json?$where=date between '2018-01-01' and '2022-01-01'"

dataset$dieselRetailPriceWeekly <- "https://data.ny.gov/resource/dtfv-pchi.json?$where=date between '2018-01-01' and '2022-01-01'"

dataset$bulkStorageFacilities <- "https://data.ny.gov/resource/pteg-c78n.json?county=NEW YORK"

dataset$spillIncidents <- "https://data.ny.gov/resource/u44d-k5fk.json?$where=spill_date>'2018-01-01'&county=New York"

dataset$hourlyTrafficMTA <- "https://data.ny.gov/resource/qzve-kjga.json?$where=date between '2018-01-01' and '2022-01-01'"

dataset$subwayCustomerJourneyMTA <- "https://data.ny.gov/resource/r7qk-6tcy.json?$where=month>'2017-01'"

dataset$nypaNetGenerationByFacility <- "https://data.ny.gov/resource/isux-jnrn.json?$where=year>'2017'"

dataset$utilityBaseRateChangeByCompany <- "https://data.ny.gov/resource/ddrw-g9a6.json?$where=date_effective between '2018-01-01' and '2022-01-01'"

dataset$keyCreditCollection <- "https://data.ny.gov/resource/kdjh-dhwi.json?$where=year>2017"

dataset$waterWells <- "https://data.ny.gov/resource/6gke-uhe4.json?county=New York"

dataset$wastewaterTreatment <- "https://data.ny.gov/resource/2v6p-juki.json?city=NEW YORK"

dataset$nyMTAEvents511 <- "https://data.ny.gov/resource/i8wu-pqzv.json?$where=create_time>'2018-01-01'&county=New York"

dataset$busCustomerJourneyMetricsMTA <- "https://data.ny.gov/resource/8mkn-d32t.json?$where=month>'2018-01'&borough='Manhattan'"

dataset$performanceKPIByAgencyMTA <- "https://data.ny.gov/resource/cy9b-i9w9.json?$where=period_year > '2017'"

dataset$greenTaxiTripData2018 <- "https://data.cityofnewyork.us/resource/w7fs-fd9i.json"

dataset$yellowTaxiTripData2018 <- "https://data.cityofnewyork.us/resource/t29m-gskq.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$FHVTripData2018 <- "https://data.cityofnewyork.us/resource/am94-epxh.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$greenTaxiTripData2019 <- "https://data.cityofnewyork.us/resource/q5mz-t52e.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$yellowTaxiTripData2019 <- "https://data.cityofnewyork.us/resource/2upf-qytp.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$FHVTripData2019 <- "https://data.cityofnewyork.us/resource/u6nh-b56h.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$greenTaxiTripData2020 <- "https://data.cityofnewyork.us/resource/pkmi-4kfn.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$yellowTaxiTripData2020 <- "https://data.cityofnewyork.us/resource/kxp8-n2sj.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$FHVTripData2020 <- "https://data.cityofnewyork.us/resource/m3yx-mvk4.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$greenTaxiTripData2021 <- "https://data.cityofnewyork.us/resource/djnb-wcxt.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$yellowTaxiTripData2021 <- "https://data.cityofnewyork.us/resource/m6nq-qud6.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$FHVTripData2021 <- "https://data.cityofnewyork.us/resource/a444-au9b.json?$limit=100000000&$offset=105000000&$order=:id"

dataset$alternativeFuelStations <- "https://data.ny.gov/resource/bpkx-gmh7.json?$where=city='Manhattan' or city='New York'"

# Convert list to data.frame
dataset <- stack(dataset)[, c("ind", "values")]
names(dataset) <- c("feature_name", "feature_url")
dataset$feature_name <- as.character(dataset$feature_name)
dataset$feature_url <- as.character(dataset$feature_url)

# Save data urls for future reference
saveRDS(dataset, file="./api/processed/nyc_dataset_urls.csv")
