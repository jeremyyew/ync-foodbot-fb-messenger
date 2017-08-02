# YNCFoodbot_Messenger
Still in development.
Facebook Messenger chatbot that sends information and links about food options around Yale-NUS campus. 
Chat with the bot on messenger at this page: https://www.facebook.com/YNC-Foodbot-979027202238929/ (currently not available as it is has not been published). 

I used https://tsaprailis.com/2016/06/02/How-to-build-and-deploy-a-Facebook-Messenger-bot-with-Python-and-Flask-a-tutorial/ to start. 

Hosted on Heroku. 

## Learning points:

- Facebook messenger API
- HTML requests
- Xml object parsing with Xpath
- git markdown
- gitignore
- git branching

## To-do To-day
**2/8 Mon**
- [X] Add location to amaan_buttons
- [X] Remove explore
- [ ] Remove info
- [ ] xpath by day/tab rel

- [ ] add emoji to all msgs
- [ ] Agora img, Utown img, explore img
- [ ] Agora - grab n go scrape
- [ ] Change explore default url

## Must-haves (Before deployment v0.1, 3/8)
- [ ] Notes
- [ ] update buttery opening timings
- [ ] Populate explore button
- [ ] Get rid of all COMING_SOON_PB

## Should-haves (Before release)
- [ ] update webscraper day tabs
- [ ] upload all img to imgbb
- [ ] update copy (e.g. share message)
- [ ] delete false links (if any)
- [ ] Implement Google Form CMS: https://www.drivecms.xyz/#getting-started

## Nice-to-haves
- [ ] case insensitivity
- [ ] coffee stand openings - scrape?
**Features to explore**
- [X] Order buttery food?
- [X] Notification subscriptions?
- [ ] Spoons and Forks link

### Other chatbot ideas:
- [ ] YNC general info, memes/comics subscription
- [ ] receipt scanner/expenses recorder

### Messenger API features explored:
- [X] Get Started message
- [X] Share Button
- [X] Carousel messages
- [X] Persistent menu
- [X] Lists
- [X] Quick Replies

## Completed:

**30/07 Sunday**
- [X] Change coming_soon_msg
- [X] refactor info msg to concat all texts
- [X] Add "Share" image.
- [X] Add quick_replies to everything
- [X] Get Started, GET_ STARTED_PB, start
- [X] info, INFO_PB
- [X] dh, DH_PB
- [X] buttery, BUTTERY_PB
- [X] amaan, AMAAN_PB
- [X] MACS_PB, macs_msg
- [X] AGORA_PB, agora_msg
- [X] UTOWN_PB, utown_msg
- [X] EXPLORE_PB, explore_msg
- [X] "help", "HELP_PB"
- [X] "FEEDBACK_PB", "feedback"
- [X] "#feedback"
- [X] GET_ALL_PB, get_all_msg
- [X] turn typing delay back on

**29/07 Saturday**
- [X] Write instant_test.py
- [X] Refactor match_text_or_payload out into match_text_or_payload.py
- [X] Refactor message_objects: add_quick_reply and generate_carousel_msg
- [X] **Feedback button**
    - [X] #feedback prompt and received message
- [X] Add emoji's to start_msg
- [X] Add help button to sorry_msg

**28/07 Friday**
- [X] Refactor YNCFoodbotserver.py
    - [X] texts
    - [X] postbacks
- [X] Branch keyword_interface:
    - [X] Change start_msg
    - [X] Implement quick_replies
    - [X] Remove persistent menu

**24/07 Monday**
- [X] Reformat daily special message
- [X] Privacy Policy
- [X] App Logo
- [X] Fix typo
- [X] Refactor YNCFoodbotserver.py
- [X] Create test generators

**23/07 Sunday**
- [X] Create messenger api json request generators (for image uploads and settings)
- [X] Send Al Amaan Menu (upload images to FB server)

