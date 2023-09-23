import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from src.movie_recommend import execute_python
# import src.services as services

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    print(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith('Recommend'):
        code = incoming_msg.strip("Recommend")
        output = execute_python(code)
        msg.body(output)
        msg.body('You can find the movies here: https://netflix.com/movies')
    else:
        msg.body("Hello and welcome to movie recommendation whatsapp bot. \n"
                 "Type Recommend and your movie name and we will send you a list of 30 recommended movies which we "
                 "think you will love!!")
    return str(resp)

if __name__ == '__main__':
    app.run()
