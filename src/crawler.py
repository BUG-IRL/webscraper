'''
############################################## ASIDE ##############################################
This is the module that contains the web crawler.
The main focus of the crawler is to access a URI, and for every anchor tag in the page,
    make a new crawler to access the anchor tag's URI.

This module will handle opening links and retriving the anchor tags from it.
'''

# imports

import re
import urllib.request as u
import uuid

# local imports

from .logger import Logger 
from .db import Database
from .consts import pv, Constants

# making the crawler OO class
# comment this later teehee

class Crawler:
    def __init__(self, 
        logger: Logger or bool = False, 
        db: Database or bool = False,
        tries: int = 5,
        nameGenerator = uuid.uuid4,
        uri: str = ""
        ):

        self._logger = logger
        self._db = db
        self._n = str(nameGenerator())[:8]
        self._uri = uri

        # Going to have a logger object and a database object passed into the constructor
        
        # basically, you have to tell it where to log and where to store information

        print(f"Made crawler {self._n}")

    def run(self):
        """
        This function makes an HTTP request to the inputted website via 'uri' and returns
        the scraped anchor tags with their completed URI

        Returns:
            A list of dicts [{}, {}, {}]
        """
        with u.urlopen(self._uri) as r: 
                return getAllAnchors(r)

    def isLogging(self):
        """
        Returns a boolean value if there is a Logger and if the Logger is logging

        Returns:
            boolean
        """
        if self.hasLogger(): return self._logger.isLogging()
        else: return False

    def hasLogger(self):
        """
        This function returns true or false whether the crawler has a logger or not

        Returns:
            true if has logger, false otherwise
        """
        return isinstance(self._logger, Logger)

    def hasDatabase(self):
        """
        This function returns true or false whether the crawler has a database or not

        Returns:
            true if has database, false otherwise
        """
        return isinstance(self._db, Database)

    @property
    def URI(self):
        return self._uri

    @property
    def Name(self):
        return self._n

    @property
    def Database(self):
        return self._db

    @property
    def Logger(self):
        return self._logger

    @property
    def Tries(self):
        return self._t

    def log(self, string: str):
        if self.hasLogger():
            self._logger.logToFile(string)
            return True
        else:
            return False

    def __str__(self):
        logStr = ("not logging", "logging with output file '%s'" % self._logger.fileOutput)[self.hasLogger()]
        dbStr = ("doesn't have a Database object", "has a Database object with name '%s'" % self._db.Name)[self.hasDatabase()]

        return f"{self._n} is {logStr} and {self._n} {dbStr}"

# defining functions

def printCrawler(c: Crawler) -> bool:
    """
    This function takes a Crawler object and prints it, same as doing print(CrawlerObject)

    Parameters:
        c (Crawler): The Crawler object to print
    """
    logStr = ("not logging", "logging with output file '%s'" % c.Logger.fileOutput)[c.hasLogger()]
    dbStr = ("doesn't have a Database object", "has a Database object with name '%s'" % c.Database.Name)[c.hasDatabase()]

    print(f"{c.Name} is {logStr} and {c.Name} {dbStr}")

    return True

def scrapeAttrs(a):
    """
    This function scrapes the attributes from an HTML element

    Parameters:
        a (str): The HTML element to be scraped in string form

    Returns:
        dict: A map of the attribute-pairs
    """

    r = {}
    r["tag"] = a[1:a.index(" ")]
    for kv in a[a.index(" "):][1:].split(">")[0][:-1].split("\" "):
        # trimming first 3 characters out ' <a ' and the last char '>'

        # finding the first occurance of =" and splitting based on that index
        # then unpacking the results from split and mapping it
        try:
            k, v = kv.split('="')
            if k and v:
                r[k] = v
        except ValueError as ve:
            # tried to splice a bad tag/string
            # therefore not a real tag
            pv("Caught bad tag during scrapeAttrs '%s'" % kv)
        except Exception as e:
            pv("Caught handled exception in scrapeAttrs: %s" % str(e))

    return r

def scrapeAnchors(s: str, p: str = Constants.anchorPattern):
    """
    A generator function which yields an anchor tag
    
    Parameters:
        string (str): Takes the full string of an HTML response

    Returns:
        Yields a string object
    """

    for i in re.findall(p, s):
        for j in i.split("<a"):
            if not j: 
                continue
            yield ("<a" + j)

def sanitizeAnchors(l, response: u.http.client.HTTPResponse, tags=Constants.tags):
    """
    This function scrapes the attributes from an HTML element
    
    '/new' --> 'https://youtube.com/new'
    Parameters:
        l (List of dicts): Takes an array of output from scrapeAttrs

    Returns:
        A list of dicts [{}, {}, {}]
    """

    r = []

    for i in l:
        if i["tag"] != "a":
            continue
        value = i['href']
        if value[0] == '/':
            if len(value) == 1:
                i['href'] = response.url
            else: 
                # some of the href tags might be /sometext
                # need to filter it out

                i['href'] = response.url + i['href'][1:]

        # removing all attrs but tag and href using a list comprehension
        i = {k:v for k, v in i.items() if k in tags}
        
        # ensuring no duplicates
        if not i in r: r.append(i)

    return r


def getAllAnchors(s: u.http.client.HTTPResponse):
    """
    This function takes the string of an HTTPResponse and scrapes all
    the anchor tags and returns them as a python dict
    
    Parameters:
        s (str): HTTPResponse

    Returns:
        A list of dicts
    """

    r = []

    for a in scrapeAnchors(str(s.read())):
        try:
            r.append(scrapeAttrs(a))
        except Exception as e:
            pv("Caught exception during getAllAnchors: %s" % str(e))

    return sanitizeAnchors(r, s)