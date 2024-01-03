from src.CtrUser import CtrUser
from src.CtrCourse import CtrCourse
"""def singleton(clase):
    instances = dict()
    def agrego(*args, **kwargs):
        if clase not in instances:
            instances[clase] = clase(*args, **kwargs)
        return instances[clase]
    return agrego"""
#@singleton

class Factory(object):
    __instance = None
    
    def __new__ (cls):
        if Factory.__instance is None:
            Factory.__instance = object.__new__(cls)
        return Factory.__instance
    

    def getIUser(self):
        return CtrUser()
    
    def getICourse(self):
        return CtrCourse()


    