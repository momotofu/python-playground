import time
import urllib

from bs4 import BeautifulSoup as bs
import requests

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    res = requests.get(url)
    html = res.text
    soup = bs(html, "html.parser")

    # This div dontains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will ramain None
