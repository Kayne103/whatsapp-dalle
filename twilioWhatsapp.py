from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)


def send_whatsapp_message(dalle_response: any, whatsapp_receiver: str, message: str):

    message = client.messages.create(
        from_=twilio_whatsapp_number,
        body=message,
        media_url=dalle_response,
        to=whatsapp_receiver
    )

    print(message.sid)
