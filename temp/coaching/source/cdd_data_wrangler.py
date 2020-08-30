# Uses the cdd_data_clean module
# to clean cdd data imported from local files (cdd_data_grabber)
# and then formats it to LUIGI patterns

import pandas as pd


def cleans_cdd_data(cdd_data_origin):
    cdd_data_clean = cdd_data_origin
    return cdd_data_clean


def sets_cdd_data_index(cdd_data_clean):
    # Transforms the date from the column Date to datetime format
    cdd_data_clean['Date'] = cdd_data_clean['Date'].apply(pd.to_datetime)
    # Updates the column name Date to DateTime
    cdd_data_clean.rename(columns={"Date": "DateTime"}, inplace=True)
    # Sets the column DateTime as the new Index of the dataframe
    cdd_data_clean.set_index('DateTime', inplace=True)
    return cdd_data_clean


def renames_cdd_data_columns(cdd_data_clean):
    # Changes the column 'Pair' to 'Trading-Pair'
    cdd_data_clean.rename(columns={"Symbol": "Trading-Pair"}, inplace=True)
    # Changes the column index-5 'Volume ???(asset)' to 'Volume'
    cdd_data_clean.columns.values[5] = "Volume"
    return cdd_data_clean


def adds_cdd_data_columns(cdd_data_clean):
    # Adds the colum "Source" indicating from where the data comes from
    cdd_data_clean["Source"] = "CryptoDataDownload"
    # Adds a columns 'Asset' based on the first three letters of the 'Trading-Pair' info
    cdd_data_clean["Asset"] = cdd_data_clean["Trading-Pair"].apply(
        lambda x: x[0:3])
    return cdd_data_clean


def fixes_cdd_data(cdd_data_clean):  # THIS FUNCTION COULD HAVE A BETTER NAME ??????
    # Add a hifen between the trading pairs of the column 'Trading-Pair'
    cdd_data_clean["Trading-Pair"] = cdd_data_clean["Trading-Pair"].apply(
        lambda x: x[:3] + "-" + x[3:])
    return cdd_data_clean


def wranglers_cdd_data(cdd_data_origin):
    cdd_data_clean = cleans_cdd_data(cdd_data_origin)
    cdd_data_clean = sets_cdd_data_index(cdd_data_clean)
    cdd_data_clean = renames_cdd_data_columns(cdd_data_clean)
    cdd_data_clean = adds_cdd_data_columns(cdd_data_clean)
    cdd_data_clean = fixes_cdd_data(cdd_data_clean)
    return cdd_data_clean


if __name__ == "__main__":
    cdd_file_origin = "cdd_test.csv"
    from cdd_data_grabber import grabs_cdd_data
    ccd_data_origin = grabs_cdd_data(cdd_file_origin)
    cdd_data_clean = cleans_cdd_data(ccd_data_origin)
    cdd_data_clean = wranglers_cdd_data(cdd_data_clean)
    print(cdd_data_clean)
