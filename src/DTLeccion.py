from src.DTEjercicio import DTEjercicio
class DTLeccion:
    def __init__(self, orden = None, tema = None, objetivo=None, leccion = None):
        if leccion is None:
            self.__Orden = orden
            self.__Tema =  tema
            self.__objetivo = objetivo
        else:
            from src.Leccion import Leccion
            self.__Orden = leccion.getOrden()
            self.__Tema =  leccion.getTema()
            self.__objetivo = leccion.getObjetivo()
            self.__ejercicios = dict()
            ejercicios = leccion.MAPgetColEjercicios()
            for ek, ev in ejercicios.items():
                self.__ejercicios[ek] = DTEjercicio(ejercicio=ev)


    def getOrden(self):
        return self.__Orden
    def getTema(self):
        return self.__Tema
    def getObjetivo(self):
        return self.__objetivo
    def getEjercicios(self):
        return self.__ejercicios
    