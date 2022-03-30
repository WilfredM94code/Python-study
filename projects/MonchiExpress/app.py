# API KEY:
# TxoFTA46xx1ACThFu_EU90i7doQYv5CBfYevuKb6WFsaDZVFhtV_Nyvr9R14SSutA-hwc75FjC7VXr_JkkQEfqZD7RJifEc6FafkImuubGFsn2F7Eb0MUR7y0TtBYnYx

# Client ID
# nh_mVVTOPfjLAyqCjmHnnQ

# Api end port
# https://api.yelp.com/v3/businesses/search

client_ID = 'nh_mVVTOPfjLAyqCjmHnnQ'
api_key = 'TxoFTA46xx1ACThFu_EU90i7doQYv5CBfYevuKb6WFsaDZVFhtV_Nyvr9R14SSutA-hwc75FjC7VXr_JkkQEfqZD7RJifEc6FafkImuubGFsn2F7Eb0MUR7y0TtBYnYx'
api_ep = 'https://api.yelp.com/v3/businesses/search'

import requests

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

# The request 

response = requests.get(api_ep)
print ('response = ',response)

print ('type(response) = ',type(response))