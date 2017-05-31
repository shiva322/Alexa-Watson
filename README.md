# Alexa-Watson

Here Alexa skill is developed with the help of flask-ask along with ngrok(for tunneling https to local http) and Echosim.io (Cloud based client for Alexa Voice Service API) is used as the interface to interact with our alexa skill.

Alternate approach is to bring up local java client to act as an interface - https://github.com/alexa/alexa-avs-sample-app (uses java for client and node server to establish identity confifuration with amazon account)

Dependencies -

	flask
	flask-ask (https://flask-ask.readthedocs.io/en/latest/)
	watson-developer-cloud	
	ngrok 

Step1 :
 > Create watson's conversion service and workspace in ibm blumix account.
 
 > Note workspace's username;password;workspace-id


Step2:
> configure watson configuration in ask-watson.py. run ask-watson.py

Step3:
> tunnel localhost http request as https using ngrok

Step4:
> Add created skill in Alexa Skill Kit in amazons's developer portal as an HTTPS endpoint.

> Use Interaction model as below -
  
	"intents": [

    {
      "name": "CancelIntent",
      "samples": [],
      "slots": []
    },
    {
      "name": "ColorIntent",
      "samples": [
        "color",
        "favorite color",
        "my favorite color is {color} ",
        "{color} is my favorite color"
      ],
      "slots": [
        {
          "name": "color",
          "type": "AMAZON.Color",
          "samples": []
        }
      ]
    },
    {
      "name": "HelloIntent",
      "samples": [
        "launch",
        "start",
        "run",
        "begin",
        "open",
        "hi",
        "hello"
      ],
      "slots": []
    },
    {
      "name": "HelpIntent",
      "samples": [
        "help",
        "info",
        "information"
      ],
      "slots": []
    },
    {
      "name": "SessionEndedRequest",
      "samples": [],
      "slots": []
    },
    {
      "name": "StopIntent",
      "samples": [
        "stop",
        "end"
      ],
      "slots": []
    },
    {
      "name": "UnforgivableCurses",
      "samples": [],
      "slots": []
    }]


> Use Invocation name as 'watson' (The name customers use to activate the skill. For example, "Alexa ask Watson...".)

Step 5:
> Login into Echosim.io with above amazon developer account and start testing the skill configured.
