from lxml import html
import requests
import datetime
import time
from settings import *
import pylibmc
# Dependencies:
# Meal timings.
# Spelling of dh menu website of days as "Mon", "Thu", etc.
# tab Today
# names of meals and headers (daily specials, stations)
#cache = pylibmc.Client(["127.0.0.1"], binary=True,
#                    behaviors={"tcp_nodelay": True,
#                               "ketama": True})


url = "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# construct time objects
t0000 = datetime.time(0, 0)
t0930 = datetime.time(9, 30)
t1300 = datetime.time(13, 00)
t1330 = datetime.time(13, 30)
t2359 = datetime.time(23, 59, 59)


def scrape(place):
    # get xpath object from dh html
    #start = time.clock()
    #page = requests.get(url, headers=headers)
    #print("TIME TAKEN FOR REQUEST: ", time.clock() - start)

    def get_page():
        start = time.clock()
        page = cache.get('page')
        if page is None:
            page = requests.get(url, headers=headers)
            cache.set('page', page)
        print("TIME TAKEN FOR CACHE: ", time.clock() - start)
        return page

    page = get_page()
    tree = html.fromstring(page.content)
    # get current day and hour
    now = datetime.datetime.now()
    day = now.strftime('%A')[:3]
    now_time = now.time()


    # set tab column to check depending on day
    tab = ""
    """
    if day == "Mon":
        tab = "tab8"
    elif day == "Tue":
        tab = "tab_na"
    elif day == "Wed":
        tab = "tab_na"
    elif day == "Thu":
        tab = "tab4"
    elif day == "Fri":
        tab = "tab5"
    elif day == "Sat":
        tab = "tab6"
    elif day == "Sun":
        tab = "tab7"
    else:
        print "tab assignment error: day unmatched""
    """

    xpath_by_today = ('//ul[@class="tabs dining"]'  # get ul of class = "tabs dining"
                      '/li[contains(text(), "%s")]'  # get list which contains text "Today" 
                      '/@rel'  # get rel of that list
                      % ("Today"))

    tab = tree.xpath(xpath_by_today)[0]

    if place == "dh":

        # set meal depending on day and time
        meal = ""
        heading = ""
        if day == "Sat" or day == "Sun":
            if now_time >= t0000 and now_time <= t1300:
                meal = "brunch"
            elif now_time >= t1300 and now_time <= t2359:
                meal = "dinner"
            else:
                print "meal assignment error: now_time unmatched"
        elif day in {"Mon", "Tue", "Wed", "Thu", "Fri"}:
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

        xpath_by_station = ('//*[@id="%s"]'  # get id = <tab> 
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
        xpath_by_station_new = ('//*[@id="%s"]'  # get id = <tab> 
                            '//span[contains(text(), "%s")]'  # get span that contains <meal> 
                            '/..'  # parent of <span> is <h4> ], goes back to <p> level 
                            '/following-sibling::p/strong/u[contains(text(), "%s")]'  # get following header that contains <heading> 
                            '/../..'  # grandparent of <p>/<strong>/<u> is <p>
                            '/following-sibling::p'  # all p's following <header> (NOT p/strong/u)
                            '['  # where 
                            'count'  # number of
                            '(following-sibling::p/strong/u)'  # preceding headers 
                            '='  # equals to 
                            'count'  # number of preceding headers before <heading> + 1. Logic: p's before and after will have diff number of preceding headers. 
                            '(//*[@id="%s"]'
                            '//span[contains(text(), "%s")]'
                            '/..'
                            '/following-sibling::p/strong/u[contains(text(), "%s")]'
                            '/../..'
                            '/following-sibling::p/strong/u)'
                            ']'
                            '/text()'  # get text of these <p>'s
                            % (tab, meal, "STATION", tab, meal, "STATION"))
        items = tree.xpath(xpath_by_heading)
        print "x_path_by_heading found these items:", items
        if items == []:
            items = tree.xpath(xpath_by_station_new)
            print "x_path_by_station_new found these items:", items

        #if u'\xa0' in items:
         #   items = items.remove(u'\xa0')

        while u'\xa0' in items:
           items.remove(u'\xa0')


        print ("TESTING scrape(\'dh\')....DAY: %s, TIME: %s, TAB: %s, MEAL: %s, HEADING: %s, ITEMS: %s" % (
            day, now_time, tab, meal, heading, items))
        return meal, heading, items

    elif place == "agora":
        meal = "lunch"
        heading = "Grab & Go"
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
        items = tree.xpath(xpath_by_heading)

        if u'\xa0' in items:
            items.remove(u'\xa0')
        print ("TESTING scrape(\'agora\')....DAY: %s, TIME: %s, TAB: %s, MEAL: %s, HEADING: %s, ITEMS: %s" % (
            day, now_time, tab, meal, heading, items))
        return meal, heading, items

    else:
        print "ERROR: please specify param 'place' as 'agora' or 'dh'"
        return None
