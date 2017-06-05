from lxml import html
import requests

url = "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)

def get_day_special (day, meal):
    tab = ""
    special = ""
    if day == "friday":
        tab = "tab5"
    elif day == "today":
        tab = "tab_na"

    if meal == "bf":
        special = "Live Station"

    xpath_string = ('//*[@id="%s"]'
    '//p/strong/u[contains(text(), "%s")]'
    '/../../'
    'following-sibling::p'
    '['
    'count'
    '(preceding-sibling::p/strong/u)'
    '='
    'count'
    '(//*[@id="tab5"]'
    '//p/strong/u[contains(text(), "Live Station")]'
    '/../../'
    'preceding-sibling::p/strong/u)'
    '+ 1'
    ']'
    '/text()' % (tab, special))

    day_special = tree.xpath(xpath_string)

    if u'\xa0' in day_special:
        day_special.remove(u'\xa0')

    return day_special

print get_day_special ("today", "bf")
print get_day_special ("friday", "bf")

