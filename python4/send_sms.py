from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC99594ce1db30987a6b486f3119705a56'
auth_token = '379139aed96a4a1a4545bdd877606386'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12819378585',
                     to='+919908201758'
                 )

print(message.sid)
