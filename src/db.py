'''
############################################## ASIDE ##############################################
This is the module that contains the database for all the websites visited.
'''

# comment this later teehee

from .consts import Constants

class Database:
    def __init__(self, dbName: str or bool = False):
        self._ref = dbName

    def isDatabase(self):
        # returns a true or false there is a database reference passed
        return (self._ref != False)