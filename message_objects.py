welcome_msg = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": (
                "Welcome to the Yale-NUS Foodbot! "
                "Please be patient if you encounter any bugs, I'm still figuring this out. "
                "Feel free to share this if you find it useful, and let me know if you have any suggestions!\n\n"
                "Regards,\nJeremy"
            ),
            "buttons": [
                {"type": "postback",
                 "title": "Share",
                 "payload": "GET_STARTED_PB"},
                {"type": "postback",
                 "title": "Feedback",
                 "payload": "GET_STARTED_PB"},
            ]
        }
    }
}

options_msg = {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": (
                "What would you like to do?\n"
                "PS: You can type these options to access them at any time, e.g. 'info'."
            ),
            "buttons": [
                {"type": "postback",
                 "title": "INFO",
                 "payload": "QUICK_REF_PB"},
                {"type": "postback",
                 "title": "INTERACT",
                 "payload": "CAROUSEL_PB"},
                {"type": "postback",
                 "title": "EXPLORE",
                 "payload": "EXPLORE_PB"}
            ]
        }
    }
}

explore_msg = {"text": "Feature coming soon."}

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

quick_reply_main =  {
    "attachment": {
        "type": "template",
        "payload": {
            "template_type": "button",
            "text": "What are you thinking of?",
            "buttons": [
                {"type": "postback",
                 "title": "See options again",
                 "payload": "QUICK_REPLY_MAIN_PB"
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

send_img = {
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "992857737522542" #dining_hall_1.jpg
        }
    }
}

dining_hall_carousel={
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
butteries_carousel={
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

al_amaan_carousel={
    "title": "Al Amaan",
    "image_url": "https://static.wixstatic.com/media/7941e9_975d7ae7bd97474bba9ed3657faaea96.jpg/v1/fill/w_1021,h_680,al_c,q_90/7941e9_975d7ae7bd97474bba9ed3657faaea96.webp",
    "subtitle": "Delivery: 67770555 (11AM-3AM)",
    "default_action": {
        "type": "web_url",
        "url": "http://www.alamaanrestaurant.com.sg/"
    },
    "buttons": [
        {
            "type": "phone_number",
            "title": "Call now",
            "payload": "+6567770555"
        },
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Menu"
        }

    ]
}

macs_carousel={
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

others_carousel={
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

carousel_main = {
    "attachment":{
        "type":"template",
        "payload":{
            "template_type":"generic",
            "image_aspect_ratio": "horizontal",
            "elements":[
                dining_hall_carousel,
                butteries_carousel,
                al_amaan_carousel,
                macs_carousel,
                others_carousel
            ]
        }
    }
}
