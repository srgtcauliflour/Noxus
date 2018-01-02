import platform

def os():
    return platform.uname().system
def osVersion():
    return platform.uname().version