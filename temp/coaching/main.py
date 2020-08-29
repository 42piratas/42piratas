
# import pandas as pd
from cdd_data_grab import *
from cdd_data_clean import *
from cdd_data_format import *

# Manages data from CryptoDataDownload
cdd_file_origin = "cdd_test_file.csv"
 = cdd_grabs_data(cdd_file_origin)
cdd_data_clean = cleans_cdd_data()
cdd_data_format = formats_cdd_data(cdd_data_clean)

print()
