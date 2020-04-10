from twilio.rest import Client
import time

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
ACCOUNT_SID = "XXX"
AUTH_TOKEN = "YYY"
client = Client(ACCOUNT_SID, AUTH_TOKEN)
# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

def sendMessage(text):
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+91xxxyyyzzzz'
    client.messages.create(body=text,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)

#Epoch loop
for i in range(5):
    #loss = train(x,y) .. Add other metrics if necessary
    loss = 15.12356-i
    trainAcc = 85+i
    validAcc = trainAcc-5
    myMessage = ["Epoch {} Summary:".format(i),
                "Loss: {}".format(loss),
                "Train Accuracy {}%".format(trainAcc),
                "Validation Accuracy: {}%".format(validAcc),
                ]

    text = "\n".join(myMessage)
    sendMessage(text)
    time.sleep(2)