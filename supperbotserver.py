from flask import Flask, request
import json
import requests

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAZAygcjNS3sBAPG5AC9WEt9FFm3Fi8DZBjb24POoGgm5OpidWyzAJVDHy7bD4ZCsAK9XUzRVnXaCbeopf0RuWaKlvHdvefZBE2SASfivlCPZAC96GBCK9XQCMlVUSkxPxJMxVr7MN3ibJRQ3zJA3ZA7IhjUJ4rT2b7UmAiR5DZAgZDZD'

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
  print payload
  for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)
    send_message(sender, message)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], {
        "text": event["message"]["text"].decode('unicode_escape')}
    else:
      yield event["sender"]["id"], {
        "text": "whatchu sayin fam??"}


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

# To-do:
  # Refactor send messages
  # Functionality: get started button, greeting text, structured messages, instant reply, loading, call by name, share bot, wit.ai, subscribe to notifications
  # Plan features
  # Implement all features
  # Send for review
  # Get feedback
  # other ideas: ync general info, buttery orders, memes/comics

#GIT
  # git add .
  # git commit -m "commit"
  # git push heroku master
  #heroku logs -t

#TESTING WITH SHELL SCRIPT
  # create test.sh.
  # Add permission: chmod +x ./test.sh (https://askubuntu.com/questions/38661/how-do-i-run-sh-files).
  # Run python server file: $ python supperbotserver.py
  # ./test.sh
  # Unsubscribe to page to ensure messages dont get sent to heroku while testing mode.

