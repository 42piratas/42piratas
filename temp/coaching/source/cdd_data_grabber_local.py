'''This module grabs data from local CSV files imported from
www.cryptodatadownload.com/data and returns a dataframe with it
'''

# Setting up the stage!
import os
import logging
import pandas as pd
from logger import *


def grabs_cdd_data_local(cdd_file_name,
                         cdd_file_path="../data/cdd/"):
    """Calls the module 'grabs_cdd_data_local' and returns cdd data

    Parameters
    ----------
    cdd_origin : cdd csv filename

    Returns
    -------
    dataframe
        cdd_data_origin

    See Also
    --------
    cdd_data_grabber_local
    """
    cdd_file_origin = cdd_file_path + cdd_file_name
    if not os.path.isfile(cdd_file_origin):
        error_msg = "COULD NOT FIND THE FILE"
        logging.critical(error_msg + ":" + cdd_file_origin)
        return "COULD NOT FIND THE FILE!"
    else:
        cdd_data_origin = pd.read_csv(cdd_file_origin, skiprows=[0])
        logging.info("Successfully read CDD csv file " + cdd_file_origin + " && returned dataframe")
        return cdd_data_origin


if __name__ == "__main__":
    # If executed directly, it will activate the function grabs_cdd_data_local()
    # to read the local cdd csv test file (which must be in the default path)
    # and return the data as a dataframe
    cdd_file_origin = "cdd_test.csv"
    cdd_data_origin = grabs_cdd_data_local(cdd_file_origin)
    print(cdd_data_origin)
    logging.info("Executed from __main__\n" + log_end_line)
