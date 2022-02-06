# Los Angeles Air Quality Data
from path import Path
d = Path(__file__).parent.parent
print(d)
Path(d).chdir()

from src.api.open_data import socrata_client

socrata_client(client_url = "usc.data.socrata.com", 
dataset_api_key= "bhyw-mxf5", 
filename= "LA-AQ-Data")
