'''
############################################## ASIDE ##############################################
This is the module that contains the database for all the websites visited.
'''

# comment this later teehee

from .consts import Constants, paramError

class Database:
    def __init__(self, dbName: str or bool = False):
        self._ref = dbName

        # param checking
        if not isinstance(self._ref, str) or self._ref == True:
            paramError('dbName', ['str', 'False'], type(self._ref))

    @property
    def Name(self):
        return str(self._ref)

    def isDatabase(self):
        # returns a true or false there is a database reference passed
        return (self._ref != False)