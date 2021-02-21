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

#     scraped = crawler.get_all_anchors(response)

#     for index, i in enumerate(scraped):
#         print(index, i)

l = logger.Logger(outputFile="h")
d = db.Database(dbName=True)

hasLogger = crawler.Crawler(logger=l)
print("%s isLogging func %s" %("hasLogger", str(hasLogger.isLogging()))) # True
print("%s hasLogger func %s" %("hasLogger", str(hasLogger.hasLogger()))) # True
print("%s hasDatabase func %s" %("hasLogger", str(hasLogger.hasDatabase()))) # False
print()

hasDatabase = crawler.Crawler(db=d)
print("%s isLogging func %s" %("hasDatabase", str(hasDatabase.isLogging()))) # False
print("%s hasLogger func %s" %("hasDatabase", str(hasDatabase.hasLogger()))) # False
print("%s hasDatabase func %s" %("hasDatabase", str(hasDatabase.hasDatabase()))) # True
print()

hasBoth = crawler.Crawler(logger=l, db=d)
print("%s isLogging func %s" %("hasBoth", str(hasBoth.isLogging()))) # True
print("%s hasLogger func %s" %("hasBoth", str(hasBoth.hasLogger()))) # True
print("%s hasDatabase func %s" %("hasBoth", str(hasBoth.hasDatabase()))) # True
print()

hasNeither = crawler.Crawler()
print("%s isLogging func %s" %("hasNeither", str(hasNeither.isLogging()))) # False
print("%s hasLogger func %s" %("hasNeither", str(hasNeither.hasLogger()))) # False
print("%s hasDatabase func %s" %("hasNeither", str(hasNeither.hasDatabase()))) # False
