
m twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb6ed0a80b9b770fc7d11ee41341a65c2"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
