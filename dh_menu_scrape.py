from lxml import html
import requests
import datetime

url = "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}



def scrape():

    #get xpath object from dh html
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)

    # get current day and hour
    now = datetime.datetime.now()
    day = now.strftime('%A')
    hour = now.hour

    # set column to check depending on day
    if day == "Monday":
        tab = "tab8"
    elif day == "Friday":
        tab = "tab5"
    elif day == "Tuesday":
        tab = "tab5"
    elif day == "Today":
        tab = "tab_na"


    # set meal based on hour
    if 0 <= hour <= 10:
        meal = "breakfast"
    if 11 <= hour <= 13:
        meal = "lunch"
    if 14 <= hour <= 23:
        meal = "dinner"

    # set heading based on meal
    if meal == "breakfast":
        heading = "Live Station"
    elif meal == "dinner" or meal == "lunch":
        heading = "Daily Special"


    xpath_string2 = ('//*[@id="%s"]' #get id = <tab> #todo: make id = day
                    '//span[contains(text(), "%s")]' #get span that contains <meal> 
                    '/..' #parent of <span> is <h4> ], goes back to <p> level 
                    '/following-sibling::p/strong/u[contains(text(), "%s")]' #get following header that contains <heading> 
                    '/../..' #grandparent of <p>/<strong>/<u> is <p>
                    '/following-sibling::p' #all p's following <header> (NOT p/strong/u)
                    '[' #where 
                    'count' #number of
                    '(preceding-sibling::p/strong/u)' #preceding headers 
                    '=' #equals to 
                    'count' #number of preceding headers before <heading> + 1. Logic: p's before and after will have diff number of preceding headers. 
                    '(//*[@id="%s"]' 
                    '//span[contains(text(), "%s")]' 
                    '/..' 
                    '/following-sibling::p/strong/u[contains(text(), "%s")]'
                    '/../..' 
                    '/preceding-sibling::p/strong/u)'
                    '+ 1'
                    ']'
                    '/text()' #get text of these <p>'s
                     % (tab, meal, heading, tab, meal, heading))

    items = tree.xpath(xpath_string2)

    if u'\xa0' in items:
        items.remove(u'\xa0')

    print ("TESTING....DAY: %s, MEAL: %s, HOUR:%s, HEADING: %s, ITEMS: %s" % (day, meal, hour, heading, items))
    return meal, heading, items


