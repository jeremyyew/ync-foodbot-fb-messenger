from flask import Flask, request
import json
import requests
import message_objects as msg
import google_form_submitter as gform

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
            print "############### RECEIVED ###############\n############### MESSAGE: ###############\n", message_text, "\n"

            def match_keyword(text):
                # IF RECOGNIZED TEXT MSG:

                if "Get Started" in text:
                    yield msg.welcome_msg
                    yield msg.start_msg

                elif "#feedback" in text:
                    yield msg.feedback_received_msg

                elif "help" in text:
                    yield msg.start_msg

                # ELSE (NOT RECOGNIZED TEXT MSG):
                else:
                    print "ERROR: not recognized text"
                    yield msg.sorry_msg

            responses = match_keyword(message_text)

        # ELSE IF POSTBACK:
        elif "postback" in event and "payload" in event["postback"]:

            payload = event["postback"]["payload"]

            def match_payload(payload):
                # IF RECOGNIZED PAYLOAD:

                if "GET_STARTED_PB" in payload:
                    yield msg.welcome_msg
                    yield msg.start_msg

                elif "FEEDBACK_PB" in payload:
                    yield msg.feedback_prompt_msg

                elif "GET_INFO_PB" in payload:
                    yield msg.quick_ref_main
                    yield msg.carousel_main

                elif "MENU_CHECK_PB" in payload:
                    yield msg.generate_short_menu_msg()

                elif "AL_AMAAN_MENU_PB" in payload:
                    yield msg.al_amaan_menu_image1_msg
                    yield msg.al_amaan_menu_image2_msg

                elif "COMING_SOON_PB" in payload:
                    yield msg.coming_soon_msg

                elif "CENDANA_BUTTERY_ORDER_PB" in event["postback"]["payload"]:
                    gform.post_form()
                    yield msg.cendana_buttery_form_submitted_msg

                # ELSE (NOT RECOGNIZED POSTBACK)
                else:
                    print "ERROR: not recognized postback"
                    yield msg.sorry_msg

            responses = match_payload(payload)

        # ELSE (NOT TEXT MSG && NOT POSTBACK):
        else:
            print "ERROR: not recognized text or postback"
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

