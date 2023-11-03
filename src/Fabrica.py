from src.CtrUsuario import CtrUsuario
from src.CtrCurso import CtrCurso
"""def singleton(clase):
    instances = dict()
    def agrego(*args, **kwargs):
        if clase not in instances:
            instances[clase] = clase(*args, **kwargs)
        return instances[clase]
    return agrego"""
#@singleton

class Fabrica(object):
    __instancia = None
    
    def __new__ (cls):
        if Fabrica.__instancia is None:
            Fabrica.__instancia = object.__new__(cls)
        return Fabrica.__instancia
    

    def getIUsuario(self):
        return CtrUsuario()
    
    def getICurso(self):
        return CtrCurso()


    