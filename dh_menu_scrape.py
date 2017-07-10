from lxml import html
import requests

url = "https://studentlife.yale-nus.edu.sg/dining-experience/daily-dining-menu/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


def scrape(day, meal):

    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    tab = ""
    special = ""

    if day == "friday":
        tab = "tab5"
    elif day == "today":
        tab = "tab_na"
    if meal == "breakfast":
        heading = "Live Station"

    xpath_string = ('//*[@id="%s"]'
    '//p/strong/u[contains(text(), "%s")]'
    '/../../'
    'following-sibling::p'
    '['
    'count'
    '(preceding-sibling::p/strong/u)'
    '='
    'count'
    '(//*[@id="%s"]'
    '//p/strong/u[contains(text(), "%s")]'
    '/../../'
    'preceding-sibling::p/strong/u)'
    '+ 1'
    ']'
    '/text()' % (tab, heading, tab, heading))

    items = tree.xpath(xpath_string)

    if u'\xa0' in items:
        items.remove(u'\xa0')
    print items
    return items
