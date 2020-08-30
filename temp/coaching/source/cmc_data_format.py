# ??????
# ??????


# Setting up the stage!
import pandas as pd


def formats_cmc_data(cmc_data_origin):
    return cmc_data_origin


if __name__ == "__main__":
    # If executed directly, it will ???????????????????
    from cmc_data_grab import grabs_cmc_data
    from cmc_data_clean import cleans_cmc_data
    cmc_file_cmc_data_origin = "cmc_test.json"
    cmc_data_cmc_data_origin = grabs_cmc_data(cmc_file_cmc_data_origin)
    cmc_data_clean = cleans_cmc_data(cmc_data_cmc_data_origin)
    cmd_data_format = formats_cmc_data(cmc_data_clean)
    print(cmd_data_format)
