# Uses the cdd_data_grabber module
# to import cdd data from local files
# and then cleans it

def cleans_cmc_data(data):
    return data


if __name__ == "__main__":
    # If executed directly, it will ???????????????????
    from cmc_data_grab import grabs_cmc_data
    cmc_file_origin = "cmc_test.json"
    cmc_data_origin = grabs_cmc_data(cmc_file_origin)
    cmc_data_clean = cleans_cmc_data(cmc_data_origin)
    print(cmc_data_clean)
