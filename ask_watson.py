import os
import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json

app = Flask(__name__)

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
#Setup Logging to a file
logging.basicConfig(filename='watson.log',level=logging.DEBUG)

# Setup Credentials on initialization to conversation service  
from watson_developer_cloud import AuthorizationV1
from watson_developer_cloud import ConversationV1

workspace_id = '7f749a89-5fa8-4893-b6a1-b14abc718c8a'
conv_username = 'a482ff6b-ef54-4025-aad6-fb10d19bc792'
conv_password =  'x5t01eec8Gt2'

# Call Conversation Service
conversation = ConversationV1(
    username = conv_username,
    password = conv_password,
    version='2016-09-20')

logging.debug('Checking Conversation Service is working')
response = conversation.message(workspace_id=workspace_id, message_input={'text': 'Hello'})
print(json.dumps(response, indent=2))
            
ask = Ask(app, "/")

@ask.launch
def launch_watson():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)



@ask.intent("HelloIntent", convert={'Phrase': str})
def hellowatson(Phrase):

    response = conversation.message(workspace_id=workspace_id, message_input={'text': Phrase})
    return question(json.dumps(response['output']['text'])).reprompt("Sorry Shiva I didn't understand what you said")


@ask.intent('ColorIntent',default={'color': 'blue'})
def favcolor(color):
    session.attributes['favcolor']=color
    msg = render_template('favcolor',color=color)
    return statement(msg)

@ask.session_ended
def session_ended():
    return "{}", 200

@ask.on_session_started
def new_session():
    logging.debug('New session started')


if __name__ == '__main__':
    print("APP RUNNING :  0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

