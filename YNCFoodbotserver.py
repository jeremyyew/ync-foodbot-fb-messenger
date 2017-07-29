import json
import time

import requests
from flask import Flask, request
import message_objects as msg
import match_keyword as match

app = Flask(__name__)
PAT = 'EAAZAygcjNS3sBAPG5AC9WEt9FFm3Fi8DZBjb24POoGgm5OpidWyzAJVDHy7bD4ZCsAK9XUzRVnXaCbeopf0RuWaKlvHdvefZBE2SASfivlCPZAC96GBCK9XQCMlVUSkxPxJMxVr7MN3ibJRQ3zJA3ZA7IhjUJ4rT2b7UmAiR5DZAgZDZD '

@app.route('/', methods=['GET'])
def handle_verification():
    print "Handling Verification."
    if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
        print "Verification successful!"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
    print "Handling Messages"
    payload = request.get_data()
    for sender, message in messaging_events(payload):
        #print "Incoming from %s: %s" % (sender, message)
        print "*************** SENDING RESPONSE: *************** \n", message, "\n"
        send_message(sender, message)
    return "ok"

def messaging_events(payload):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]

    for event in messaging_events:
        # IF TEXT MSG:
        sender_id = event["sender"]["id"]

        if "message" in event and "text" in event["message"]:
            message_text = event["message"]["text"]
            print "############### RECEIVED ###############\n############### MESSAGE: ###############\n", message_text.encode('unicode_escape'), "\n"
            #responses = match_text_or_payload(message_text)
            responses = match.match_text_or_payload(message_text, sender_id)

        # ELSE IF POSTBACK:
        elif "postback" in event and "payload" in event["postback"]:
            postback = event["postback"]["payload"]
            print "############### RECEIVED ###############\n############### POSTBACK: ###############\n", postback, "\n"
            #responses = match_text_or_payload(postback)
            responses = match.match_text_or_payload(postback, sender_id)

        # ELSE (NOT TEXT MSG && NOT POSTBACK):
        else:
            print "ERROR: message not text or postback"
            responses = msg.sorry_msg

        for response in responses:
            yield sender_id, response

def send_message(recipient, message):
    """Send the message text to recipient with id recipient.
    """

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": PAT},
                      data=json.dumps({
                          "recipient": {"id": recipient},
                          "message": message
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text



if __name__ == '__main__':
    app.run()

    
#GIT
# git add .
# git commit -m "commit"
# git push heroku master
#heroku logs -t

#TESTING WITH SHELL SCRIPT
# create test.sh.
# Add permission: chmod +x ./test.sh (https://askubuntu.com/questions/38661/how-do-i-run-sh-files).
# Run python server file: $ python YNCFoodbotserver.py
# ./test.sh
# Unsubscribe to page to ensure messages dont get sent to heroku while testing mode.

