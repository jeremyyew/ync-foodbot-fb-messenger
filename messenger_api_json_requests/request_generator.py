import json

# generate json request shell files
def generate_json_request(pre, payloads, filename, url):
    text_file = open(filename, "w+")
    for payload in payloads:
        request = pre + " \'" + json.dumps(payload) + "\' " + url + "\n"
        text_file.write(request)
    text_file.close()
    return

# set params
thread_settings_url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"
pre = "curl -X POST -H \"Content-Type: application/json\" -d"
fn = "messenger_api_json_requests.sh"

# create setting payloads
greeting_pl = {"setting_type": "greeting", "greeting": {"text": "Hungry? I gotchu fam."}}
get_started_pl = {
    "setting_type": "call_to_actions",
    "thread_state": "new_thread",
    "call_to_actions": [
        {
            "payload": "GET_STARTED_PB"
        }
    ]
}
persistent_menu_pl = {
  "setting_type":"call_to_actions",
  "thread_state":"existing_thread",
  "call_to_actions": [
        {
          "type": "postback",
          "title": "What\u0027s cooking?",
          "payload": "MENU_CHECK_PB"
        },
        {
          "type": "postback",
          "title": "Order from buttery",
          "payload": "CENDANA_BUTTERY_ORDER_PB"
        },
        {
          "type": "postback",
          "title": "Discover new food",
          "payload": "COMING_SOON_PB"
        }
      ],
}

#generate file
generate_json_request(pre, [greeting_pl, get_started_pl, persistent_menu_pl], fn, thread_settings_url)

# set params
message_attachments_url = "https://graph.facebook.com/v2.6/me/message_attachments?access_token=EAAZAygcjNS3sBAEZCWHjMDwU8gW0OartsOxT1MElrwMpB4mHZCuniZBifZAKIT3sPTYgfJNVzPfO0EMnZANwZBEGGYPMU6tStXMUDvZBIoNUXzxQ9aKOf7k33wTDATnWTn6B90mr5Ulvp27DTvbKqK75ER17GLLt6rX9XgPnNAltgwZDZD"
pre = "curl -X POST -H \"Content-Type: application/json\" -d"
fn = "attachment_upload_api.sh"

# create attachment payloads
def generate_upload_payload(url):
    upload_payload = {
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url,
                    "is_reusable": True,
                }
            }
        }
    }
    return upload_payload
al_amaan_pl1 = generate_upload_payload("https://image.ibb.co/kjmYX5/alamaanmenu1.jpg")
al_amaan_pl2 = generate_upload_payload("https://image.ibb.co/kNRaC5/alamaanmenu2.jpg")
generate_json_request(pre, [al_amaan_pl1, al_amaan_pl2], fn, message_attachments_url)

# Add permission:  (https://askubuntu.com/questions/38661/how-do-i-run-sh-files)
# chmod +x ./messenger_settings.sh
# chmod +x ./attachment_upload_api.sh
# ./messenger_settings.sh
# ./attachment_upload_api.sh > al_amaan_img_ids.txt