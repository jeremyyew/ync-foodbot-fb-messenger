get_started = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": "Pick a dining option:",
            "buttons": [
                {"type": "web_url",
                 "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                 "title": "Dining Hall"},
                {"type": "web_url",
                 "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                 "title": "Other Campus Options"},
                {"type": "web_url",
                 "url": "https://studentlife.yale-nus.edu.sg/dining-experience/operating-hours/",
                 "title": "Order In"}
            ]
        }
    }
}


quick_reply_main =  {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": "What are you thinking of?",
            "buttons": [
                {"type": "postback",
                 "title": "See options again",
                 "payload": "quick_reply_main_pb"
                 }
            ]
        }
    },
    "quick_replies":[
        {
            "content_type":"text",
            "title":"dining hall",
            "payload":"dining_hall_pb"
        },
        {
            "content_type":"text",
            "title":"buttery",
            "payload":"buttery_pb"
        },
        {
            "content_type": "text",
            "title": "al amaan",
            "payload": "al_amaan_pb"
        },
        {
            "content_type": "text",
            "title": "macs",
            "payload": "macs_pb"
        },
        {
            "content_type": "text",
            "title": "others",
            "payload": "others_pb"
        }
    ]
}

carousel_main = {
    "attachment":{
        "type":"template",
        "payload":{
            "template_type":"generic",
            "elements":[
                {
                    "title":"Dining Hall",
                    "image_url":"https://petersfancybrownhats.com/company_image.png",
                    "subtitle":"Dining Hall operating hours:\n hi",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                        "messenger_extensions": True,
                        "webview_height_ratio": "tall",
                        "fallback_url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
                    },
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                            "title":"View menu"
                        }
                    ]
                },
                {
                    "title": "Butteries",
                    "image_url": "https://petersfancybrownhats.com/company_image.png",
                    "subtitle": "Buttery operating hours:\n hi",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://docs.google.com/forms/d/e/1FAIpQLSeZncU9zU9mYWr3o_N8syDljmsRSSM_VzH536CeC9eg1b2csg/viewform",
                        "messenger_extensions": True,
                        "webview_height_ratio": "tall",
                        "fallback_url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                            "title": "The Nest menu/order form"
                        },
                        {
                            "type": "web_url",
                            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                            "title": "Shiner's Diner menu/order form"
                        },
                        {
                            "type": "web_url",
                            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
                            "title": "Shiok Shack menu/order form"
                        }
                    ]
                }
            ]
        }
    }
}