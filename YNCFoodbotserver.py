from flask import Flask, request
import json
import requests
import message_objects as msg
import google_form_submitter as gform
import time

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

        def match_text_or_payload(input):
            # IF RECOGNIZED TEXT MSG/POSTBACK:
            def input_contains(keys):
                return any(key in input for key in keys)

            if input_contains(["Get Started", "start", "GET_ STARTED_PB"]):
                yield msg.welcome_msg
                time.sleep(1)
                send_typing_msg(sender_id)
                time.sleep(2)
                yield msg.start_msg

            elif input_contains(["info", "INFO_PB"]):
                yield msg.info_msg

            elif input_contains(["dh", "DH_PB"]):
                yield msg.generate_short_menu_msg()

            elif input_contains(["buttery", "BUTTERY_PB"]):
                yield msg.buttery_msg

            elif input_contains(["amaan", "AMAAN_PB"]):
                yield msg.al_amaan_menu_image1_msg
                yield msg.al_amaan_menu_image2_msg

            elif input_contains(["macs", "MACS_PB"]):
                yield msg.sorry_msg

            elif input_contains(["agora", "AGORA_PB"]):
                yield msg.sorry_msg

            elif input_contains(["utown", "UTOWN_PB"]):
                yield msg.sorry_msg

            elif input_contains(["explore", "EXPLORE_PB"]):
                yield msg.sorry_msg

            elif input_contains(["help", "HELP_PB"]):
                yield msg.start_msg

            elif input_contains(["FEEDBACK_PB", "feedback"]):
                yield msg.feedback_prompt_msg

            elif input_contains(["#feedback"]):
                yield msg.feedback_received_msg

            elif input_contains(["get all", "GET_ALL_PB"]):
                yield msg.info_msg
                yield msg.all_carousels_msg

            elif "COMING_SOON_PB" in payload:
                yield msg.coming_soon_msg

            # ELSE (NOT RECOGNIZED text or postback: ):
            else:
                print "ERROR: not recognized text or postback"
                yield msg.sorry_msg

            #elif "CENDANA_BUTTERY_ORDER_PB" in event["postback"]["payload"]:
                #gform.post_form()
                #yield msg.cendana_buttery_form_submitted_msg


        if "message" in event and "text" in event["message"]:
            message_text = event["message"]["text"]
            print "############### RECEIVED ###############\n############### MESSAGE: ###############\n", message_text.encode('unicode_escape'), "\n"
            responses = match_text_or_payload(message_text)

        # ELSE IF POSTBACK:
        elif "postback" in event and "payload" in event["postback"]:
            postback = event["postback"]["payload"]
            print "############### RECEIVED ###############\n############### POSTBACK: ###############\n", postback, "\n"
            responses = match_text_or_payload(postback)

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

def send_typing_msg(recipient):
    """Send the message text to recipient with id recipient."""
    

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": PAT},
                      data=json.dumps({
                          "recipient": {"id": recipient},
                          "sender_action": "typing_on"
                      }),
                      headers={'Content-type': 'application/json'})
    print "REQUEST: ", r.text
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

