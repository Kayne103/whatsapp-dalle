from fastapi import FastAPI, Form
from dalle import create_image
from twilioWhatsapp import send_whatsapp_message

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/whatsapp")
async def create_image_with_prompt(Body: str = Form(), From: str = Form()):
    print(From)
    dalle_response = create_image(Body)

    return send_whatsapp_message(dalle_response, From, Body)
