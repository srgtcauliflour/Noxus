import psutil

def size():
    return psutil.virtual_memory().total
def percentage():
    return psutil.virtual_memory().percent
def free():
    return psutil.virtual_memory().free
def used():
    return psutil.virtual_memory().used