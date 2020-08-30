# Connects to the coinmarketcap API
# Grabs the relevant data
# Saves it to a json file

import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def grabs_cmc_data_api():
    # cmc_url = 'https://sandbox.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # SANDBOX!!!
    cmc_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': 'BTC,ETH,OMG,XRP,LTC',
        'convert': 'EUR'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': < INSERT YOUR KEY HERE >,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(cmc_url, params=parameters)
        data = json.loads(response.text)
        # data = json.loads(response.content) ## CONTENT MAYBE TO DEAL WITH THE WEIRD FORMATED FILES??????
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    # Cleaning up the value of the timestamp of the json
    # To define the name of the json sfile
    cmc_data_datetime = data['status']['timestamp']
    cmc_data_file_name = cmc_data_datetime
    cmc_data_file_name = cmc_data_file_name.replace(":", "-")
    cmc_data_file_name = cmc_data_file_name.replace("T", "-T")
    cmc_data_file_name = cmc_data_file_name[0:20]
    cmc_data_file_name = "cmc_" + cmc_data_file_name + ".json"

    # Directory where the cmc data is being saved
    cmc_data_directory = "../data/cmc/"
    cmc_data_file = cmc_data_directory + cmc_data_file_name

    # Creates and stores the json file
    with open(cmc_data_file, 'wb') as outf:
        outf.write(response.content)


if __name__ == "__main__":
    # If executed directly, it will grab data from cmc API
    # And create a json file with it
    cmc_data_origin = grabs_cmc_data_api()
