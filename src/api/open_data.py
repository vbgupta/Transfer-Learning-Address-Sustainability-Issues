from path import Path
d = Path(__file__).parent.parent.parent
Path(d).chdir()
import pandas as pd
from sodapy import Socrata

def socrata_client(client_url: str, dataset_api_key: str, filename: str):
    """
    client_url = found under developer portal -> str
    dataset_api_key = found under developer portal -> str
    filename = depends on which dataset (personal choice) -> str

    Example: 
    socrata_client(client_url = "usc.data.socrata.com", dataset_api_key= "bhyw-mxf5", filename= "LA-AQ-Data")
    """

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata(client_url, None)

    # First 10,000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get(dataset_api_key, limit=10000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    # Save the result to the data/raw folder
    results_df.to_csv('data/raw/'+ filename)

    # Print the results
    print(results_df.head())
    return results_df

    