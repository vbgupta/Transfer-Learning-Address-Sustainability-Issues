from path import Path
import pandas as pd
from sodapy import Socrata
import pathlib

def socrata_client(client_url: str, dataset_api_key: str, foldername: str, filename: str):
    """
    client_url = found under developer portal -> str
    dataset_api_key = found under developer portal -> str
    filename = depends on which dataset (personal choice) -> str
    Example: 
    socrata_client(client_url = "usc.data.socrata.com", dataset_api_key= "bhyw-mxf5", foldername = "AQI",
    filename= "LA-AQ-Data")
    """

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata(client_url, None)

    # First 10,000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get(dataset_api_key, limit=100000000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    # Save the result to the data folder
    #data_dir = pathlib.Path("./data")
    data_dir = "./data/" + foldername
    print(data_dir)
    results_df.to_csv(data_dir + "/" + filename + ".csv")

    # Print the results
    print(results_df.head())
    return results_df
socrata_client(client_url = "usc.data.socrata.com", dataset_api_key= "bhyw-mxf5", foldername = "AQI", filename= "LA-AQ-Data-2")