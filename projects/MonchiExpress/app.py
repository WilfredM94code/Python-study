# API KEY:
# TxoFTA46xx1ACThFu_EU90i7doQYv5CBfYevuKb6WFsaDZVFhtV_Nyvr9R14SSutA-hwc75FjC7VXr_JkkQEfqZD7RJifEc6FafkImuubGFsn2F7Eb0MUR7y0TtBYnYx

# Client ID
# nh_mVVTOPfjLAyqCjmHnnQ

# Api end port
# https://api.yelp.com/v3/businesses/search

import config
import requests
client_ID = 'nh_mVVTOPfjLAyqCjmHnnQ'
api_ep = 'https://api.yelp.com/v3/businesses/search'


# The usage of the request library requires an important level of understanding of HTTP
# All the data liked to HTTP can be found in the next link:
# https://www.tutorialspoint.com/http/index.htm
# https://realpython.com/python-requests/

# Every note taken of this topic will be on a file called
# HTTP

# To work with the YELP API is required to get an authorization
# To do that we have to send a JSON request with the request details
# For the request library, every request made can accept parameters in the form of dictionaries
# Which then will be coverted to JSON

# The request headers is defined next

headers = {
    'Authorization': 'Bearer ' + config.api_key
}

# The request parameters are defined next
# The API request params can be found here https://www.yelp.com/developers/documentation/v3/business_search

params = {
    'term': 'salon',
    'limit': 30,
    'location': 'Miami',
}

response = requests.get(api_ep, headers=headers, params=params)
print('response = ', response)
print('type(response) = ', type(response))

businesses = response.json()['businesses']

for business in businesses:
    for data in business:
        data = str(data)
        print('bussiness', data, 'name = ', business[data])
    print('\n')

# This API returns a json object which contains data of several business
# The data retrive stands for the request made using the parameters stablished
# These parameters can be changed according to the ones that can recieve the server to retrive data

# To avoid placing and api key or any sensitive data on the repository this can be placed in
# another Python file and call the value from that module.

# To avoid this file with data away from any git commit there has to be created a '.gitignore' file
# with the name of the file not meant to be commited or push in it
