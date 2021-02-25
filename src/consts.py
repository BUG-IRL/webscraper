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
    anchorPattern = r"<a.+<\/a>"
    tags = ("tag", "href")

# Functions #
def pv(s: str): # pv ---> print verbose
    if Constants.verbose:
        print(s)

def paramError(paramName: str, allowedTypes: list or str, typeReceived: str):
    if isinstance(allowedTypes, list) or isinstance(allowedTypes, tuple):
        typeString = ", ".join(str(T) for T in allowedTypes)
    elif isinstance(allowedTypes, str):
        typeString = allowedTypes
    else:
        raise TypeError("allowedTypes can be of type list or str %s" % type(allowedTypes))

    raise TypeError(f"{paramName} can only be of type {typeString} not {typeReceived}")  