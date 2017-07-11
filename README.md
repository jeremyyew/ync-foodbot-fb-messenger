# YNCFoodbot_Messenger

Still in development. 
Facebook Messenger chatbot that sends information and links about food options around Yale-NUS campus. 
Chat with the bot on messenger at this page: https://www.facebook.com/YNC-Foodbot-979027202238929/ (currently not available as it is has not been published). 

I used https://tsaprailis.com/2016/06/02/How-to-build-and-deploy-a-Facebook-Messenger-bot-with-Python-and-Flask-a-tutorial/ to start. 

Hosted on Heroku. 

## Learning points: 

Through this project (so far), I have learned a little bit about: 

- Facebook messenger API
- HTML requests
- Webscraping with Xpath
- using curl/shell script

## To-do

### Completed Features:
- [ ] Explore food options
    - [ ] Send Al Amaan Menu (+ upload images to FB server)
    - [ ] Edit "Others" carousel
    - [ ] Add "Share" image.
    - [ ] "Feedback" button text.
    - [ ] Add Buttery links.
- [X] Share
- [ ] Feedback
    - [ ] Link to send message to Jeremy?

11/7 Tuesday:
- [ ]Send webscraped dining hall menu content
    - [X] refactor call to scrape in supperbotserver
    - [X] xpath by special
    - [X] xpath by meal
    - [ ] xpath by day/tab rel
    - [ ] refactor call to scrape to get meal and special
    - [ ] set mealtime conditions by half-hour instead of hour, set separate for wknds (brunch)
    - [X] set default specials

-[ ] Features to explore:
    - [ ] NLP interaction ("Order buttery food")
    - [ ] Notification subscription ("What's cookin'?")
    - [ ] More content ("Discover new food places"). Find a food blogger.

#### Interfaces implemented:

- [X] Get Started message
- [X] Share Button
- [X] Carousel messages
- [X] Persistent menu

#### Interfaces tried:
- [X] Lists and Quick Replies

### Deployment:

14/7 Friday:
- [ ] ***Check FB review requirements, send for review

### When school reopens (10/8):

- [ ] update buttery opening timings
- [ ] update webscraper day tabs
- [ ] update copy (e.g. share message)
- [ ] delete false links
- [ ] re-publish, test group

### Other chatbot ideas:
- [ ] YNC general info, memes/comics subscription 


