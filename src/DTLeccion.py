class DTLeccion:
    def __init__(self, orden, tema, objetivo):
        self.__Orden = orden
        self.__Tema =  tema
        self.__objetivo = objetivo

    def getOrden(self):
        return self.__Orden
    def getTema(self):
        return self.__Tema
    def getObjetivo(self):
        return self.__objetivo