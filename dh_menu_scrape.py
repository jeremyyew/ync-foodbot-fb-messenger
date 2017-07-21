from lxml import html
import requests
import datetime

url = "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# construct time objects
t0000 = datetime.time(0, 0)
t0930 = datetime.time(9, 30)
t1300 = datetime.time(13, 00)
t1330 = datetime.time(13, 30)
t2359 = datetime.time(23, 59, 59)
print t0000, t0930, t1330, t2359


def scrape():
    # get xpath object from dh html
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)

    # get current day and hour
    now = datetime.datetime.now()
    day = now.strftime('%A')
    now_time = now.time()

    # testing:
    day = "Saturday"

    # set tab column to check depending on day
    tab = ""
    if day == "Monday":
        tab = "tab8"
    elif day == "Tuesday":
        tab = "tab_na"
    elif day == "Wednesday":
        tab = "tab_na"
    elif day == "Thursday":
        tab = "tab4"
    elif day == "Friday":
        tab = "tab5"
    elif day == "Saturday":
        tab = "tab6"
    elif day == "Sunday":
        tab = "tab7"
    else:
        print "tab assignment error: day unmatched"

    # set meal depending on day and time
    meal = ""
    heading = ""
    if day == "Saturday" or day == "Sunday":
        if now_time >= t0000 and now_time <= t1300:
            meal = "brunch"
        elif now_time >= t1300 and now_time <= t2359:
            meal = "dinner"
        else:
            print "meal assignment error: now_time unmatched"
    elif day in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}:
        if now_time >= t0000 and now_time <= t0930:
            meal = "breakfast"
        elif now_time >= t0930 and now_time <= t1330:
            meal = "lunch"
        elif now_time >= t1330 and now_time <= t2359:
            meal = "dinner"
        else:
            print "meal assignment error: now_time unmatched"
    else:
        print "meal assignment error: day unmatched"

    # set heading based on meal
    if meal == "breakfast":
        heading = "Live Station"
    elif meal == "brunch":
        heading = "Daily Special"
    elif meal == "lunch":
        heading = "Daily Special"
    elif meal == "dinner":
        heading = "Daily Special"
    else:
        print "heading assignment error: meal unmatched"

    xpath_by_heading = ('//*[@id="%s"]'  # get id = <tab> #todo: make id = day
                     '//span[contains(text(), "%s")]'  # get span that contains <meal> 
                     '/..'  # parent of <span> is <h4> ], goes back to <p> level 
                     '/following-sibling::p/strong/u[contains(text(), "%s")]'  # get following header that contains <heading> 
                     '/../..'  # grandparent of <p>/<strong>/<u> is <p>
                     '/following-sibling::p'  # all p's following <header> (NOT p/strong/u)
                     '['  # where 
                     'count'  # number of
                     '(preceding-sibling::p/strong/u)'  # preceding headers 
                     '='  # equals to 
                     'count'  # number of preceding headers before <heading> + 1. Logic: p's before and after will have diff number of preceding headers. 
                     '(//*[@id="%s"]'
                     '//span[contains(text(), "%s")]'
                     '/..'
                     '/following-sibling::p/strong/u[contains(text(), "%s")]'
                     '/../..'
                     '/preceding-sibling::p/strong/u)'
                     '+ 1'
                     ']'
                     '/text()'  # get text of these <p>'s
                     % (tab, meal, heading, tab, meal, heading))

    xpath_by_station = ('//*[@id="%s"]'  # get id = <tab> #todo: make id = day
                     '//span[contains(text(), "%s")]'  # get span that contains <meal> 
                     '/..'  # parent of <span> is <h4> ], goes back to <p> level 
                     '/following-sibling::p/strong/u[contains(text(), "%s")]'  # get following header that contains <heading> 
                     '/../..'  # grandparent of <p>/<strong>/<u> is <p>
                     '/following-sibling::p'  # all p's following <header> (NOT p/strong/u)
                     '['  # where 
                     'count'  # number of
                     '(preceding-sibling::p/strong/u)'  # preceding headers 
                     '='  # equals to 
                     'count'  # number of preceding headers before <heading> + 1. Logic: p's before and after will have diff number of preceding headers. 
                     '(//*[@id="%s"]'
                     '//span[contains(text(), "%s")]'
                     '/..'
                     '/following-sibling::p/strong/u[contains(text(), "%s")]'
                     '/../..'
                     '/preceding-sibling::p/strong/u)'
                     '+ 1'
                     ']'
                     '/text()'  # get text of these <p>'s
                     % (tab, meal, "STATION", tab, meal, "STATION"))

    items = tree.xpath(xpath_by_heading)
    if items == []:
        items = tree.xpath(xpath_by_station)

    if u'\xa0' in items:
        items.remove(u'\xa0')
    print ("TESTING....DAY: %s, TIME: %s, TAB: %s, MEAL: %s, HEADING: %s, ITEMS: %s" % (
    day, now_time, tab, meal, heading, items))
    return meal, heading, items