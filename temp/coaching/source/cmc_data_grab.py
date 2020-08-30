# THIS FILE MUST BE UPGRADED TO DECIDE
# IF IT GRABS THE DATA FROM A LOCAL FILE
# OR IF IT USES THE CMM API
# CURRENTLY, IT'S ALWAYS GETTING THE LOCAL DATA
# AND THEN TRANSFORMS IT INTO A DATASET

# Setting up the stage
import pandas as pd


def grabs_cmc_data(cmc_file_origin):
    from cmc_data_grab_local import grabs_cmc_data_local
    cmc_data_origin = grabs_cmc_data_local(cmc_file_origin)
    return cmc_data_origin


def creates_cmc_dataframe(cmc_data_origin):
    cmc_data_origin["data"] = [cmc_data_origin["data"][k] for k in
                               cmc_data_origin["data"].keys()]
    pd.json_normalize(pd.json_normalize(cmc_data_origin).
                      explode("data").to_dict(orient="records"))
    cmc_df = pd.DataFrame.from_dict(cmc_data_origin["data"])
    cmc_df = cmc_df.join(cmc_df['quote'].apply(pd.Series))
    cmc_df = cmc_df.drop('quote', axis=1)
    cmc_df = pd.concat([cmc_df.drop(['EUR'], axis=1), cmc_df['EUR'].apply(pd.Series)], axis=1)
    return cmc_df


if __name__ == "__main__":
    # If executed directly, it will ??????????????
    cmc_file_origin = "cmc_test.json"
    cmc_data_origin = grabs_cmc_data(cmc_file_origin)
    cmc_df_origin = creates_cmc_dataframe(cmc_data_origin)
    print(cmc_df_origin)
