'''
############################################## ASIDE ##############################################
This module will contain all the constant variables and functions which will be used by all 
    other modules.
'''

# Constants #
class Constants:
    # this is just a fancy container for a bunch of vars

    # This enables the logging to the screen
    verbose = True

# Functions #
def pv(s: str): # pv ---> print verbose
    if Constants.verbose:
        print(s)