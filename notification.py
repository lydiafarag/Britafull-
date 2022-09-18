<<<<<<< HEAD
from twilio.rest import Client

def sendNotification():
    # Your Account SID from twilio.com/console
    account_sid = 'ACa54aafa1c425ecffb7604fb412f093ce'
    # Your Auth Token from twilio.com/console
    auth_token  = '117974b01c33d09f18e0bc1f2b172f4b'
    numbers = ["+16478863575"]
    outgoing_number = "+16726480239"
=======
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
>>>>>>> d3927b2b0f2613f4651794c3df2ee14a7e47b6e5

    client = Client(account_sid, auth_token)

    for num in numbers:
<<<<<<< HEAD
        print(num)
=======
>>>>>>> d3927b2b0f2613f4651794c3df2ee14a7e47b6e5
        message = client.messages.create(
            to=num, 
            from_=outgoing_number,
            body="One of your roommates has not refilled the Brita!")
<<<<<<< HEAD
        print(message.sid)
=======
        print(message.sid)

sendNotification()
>>>>>>> d3927b2b0f2613f4651794c3df2ee14a7e47b6e5
