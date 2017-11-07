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


