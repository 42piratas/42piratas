'''This module grabs the data imported from www.cryptodatadownload.com/data
and orchestrates the process of data cleaning and data formating according to
the needs of LUIGI. Other similar 'xxx_data_grab' modules (i.e. equivalent
modules for other sources) decide (based on factors of date and time, and usage
of API) if they should import the data from local files (calling their
respective 'xxx_data_grab_local') or if they should import new data from the
source's API (calling their respective 'xxx_data_grab_api') BUT
cryptodatadownload.com doesn't have an API, therefore this module only exists to
follow Luigi's architecture pattern and it always calls 'cdd_data_grabber_local'.
It retuns a Pandas DataFrame!
'''

# Setting up the stage
import logging
from logger import *


def grabs_cdd_data(cdd_origin):
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
    from cdd_data_grabber_local import grabs_cdd_data_local
    cdd_data_origin = grabs_cdd_data_local(cdd_origin)
    logging.info("Successfully returned CDD dataframe")
    return cdd_data_origin


if __name__ == "__main__":
    # If executed directly, it will activate the function grabs_cdd_data() to
    # read the local cdd csv test file (which must be in the default path)
    # through the module cdd_data_grabber_local and return the data as a dataframe
    cdd_file_origin = "cdd_test.csv"
    cdd_data_origin = grabs_cdd_data(cdd_file_origin)
    print(cdd_data_origin)
    logging.info("Executed from __main__\n" + log_end_line)
