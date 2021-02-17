"""
To do:

make web crawler class
make multi threading
make logging
make crawlers for each scraped anchor tag
"""

__author__ = "Liam Major"
__version__ = "0.1"

from src import db, logger, crawler
from src.consts import *
import urllib.request

href = "https://youtube.com"

with urllib.request.urlopen(href) as response:

    scraped = crawler.get_all_anchors(response)

    for index, i in enumerate(scraped):
        print(index, i)