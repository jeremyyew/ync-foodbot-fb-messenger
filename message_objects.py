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

send_img = {
    "attachment": {
        "type": "image",
        "payload": {
            "attachment_id": "992857737522542" #dining_hall_1.jpg
        }
    }
}

dining_hall_carousel = {
    "title": "Dining Hall",
    "image_url": "https://image.ibb.co/iwb5fv/dining_hall_1.jpg", #dining_hall_1.jpg
    "subtitle":"Weekdays: 730-930am/1130-130pm/6-830pm\nWeekends: 10AM-1pm/6-830pm\nGreen Days: TBC",
    "default_action": {
        "type": "web_url",
        "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
    },
    "buttons": [
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Today's Menu"
        },
        {
            "type": "web_url",
            "url": "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/",
            "title": "Veg days"
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
