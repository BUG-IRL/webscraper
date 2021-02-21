"""
To do:

Current:
1. complete logging functions
2. complete database functions

Future:
3. introduce multithreading options
"""

__author__ = "Liam Major"
__version__ = "0.1"

from src import db, logger, crawler
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