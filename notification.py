from twilio.rest import Client

def sendNotification():
    # Your Account SID from twilio.com/console
    account_sid = 'ACa54aafa1c425ecffb7604fb412f093ce'
    # Your Auth Token from twilio.com/console
    auth_token  = '117974b01c33d09f18e0bc1f2b172f4b'
    numbers = ["+16478863575"]
    outgoing_number = "+16726480239"

    client = Client(account_sid, auth_token)

    for num in numbers:
        print(num)
        message = client.messages.create(
            to=num, 
            from_=outgoing_number,
            body="One of your roommates has not refilled the Brita!")
        print(message.sid)
