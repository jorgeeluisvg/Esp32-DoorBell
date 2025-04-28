from fastapi import FastAPI, Request
from twilio.rest import Client

app = FastAPI()

# Configura tus credenciales de Twilio
TWILIO_ACCOUNT_SID = 'TU_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'TU_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = '+1XXXXXXXXXX'  # Número de Twilio
MY_PHONE_NUMBER = '+52XXXXXXXXXX'  # Tu número real

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.post("/send-sms")
async def send_sms(request: Request):
    data = await request.json()
    message_body = data.get("message", "Alguien tocó el timbre")

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

    return {"status": "Mensaje enviado", "sid": message.sid}
