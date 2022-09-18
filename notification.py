from dotenv import load_dotenv
from twilio.rest import Client
import os
import json

load_dotenv()

def sendNotification():
    # Your Account SID from twilio.com/console
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    # Your Auth Token from twilio.com/console
    auth_token  = os.getenv('TWILIO_AUTH_TOKEN')
    numbers = json.loads(os.environ['PHONE_NUMBERS'])
    outgoing_number = os.getenv('OUTGOING_NUMBER')

    client = Client(account_sid, auth_token)

    for num in numbers:
        message = client.messages.create(
            to=num, 
            from_=outgoing_number,
            body="One of your roommates has not refilled the Brita!")
        print(message.sid)

sendNotification()