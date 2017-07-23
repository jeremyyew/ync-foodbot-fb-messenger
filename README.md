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

## To-do
### Features:
- [ ] **Food carousel**
    - [ ] Send Al Amaan Menu (+ upload images to FB server)
    - [ ] Edit "Others" carousel
    - [ ] Add "Share" image.
    - [ ] Add Buttery links.
    - [ ] Add location?
    - [ ] Separate Brinda's and Utown

- [X] **Share button**
    - [ ] Add Share button to persistent menu

- [ ] **Send webscraped dining hall menu content**
    - [X] refactor call to scrape in supperbotserver
    - [X] xpath by special
    - [X] xpath by meal
    - [X] format items_msg: change call to scrape to get meal and special
    - [X] set heading assignment by min instead of hour
    - [X] set separate meal/heading assignnment for weekends (brunch)
    - [X] set default specials
    - [ ] xpath by day/tab rel
    - [ ] Reformat daily special message


- [X] **Feedback button**
    - [X] #feedback prompt and received message

- [ ] **Misc**
    - [ ] "I don't understand" message
    - [ ] Refactor YNCFoodbotserver.py
    - [ ] Refactor messenger settings
        - [ ] Create request_generator, automate all request generation


- [ ] Other features to explore:
    - [ ] **"Order buttery food"**
    - [ ] **Notification subscription ("What's cookin'?")**
    - [ ] **"Discover new food places")**


### Deployment: 24/7 Sat
- [ ] **Check FB review requirements, send for review**

### When school reopens (10/8):

- [ ] update buttery opening timings
- [ ] update webscraper day tabs
- [ ] update copy (e.g. share message)
- [ ] delete false links
- [ ] re-publish, test group

### Other chatbot ideas:
- [ ] YNC general info, memes/comics subscription
- [ ] receipt scanner/expenses recorder

#### Messenger API features implemented:
- [X] Get Started message
- [X] Share Button
- [X] Carousel messages
- [X] Persistent menu

#### Messenger API features tried:
- [X] Lists and Quick Replies
