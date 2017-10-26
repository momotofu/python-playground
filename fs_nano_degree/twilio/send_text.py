
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb6ed0a80b9b770fc7d11ee41341a65c2"
# Your Auth Token from twilio.com/console
auth_token = "3f4aa788221625f1150637d7e04e12f4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14358622097",
    from_="+14352362349",
    body="Hey Dad, it's Chris. I'm working on a programming project. If you get this message let me know on facebook messenger. Have a good day! :D")

print(message.sid)
