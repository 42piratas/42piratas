# import pandas as pd
from cdd_data_grabber import *
from cdd_data_wrangler import *

# LUIGIS data from CryptoDataDownload
cdd_file_origin = "cdd_test.csv"
cdd_data_origin = grabs_cdd_data(cdd_file_origin)
cdd_data_clean = wranglers_cdd_data(cdd_data_origin)
print(cdd_data_clean)