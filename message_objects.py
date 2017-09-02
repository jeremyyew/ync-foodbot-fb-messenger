import dh_menu_scrape as dh
import message_objects_updated_text as updated_text

# json generators
keywords_desc_list = [
    # (u'\U0001f552', "info", "all opening hours/etc"),
    (u'\U0001f374', "dh", "dining hall menu preview/link"),
    (u'\U0001f354', "buttery", "opening hours, menus/order form links"),
    (u'\U0001f35b', "amaan", "Al Amaan menu/hotline"),
    (u'\U0001F35F', "macs", "Macs menu/hotline/online order"),
    (u'\u2615', "agora", "cafe opening hours/menu"),
    (u'\u2668', "utown", "Utown F&B outlets")
    # (u'\U0001f6b2', "explore", "places near campus to visit")
    # ("brewhouse", "Brewhouse pop-up times/locations.")
]

def generate_keywords_desc_text():
    keywords_desc_text = ""
    for emoji, keyword, desc in keywords_desc_list:
        keywords_desc_text += ("%s \'%s\' --- %s\n" % (emoji, keyword, desc))
    return keywords_desc_text


quick_replies_list = [
    # ("info", "INFO_PB"),
    (u'\U0001f374' + "dh", "DH_PB"),
    (u'\U0001f354' + "buttery", "BUTTERY_PB"),
    (u'\U0001f35b' + "amaan", "AMAAN_PB"),
    (u'\U0001F35F' + "macs", "MACS_PB"),
    (u'\u2615' + "agora", "AGORA_PB"),
    (u'\u2668' + "utown", "UTOWN_PB"),
    (u'\U0001f4af' + "get all", "GET_ALL_PB"),
    # ("explore", "EXPLORE_PB"),
    (u'\u2764\ufe0f' + "share", "SHARE_PB"),
    (u'\u2753' + "help", "HELP_PB"),
    (u'\U0001f4ac' + "feedback", "FEEDBACK_PB"),
]


def generate_quick_replies():
    quick_replies_json = []
    for title, payload in quick_replies_list:
        quick_replies_json.append(
            {"content_type": "text",
             "title": title,
             "payload": payload})
    return quick_replies_json


quick_replies_json = generate_quick_replies()


def add_quick_reply(msg):
    msg.update({"quick_replies": quick_replies_json})
    return msg


# CAROUSEL and BUTTON GENERATOR
def generate_carousel_msg(elements):
    carousel_msg = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "image_aspect_ratio": "horizontal",
                "elements": elements
            }
        }
    }
    return carousel_msg


def generate_carousel_element(title, image_url, subtitle, default_url, buttons):
    return {
        "title": title,
        "image_url": image_url,
        "subtitle": subtitle,
        "default_action": {
            "type": "web_url",
            "url": default_url
        },
        "buttons": buttons
    }


def generate_buttons_msg(text, buttons):
    if buttons == []:
        return {"text": text}
    else:
        return {'attachment': {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": text,
                "buttons": buttons
            }
        }}


# GET_STARTED_PB
from message_objects_updated_text import welcome_msg_text, share_msg_text, share_msg_subtitle_text

welcome_msg = add_quick_reply({'attachment': {
    "type": "template",
    "payload": {
        "template_type": "button",
        "text": (
            welcome_msg_text
        ),
        "buttons": [
            {"type": "element_share",
             "share_contents": {
                 "attachment": {
                     "type": "template",
                     "payload": {
                         "template_type": "generic",
                         "elements": [
                             {
                                 "title": share_msg_text,
                                 "subtitle": (
                                     share_msg_subtitle_text),
                                 "image_url": "https://image.ibb.co/d03JQQ/YNCFoodbotlogo2.png",
                                 "default_action": {
                                     "type": "web_url",
                                     "url": "http://m.me/979027202238929"
                                 },
                                 "buttons": [
                                     {
                                         "type": "web_url",
                                         "url": "http://m.me/979027202238929",
                                         "title": "Try it out"
                                     }
                                 ]
                             }
                         ]
                     }
                 }
             }
             },
            {
                "type": "postback",
                "title": "feedback",
                "payload": "FEEDBACK_PB"
            },
        ]
    }
}})
start_msg = add_quick_reply({
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": (
                "Try typing/selecting these keywords:\n" + generate_keywords_desc_text()
            ),
            "buttons": [
                {"type": "postback",
                 "title": "Get All",
                 "payload": "GET_ALL_PB"},
            ]
        }
    }})

# FEEDBACK_PB
feedback_prompt_msg = add_quick_reply({
                                          "text": "Simply include the tag #feedback directly in your feedback message. If reporting a bug, please try to be as specific as possible. You can also hit me up at m.me/jeremy.yew.9.\n\n"})
feedback_received_msg = add_quick_reply({"text": "Feedback received, thanks! I'll work on it."})

# DH_PB
from message_objects_updated_text import dh_info_msg_text

dh_buttons = [
    {"type": "web_url",
     "title": "View menu",
     "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"},
]
dh_info_msg = add_quick_reply({"text": dh_info_msg_text
                               })
dh_carousel = generate_carousel_element(title="Dining Hall", image_url="https://image.ibb.co/iwb5fv/dining_hall_1.jpg",
                                        subtitle=dh_info_msg_text,
                                        default_url="https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                                        buttons=dh_buttons)


def generate_dh_menu_msg():
    meal, heading, items = dh.scrape("dh")
    msg_string = ""
    msg_string += "Today's %s for %s: \n" % (heading, meal)
    if items == []:
        msg_string += "(preview not available)"
    else:
        for item in items:
            msg_string += "-" + item + "\n"
    msg = generate_buttons_msg(msg_string, dh_buttons)
    return add_quick_reply(msg)


# BUTTERY_PB
from message_objects_updated_text import buttery_msg_text
buttery_buttons = [
    {
        "type": "web_url",
        "url": "https://docs.google.com/forms/d/e/1FAIpQLSeZncU9zU9mYWr3o_N8syDljmsRSSM_VzH536CeC9eg1b2csg/viewform",
        "title": "Nest Order Form"
    },
    {
        "type": "postback",
        "payload": "COMING_SOON_PB",
        "title": "Shiner's Diner Menu"
    },
    {
        "type": "postback",
        "payload": "COMING_SOON_PB",
        "title": "Shiok Shack Menu"
    }
]
buttery_msg = add_quick_reply(generate_buttons_msg(
    text=buttery_msg_text, buttons=buttery_buttons))
buttery_carousel = generate_carousel_element(title="Butteries",
                                             image_url="https://image.ibb.co/cgEVDF/12003252_488018108046512_3022481886860987112_n.jpg",
                                             subtitle=buttery_msg_text,
                                             default_url="https://docs.google.com/forms/d/e/1FAIpQLSeZncU9zU9mYWr3o_N8syDljmsRSSM_VzH536CeC9eg1b2csg/viewform",
                                             buttons=buttery_buttons)

# AMAAN_PB
amaan_msg_text = u'\U0001f35b ' + "Al Amaan Delivery: +67770555 (Open 11AM-3AM)\n"
amaan_buttons = [{
    "type": "phone_number",
    "title": "Call now",
    "payload": "+6567770555"
}, {
    "type": "postback",
    "title": "Get Menu",
    "payload": "AMAAN_MENU_PB"
},
    {
        "type": "web_url",
        "title": "Location",
        "url": "https://goo.gl/maps/fRyaBEeCx172"
    }
]
amaan_msg = add_quick_reply(generate_buttons_msg(amaan_msg_text, amaan_buttons))
amaan_menu_image1_msg = add_quick_reply({
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "1033950820079900"  # dining_hall_1.jpg
        }
    }
})
amaan_menu_image2_msg = add_quick_reply({
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "1033950833413232"  # dining_hall_1.jpg
        }
    }
})
amaan_carousel = generate_carousel_element(title="Al Amaan",
                                           image_url="https://static.wixstatic.com/media/7941e9_975d7ae7bd97474bba9ed3657faaea96.jpg/v1/fill/w_1021,h_680,al_c,q_90/7941e9_975d7ae7bd97474bba9ed3657faaea96.webp",
                                           subtitle=amaan_msg_text, default_url="http://www.alamaanrestaurant.com.sg/",
                                           buttons=amaan_buttons)

# MACS_PB

macs_msg_text = u'\U0001F35F ' + "McDelivery: 67773777 (Open 24hrs)\n-Cendana: S138533\n-Elm: S138610\n-Saga: S138609\n"
macs_buttons = [{
    "type": "phone_number",
    "title": "Call now",
    "payload": "+6567773777"
},
    {
        "type": "web_url",
        "url": "https://www.mcdelivery.com.sg/sg/browse/menu.html",
        "title": "Menu"
    },
    {
        "type": "web_url",
        "url": "https://www.mcdelivery.com.sg/sg/guest.html",
        "title": "Order online"
    }]
macs_msg = add_quick_reply(generate_buttons_msg(macs_msg_text, macs_buttons))
macs_carousel = generate_carousel_element(title="McDonald's",
                                          image_url="https://image.ibb.co/kwM6Ga/macs.png",
                                          subtitle=macs_msg_text,
                                          default_url="https://www.mcdelivery.com.sg/sg/browse/menu.html",
                                          buttons=macs_buttons)

# AGORA_PB
from message_objects_updated_text import agora_msg_text

agora_buttons = [{"type": "postback", "title": "Grab & Go Menu", "payload": "AGORA_MENU_PB"}]
agora_msg = add_quick_reply(generate_buttons_msg(agora_msg_text, []))
agora_carousel = generate_carousel_element(title="Agora Cafe", image_url="https://image.ibb.co/kk059v/agora1.jpg",
                                           subtitle=agora_msg_text,
                                           default_url="https://studentlife.yale-nus.edu.sg/dining-experience/operating-hours/",
                                           buttons=agora_buttons)


def generate_agora_menu_msg():
    meal, heading, items = dh.scrape("agora")
    msg_string = ""
    msg_string += "Today's Grab & Go Lunch: \n"
    if items == []:
        msg_string += "(preview not available)"
    else:
        for item in items:
            msg_string += item + "\n"
    msg = generate_buttons_msg(msg_string, dh_buttons)
    return add_quick_reply(msg)


# UTOWN_PB
utown_msg_text = u'\u2668 ' + "Utown Foodcourts: \n-Koufu Foodcourt: Mon-Fri 7am- 10pm, Sat-Sun 10am-10pm\n-Flavours@Utown: Everyday 7.30am-10pm\n"
utown_buttons = [{
    "type": "web_url",
    "url": "http://www.nus.edu.sg/oca/Retail-And-Dining/Food-and-Beverages.html",
    "title": "View More"
}]
utown_msg = add_quick_reply(generate_buttons_msg(utown_msg_text, utown_buttons))
utown_carousel = generate_carousel_element(title="UTown F&B Outlets", image_url="https://image.ibb.co/dgqYwa/Utown.jpg",
                                           subtitle=utown_msg_text,
                                           default_url="http://www.nus.edu.sg/oca/Retail-And-Dining/Food-and-Beverages.html",
                                           buttons=utown_buttons)

# EXPLORE_PB
explore_msg_text = "Check out these cool places near campus!"
explore_buttons = [{
    "type": "postback",
    "title": "Explore",
    "payload": "EXPLORE_PB"
}]
explore_msg = add_quick_reply(generate_buttons_msg(explore_msg_text, []))
explore_carousel = generate_carousel_element(title="Explore", image_url="", subtitle=explore_msg_text,
                                             default_url="https://studentlife.yale-nus.edu.sg/dining-experience/operating-hours/",
                                             buttons=explore_buttons)


# EXPLORE_PB - explore places
def generate_review_msgs(reviews):
    for review in reviews:
        yield add_quick_reply({"text": review})


pipe_district_url = "http://www.thepipedistrict.com/#aboutPage"
pipe_district_reviews = ["http://danielfooddiary.com/2016/02/17/thepipedistrict/",
                         "https://www.burpple.com/the-pipe-district"]
pipe_district_loc = "https://goo.gl/maps/R85eSuf8xnL2"
pipe_district_buttons = [{"type": "web_url", "url": pipe_district_url, "title": "Website"},
                         {"type": "postback", "payload": "EXPLORE_REVIEWS_PB", "title": "Reviews"},
                         {"type": "web_url", "url": pipe_district_loc, "title": "Directions"}]
pipe_district_carousel1 = generate_carousel_element(title="Pipe District",
                                                    image_url="https://image.ibb.co/gdPHjk/pipedistrict1.jpg",
                                                    subtitle="Pipe-themed restaurant in Science Park.",
                                                    default_url=pipe_district_url, buttons=pipe_district_buttons)
pipe_district_review_msgs = generate_review_msgs(pipe_district_reviews)

pipe_district_carousel2 = pipe_district_carousel1
explore_places_list = [pipe_district_carousel1, pipe_district_carousel2]
explore_places_carousel_msg = add_quick_reply(generate_carousel_msg(explore_places_list))

# GET_ALL_MSG
def generate_get_all_text(texts):
    get_all_text = ""
    for text in texts:
        get_all_text += text + "\n"
    return get_all_text

all_texts = [dh_info_msg_text, buttery_msg_text, amaan_msg_text, macs_msg_text, agora_msg_text, utown_msg_text]

get_all_text = generate_get_all_text(all_texts)
get_all_buttons = []
get_all_text_msg = add_quick_reply(generate_buttons_msg(get_all_text, get_all_buttons))

get_all_carousels_list = [
    dh_carousel,
    buttery_carousel,
    amaan_carousel,
    macs_carousel,
    agora_carousel,
    utown_carousel
    # explore_carousel
]
get_all_carousel_msg = add_quick_reply(generate_carousel_msg(get_all_carousels_list))

# MISC
coming_soon_msg = add_quick_reply({"text": "Coming soon!"})
sorry_msg = add_quick_reply({'attachment': {
    "type": "template",
    "payload": {
        "template_type": "button",
        "text": "Sorry, I don't understand. Type or tap \"help\" to show list of commands.",
        "buttons": [{"type": "postback",
                     "title": "help",
                     "payload": "HELP_PB"}
                    ]
    }
}})

# UNUSED
list_main = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "list",
            "top_element_style": "compact",
            "elements": [
                {
                    "title": "Classic White T-Shirt",
                    "image_url": "https://peterssendreceiveapp.ngrok.io/img/white-t-shirt.png",
                    "subtitle": "100% Cotton, 200% Comfortable",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=100",
                        "webview_height_ratio": "tall"
                    },
                    "buttons": [
                        {
                            "title": "Buy",
                            "type": "web_url",
                            "url": "https://peterssendreceiveapp.ngrok.io/shop?item=100",
                            "webview_height_ratio": "tall"
                        }
                    ]
                },
                {
                    "title": "Classic Blue T-Shirt",
                    "image_url": "https://peterssendreceiveapp.ngrok.io/img/blue-t-shirt.png",
                    "subtitle": "100% Cotton, 200% Comfortable",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=101",
                        "webview_height_ratio": "tall"
                    },
                    "buttons": [
                        {
                            "title": "Buy",
                            "type": "web_url",
                            "url": "https://peterssendreceiveapp.ngrok.io/shop?item=101",
                            "webview_height_ratio": "tall"
                        }
                    ]
                },
                {
                    "title": "Classic Black T-Shirt",
                    "image_url": "https://peterssendreceiveapp.ngrok.io/img/black-t-shirt.png",
                    "subtitle": "100% Cotton, 200% Comfortable",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=102",
                        "webview_height_ratio": "tall"
                    },
                    "buttons": [
                        {
                            "title": "Buy",
                            "type": "web_url",
                            "url": "https://peterssendreceiveapp.ngrok.io/shop?item=102",
                            "webview_height_ratio": "tall"
                        }
                    ]
                },
                {
                    "title": "Classic Gray T-Shirt",
                    "image_url": "https://peterssendreceiveapp.ngrok.io/img/gray-t-shirt.png",
                    "subtitle": "100% Cotton, 200% Comfortable",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
                        "webview_height_ratio": "tall"
                    },
                    "buttons": [
                        {
                            "title": "Buy",
                            "type": "web_url",
                            "url": "https://peterssendreceiveapp.ngrok.io/shop?item=103",
                            "webview_height_ratio": "tall"
                        }
                    ]
                }
            ],
            "buttons": [
                {
                    "title": "View More",
                    "type": "postback",
                    "payload": "payload"
                }
            ]
        }
    }
}
cendana_buttery_form_submitted_msg = {"text": "Submitted your order to The Nest."}
others_carousel = {
    "title": "Others",
    "image_url": "https://petersfancybrownhats.com/company_image.png",
    "subtitle": "Agora opening hours:\nFoodclique operating hours:\nKoufu operating hours:\nBrinda's operating hours:",
    "default_action": {
        "type": "web_url",
        "url": "https://docs.google.com/forms/d/e/1FAIpQLSeZncU9zU9mYWr3o_N8syDljmsRSSM_VzH536CeC9eg1b2csg/viewform"
    },
    "buttons": [
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Call Brinda's now"
        },
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Brinda's menu"
        },
        {
            "type": "web_url",
            "url": "http://www.nus.edu.sg/oca/Retail-And-Dining/Food-and-Beverages.html",
            "title": "UTown F&B"
        }
    ]
}
slow_msg = {"text": "Hang on, this might take a second..."}
