"""
To do:

Current:
1. complete logging functions
2. complete database functions

Future:
3. introduce multithreading options
"""

__author__ = "Liam Major"
__version__ = "0.7"

from src import db, logger, crawler

href = "https://youtube.com"

l = logger.Logger(outputFile="h")
d = db.Database(dbName="h")

hasBoth = crawler.Crawler(logger=l, db=d, uri=href)
result = hasBoth.run()

for index, i in enumerate(result):
    print(index, i)
