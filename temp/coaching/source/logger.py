# Setting up the stage
import logging
from datetime import datetime

log_end_line = "-"*80

# Setting logging format
today_year = str(datetime.now().strftime("%Y"))
today_month = str(datetime.now().strftime("%m"))
today_date = str(datetime.now().strftime("%Y-%m-%d"))
# log_folder = "../logs/" + today_year + today_month
# log_name = "luigi-" + today_date + ".log"
# log_file = log_folder + log_name
log_file = "../logs/luigi-" + today_date + ".log"
log_format = "***%(levelname)s*** %(asctime)s Trigger:%(name)s Filename:%(filename)s\nFunction:%(funcName)s Message: %(message)s"
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format=log_format)
