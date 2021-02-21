'''
############################################## ASIDE ##############################################
This is the module that will contain all the code for the logging process.
It will be a neat wrapper that can be interfaced with via. multithreading and the webcrawler
'''

# comment this later teehee

from .consts import Constants

class Logger:
    def __init__(self, verbose: bool = Constants.verbose, outputFile: str or bool = False):
        self._fout = outputFile

        # Verifying params
        if not isinstance(self._active, bool):
            raise ValueError("isLogging can only be of type boolean not of type %s" % type(self._active))
        if not self._fout and self._fout != True:
            if not isinstance(self._fout, str):
                raise ValueError("outputFile can only be of type string or False not of type %s" % type(self._fout)) 
        
    def logToFile(self, string: str):
        # in the future it'll just self._fout.write(string)

        print(string)

    def isLogging(self):
        return isinstance(self._fout, str) and not self._fout
