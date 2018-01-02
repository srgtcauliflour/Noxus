import platform

def os():
    return platform.uname().system
def osVersion():
    return platform.uname().version
def name():
    return platform.uname().node
def arc():
    return platform.uname().machine
def cpu():
    return platform.uname().processor
def distro():
    if os() == "Linux":
        return platform.linux_distribution()
    else:
<<<<<<< HEAD
        return os()
=======
        return os()
>>>>>>> a2800409e2863e49934e05951eb6857da84b5e96
