import dh_menu_scrape as dh

# json generators
keywords_desc_list = [
    (u'\U0001f552', "info", "All opening days/hours, etc."),
    (u'\U0001F35F', "dh", "Dining hall menu link & preview."),
    (u'\U0001F35F', "buttery", "Opening days/hours, menu, order form links."),
    (u'\U0001F35F', "amaan", "Al Amaan menu & hotline."),
    (u'\U0001F35F', "macs", "Macs menu, hotline, & online order."),
    (u'\u2615', "agora", "Opening hours & menu."),
    (u'\U0001F35F', "utown", "Utown F&B outlets link."),
    (u'\U0001F35F', "explore", "Places near campus to visit!")
    # ("brewhouse", "Brewhouse pop-up times/locations.")
]


def generate_keywords_desc_text():
    keywords_desc_text = ""
    for emoji, keyword, desc in keywords_desc_list:
        keywords_desc_text += ("%s \'%s\'  --  %s\n" % (emoji, keyword, desc))
    return keywords_desc_text


quick_replies_list = [
    ("info", "GET_INFO_PB"),
    ("dh", "DH_MENU_PB"),
    ("buttery", "COMING_SOON_PB"),
    ("amaan", "AL_AMAAN_PB"),
    ("macs", "COMING_SOON_PB"),
    ("agora", "COMING_SOON_PB"),
    ("utown", "COMING_SOON_PB"),
    ("explore", "COMING_SOON_PB"),
    ("help", "COMING_SOON_PB"),
    ("feedback", "FEEDBACK_PB"),
]


def generate_quick_replies():
    quick_replies_json = []
    for title, payload in quick_replies_list:
        quick_replies_json.append(
            {"content_type": "text",
             "title": title,
             "payload": payload})
    return quick_replies_json


# GET_STARTED_PB
welcome_msg = {'attachment': {
    "type": "template",
    "payload": {
        "template_type": "button",
        "text": (
            "Welcome to the Yale-NUS Foodbot!\n"
            "Feel free to share if you find it useful " + u'\U0001f60e'
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
                                 "title": "Hungry? I gotchu fam.",
                                 "subtitle": (
                                     "Quick access to buttery order forms, dining hall menu, delivery hotlines, and more!"),
                                 "image_url": "https://bot.peters-hats.com/img/hats/fez.jpg",
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
                "title": "Feedback",
                "payload": "FEEDBACK_PB"
            },
        ]
    }
}}
start_msg = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": (
                "Try typing these commands!\n\n" + generate_keywords_desc_text()
            ),
            "buttons": [
                {"type": "postback",
                 "title": "Get All",
                 "payload": "GET_ALL_PB"},
            ]
        }
    },
    "quick_replies": generate_quick_replies()
}

# FEEDBACK_PB
feedback_prompt_msg = {"text": "You can send any suggestions, feedback or bug reports directly to the bot. "
                               "Simply include the tag #feedback in your message to make sure I see it. "
                               "If reporting a bug, please try to be as specific as possible. "
                               "You can also hit me up at m.me/jeremy.yew.9.\n\n"}
feedback_received_msg = {"text": "Got it, thanks! I'll work on it."}

# GET_INFO_PB
quick_ref_main = {"text": (
    "Dining Hall:\n"
    "Weekdays: 730-930am, 1130-130pm, 6-830pm\n"
    "Weekends: 10am-1pm, 6-830pm\n"
    "Green & Healthy Lunches: Mon (Elm), Wed (Cen), Fri (Saga)\n\n"

    "Butteries:\n"
    "The Nest: Sat/Sun/Mon, 10-12pm\n"
    "Shiner's Diner: Fri/Sun/Mon, 830-12pm\n"
    "Shiok Shack: Tue/Thur, 9-12pm, Wed 10-11pm\n\n"

    "Agora Opening Hours: Mon-Fri 8am-6pm, Sat 9am-3pm\n"
    "Grab N' Go Lunch: TBC\n\n"

    "Al Amaan's Delivery: 67770555 (11AM-3AM)\n"
    "McDelivery: 67773777 (24hrs)\n\n"

    "RC addresses:\n"
    "Cendana: 28 College Ave West, S138533\n"
    "Elm: 12 College Ave West, S138610\n"
    "Saga: 10 College Ave West, S138609\n"
)
}

# IMG ATTACHMENTS
al_amaan_menu_image1_msg = {
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "1033950820079900"  # dining_hall_1.jpg
        }
    }
}
al_amaan_menu_image2_msg = {
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "1033950833413232"  # dining_hall_1.jpg
        }
    }
}

# CAROUSEL
dining_hall_carousel = {
    "title": "Dining Hall",
    "image_url": "https://image.ibb.co/iwb5fv/dining_hall_1.jpg",
    "subtitle": ("Dining Hall:\n"
                 "Weekdays: 730-930am, 1130-130pm, 6-830pm\n"
                 "Weekends: 10am-1pm, 6-830pm\n"
                 "Green & Healthy Lunches: Mon (Elm), Wed (Cen), Fri (Saga)"),
    "default_action": {
        "type": "web_url",
        "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
    },
    "buttons": [
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "MENU"
        }
    ]
}
butteries_carousel = {
    "title": "Butteries",
    "image_url": "https://image.ibb.co/cgEVDF/12003252_488018108046512_3022481886860987112_n.jpg",
    "subtitle": "Nest: Sat/Sun/Mon 10-12pm\nShiner's: Fri/Sun/Mon 830-12pm\nShiok: Tue/Thur 9-12pm, Wed 10-11pm",
    "default_action": {
        "type": "web_url",
        "url": "https://docs.google.com/forms/d/e/1FAIpQLSeZncU9zU9mYWr3o_N8syDljmsRSSM_VzH536CeC9eg1b2csg/viewform"
    },
    "buttons": [
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "The Nest"
        },
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Shiner's Diner"
        },
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Shiok Shack"
        }
    ]
}
al_amaan_carousel = {'title': "Al Amaan",
                     'image_url': "https://static.wixstatic.com/media/7941e9_975d7ae7bd97474bba9ed3657faaea96.jpg/v1/fill/w_1021,h_680,al_c,q_90/7941e9_975d7ae7bd97474bba9ed3657faaea96.webp",
                     'subtitle': "Delivery: 67770555 (11AM-3AM)", 'default_action': {
        "type": "web_url",
        "url": "http://www.alamaanrestaurant.com.sg/"
    }, 'buttons': [
        {
            "type": "phone_number",
            "title": "Call now",
            "payload": "+6567770555"
        },
        {
            "type": "postback",
            "title": "Menu",
            "payload": "AL_AMAAN_MENU_PB"
        }

    ]}
macs_carousel = {
    "title": "McDonald's",
    "image_url": "https://d1nqx6es26drid.cloudfront.net/app/assets/img/logo_mcd.png",
    "subtitle": "Delivery: 67773777 (24hrs)\nCendana: S138533\nElm: S138610\nSaga: S138609",
    "default_action": {
        "type": "web_url",
        "url": "https://www.mcdelivery.com.sg/sg/browse/menu.html"
    },
    "buttons": [
        {
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
        }
    ]
}
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
carousel_main = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "image_aspect_ratio": "horizontal",
            "elements": [
                dining_hall_carousel,
                butteries_carousel,
                al_amaan_carousel,
                macs_carousel,
                others_carousel
            ]
        }
    }
}


# MENU_CHECK_PB
def generate_short_menu_msg():
    meal, heading, items = dh.scrape()

    items_string = ""
    if items == []:
        items_string = "Sorry, menu not available."
    else:
        for item in items:
            items_string += item + "\n"

    full_menu_msg = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": ("%s for %s today:\n%s"
                         % (heading, meal, items_string)
                         ),
                "buttons": [
                    {"type": "web_url",
                     "title": "View menu",
                     "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"},
                ]
            }
        }
    }

    return full_menu_msg


# MISC
coming_soon_msg = {"text": "Feature in development."}
sorry_msg = {"text": "Sorry, I don't understand. Type \"help\" to show list of commands with descriptions.",
             "quick_replies": generate_quick_replies()}

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
