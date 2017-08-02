import time
import message_objects as msg
import requests
import json
import YNCFoodbotserver as yncfbserver

def match_text_or_payload(input, sender_id):
    # IF RECOGNIZED TEXT MSG/POSTBACK:
    def input_contains(keys):
        return any(key in input for key in keys)

    if input_contains(["Get Started", "start", "GET_ STARTED_PB"]):
        yield msg.welcome_msg
        time.sleep(1)
        send_typing_msg(sender_id)
        time.sleep(1)
        yield msg.start_msg

    #elif input_contains(["info", "INFO_PB"]):
        #yield msg.info_msg

    elif input_contains(["dh", "DH_PB"]):
        yield msg.dh_info_msg
        yield msg.generate_dh_menu_msg()

    elif input_contains(["buttery", "BUTTERY_PB"]):
        yield msg.buttery_msg

    elif input_contains(["amaan", "AMAAN_PB"]):
        yield msg.amaan_msg

    elif input_contains(["AMAAN_MENU_PB"]):
        yield msg.amaan_menu_image1_msg
        yield msg.amaan_menu_image2_msg

    elif input_contains(["macs", "MACS_PB"]):
        yield msg.macs_msg

    elif input_contains(["agora", "AGORA_PB"]):
        yield msg.agora_msg

    elif input_contains(["utown", "UTOWN_PB"]):
        yield msg.utown_msg

    #elif input_contains(["explore", "EXPLORE_PB"]):
    #     yield msg.explore_msg
    #    yield msg.explore_places_carousel_msg

    elif input_contains(["help", "HELP_PB"]):
        yield msg.start_msg

    elif input_contains(["#feedback"]):
        yield msg.feedback_received_msg

    elif input_contains(["FEEDBACK_PB", "feedback"]):
        yield msg.feedback_prompt_msg

    elif input_contains(["get all", "GET_ALL_PB"]):
        yield msg.get_all_text_msg
        time.sleep(1)
        send_typing_msg(sender_id)
        yield msg.get_all_carousel_msg
        """yield msg.slow_msg
        yield msg.dh_info_msg
        yield msg.generate_dh_menu_msg()
        yield msg.buttery_msg
        yield msg.amaan_msg
        yield msg.macs_msg
        yield msg.agora_msg
        yield msg.utown_msg"""

    #elif input_contains(["EXPLORE_REVIEWS_PB"]):
    #    for review in msg.pipe_district_review_msgs:
    #        yield review

    elif input_contains(["COMING_SOON_PB"]):
        yield msg.coming_soon_msg

    elif input_contains(["list"]):
        yield msg.list_main

    # ELSE (NOT RECOGNIZED text or postback: ):
    else:
        print "ERROR: not recognized text or postback"
        yield msg.sorry_msg

        # elif "CENDANA_BUTTERY_ORDER_PB" in event["postback"]["payload"]:
        # gform.post_form()
        # yield msg.cendana_buttery_form_submitted_msg


def send_typing_msg(recipient):
    """Send the message text to recipient with id recipient."""

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": yncfbserver.PAT},
                      data=json.dumps({
                          "recipient": {"id": recipient},
                          "sender_action": "typing_on"
                      }),
                      headers={'Content-type': 'application/json'})
    print "REQUEST: ", r.text
    if r.status_code != requests.codes.ok:
        print r.text

