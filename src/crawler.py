'''
############################################## ASIDE ##############################################
This is the module that contains the web crawler.
The main focus of the crawler is to access a URI, and for every anchor tag in the page,
    make a new crawler to access the anchor tag's URI.

This module will handle opening links and retriving the anchor tags from it.
'''

# imports

from .consts import pv
import re
import urllib.request as u

from .logger import Logger 
from .db import Database

# consts from here

anchor_pattern = r"<a.+<\/a>"

# making the crawler OO class
# comment this later teehee

class Crawler:
    def __init__(self, logger: Logger or bool = False, db: Database or bool = False):
        self._logger = logger
        self._db = db

        # Going to have a logger object and a database object passed into the constructor
        
        # basically, you have to tell it where to log and where to store information

        print("Made crawler")

    def isLogging(self):
        if self.hasLogger():
            return self._logger.isLogging()
        else:
            return False

    def hasLogger(self):
        return isinstance(self._logger, Logger)

    def hasDatabase(self):
        return isinstance(self._db, Database)

    def log(self, string: str):
        if self.hasLogger():
            print("called Crawler.log with a logger")
            self._logger.logToFile(string)

# defining functions

def scrape_attrs(a):
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
        k, v = kv.split('="')
        r[k] = v

    return r

def scrape_anchors(string):
    """
    A generator function which yields an anchor tag
    
    Parameters:
        string (str): Takes the full string of an HTML response

    Returns:
        Yields a string object
    """

    global anchor_pattern

    for i in re.findall(anchor_pattern, string):
        for j in i.split("<a"):
            if not j: 
                continue
            yield ("<a" + j)

def sanitize_anchors(l, response: u.http.client.HTTPResponse):
    """
    This function scrapes the attributes from an HTML element
    
    '/new' --> 'https://youtube.com/new'
    Parameters:
        l (List of dicts): Takes an array of output from scrape_attrs

    Returns:
        A list of dicts [{}, {}, {}]
    """

    r = []

    for i in l:
        value = i['href']
        if value[0] == '/':
            if len(value) == 1:
                i['href'] = response.url
            else: 
                # some of the href tags might be /sometext
                # need to filter it out

                i['href'] = response.url + i['href'][1:]
        
        r.append(i)

    return r


def get_all_anchors(s: u.http.client.HTTPResponse):
    """
    This function takes the string of an HTTPResponse and scrapes all
    the anchor tags and returns them as a python dict
    
    Parameters:
        s (str): HTTPResponse

    Returns:
        A list of dicts
    """

    r = []

    for a in scrape_anchors(str(s.read())):
        try:
            r.append(scrape_attrs(a))
        except Exception as e:
            pass

    return sanitize_anchors(r, s)