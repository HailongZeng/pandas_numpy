# from twilio import rest
# rest.TwilioRestClient
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = 'ACd5751f3068d5e314ad8a61f01664900'
auth_token = ''
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = 'My name is Hailong Zeng?',     # message information
    to = '' ,       # replace with your own phone number
    from_ = ''     # replace with your Twilio Number
)
print message.sid