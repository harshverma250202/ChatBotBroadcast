# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC5b469b0c07a8c5fe06be126f5c3836a7"
auth_token = "b8b4eb455252720b2dfd61a6384c5355"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='cat likh kar bhej bosdk',
                              to='whatsapp:+919695448779'
                          )

print(message)