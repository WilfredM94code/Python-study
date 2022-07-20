# This app is meant to send text messages between an API to a registred phone number. In this case 
# is mine personal
# To get personalize this APP user is supposed to create an account in:
# https://www.twilio.com

# Then the account must be verified and from the account's dashborad
# get the ACCOUNT SID and rhe Authentication TOKEN

# These 2 values are stored in the file 'config.py' contained in the folder where the 'app.py'
# is located. There's also the mobile nuber associated with the API

# This account counts with 15.50$ of credit to test Twilio service


from twilio.rest import Client
from config import account_SID,auth_token,tw_phone_number, my_phone_number

client = Client(account_SID, auth_token)

messager = input('Write a message to send\n')

client.messages.create(
    to = my_phone_number,
    from_ = tw_phone_number,
    body = 'This is a new test, dreams are meant to say something? We dont know, but we think about it'
)
