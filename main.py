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
# from src.consts import *
# import urllib.request

# href = "https://youtube.com"

# with urllib.request.urlopen(href) as response:

#     scraped = crawler.getAllAnchors(response)

#     for index, i in enumerate(scraped):
#         print(index, i)

l = logger.Logger(outputFile="h")
d = db.Database(dbName=True)

hasBoth = crawler.Crawler(logger=l, db=d)
print("%s isLogging func %s" %("hasBoth", str(hasBoth.isLogging()))) # True
print("%s hasLogger func %s" %("hasBoth", str(hasBoth.hasLogger()))) # True
print("%s hasDatabase func %s" %("hasBoth", str(hasBoth.hasDatabase()))) # True
print()

hasBoth.log("logged something lmao")