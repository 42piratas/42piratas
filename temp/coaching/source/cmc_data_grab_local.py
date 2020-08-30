# This module grabs the datasets from local files
# imported/saved from coinmarketcap.com
# and stored in the directory /data/cmc/
# and retrieves the relevant data
# THIS MODULE DO NOT CONNECTS WITH CMC APIS

# # Setting up the stage!
import json
import os


def grabs_cmc_data_local(file_name,
                         file_path="../data/cmc/"):

    cmc_file_origin = file_path + file_name
    if not os.path.isfile(cmc_file_origin):
        return "COULD NOT FIND THE FILE!"
    else:
        cmc_file_origin = open(cmc_file_origin)
        cmc_data_origin = cmc_file_origin.read()
        cmc_data_origin = json.loads(cmc_data_origin)
        return cmc_data_origin


if __name__ == "__main__":
    # If executed directly, it will grab data
    # From the specified json file and prints it
    cmc_file_origin = "cmc_test.json"
    cmc_data_origin = grabs_cmc_data_local(cmc_file_origin)
    print(cmc_data_origin)
