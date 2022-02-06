from path import Path
d = Path(__file__).parent.parent.parent
print(d)
Path(d).chdir()
import pandas as pd
from sodapy import Socrata


def socrata_client(dataset_api_key: str, filename: str):

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("usc.data.socrata.com", None)

    # First 10,000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get(dataset_api_key, limit=10000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    # Save the result to the data/raw folder
    results_df.to_csv('DS440-Transfer-Learning-Address-Sustainability-Issues/data/raw/' + filename)

    # Print the results
    print(results_df.head())
    return results_df


socrata_client(dataset_api_key= "bhyw-mxf5", filename= "LA-AQ-Data")