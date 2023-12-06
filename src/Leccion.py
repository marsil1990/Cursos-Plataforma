from src.CompletarPalabra import CompletarPalabra
from src.MultiOpcion import MultiOpcion
class Leccion:
    def __init__(self, orden, tema, objetivo, ejercicios = None):
        self.__orden = orden
        self.__tema = tema
        self.__objetivo = objetivo
        if ejercicios is None:
           self.__MAPEjercicio = dict()
        else:
           self.__MAPEjercicio =  ejercicios
    
    def getOrden(self): 
        return self.__orden
    def getTema(self):
        return self.__tema
    def getObjetivo(self):
        return self.__objetivo
    def añadirEjercicioCompletar(self, descripcion, frase,  MAPrespuesta):
        n = len(self.__MAPEjercicio) + 1
        ej = CompletarPalabra(n , descripcion, frase, MAPrespuesta)
        self.__MAPEjercicio[n] = ej
        

    def añadirEjercicioMultiple(self, descripcion, pregunta, opciones, opcionCorrecta):
        n = len(self.__MAPEjercicio) + 1
        ej = MultiOpcion(n , descripcion,pregunta, opciones, opcionCorrecta)
        self.__MAPEjercicio[n] = ej
    def contarEjercicios(tot, ap, nickestudiante): pass
    def SETobtenerNoAprobados(): pass
    def obtenerEjercicio(self, Id):
        return self.__MAPEjercicio[Id]
    def getCantEjercicios(self):
        return len(self.__MAPEjercicio)
    def setOrden(orden): pass
    def MAPgetColEjercicios(self):
        return self.__MAPEjercicio
    def eliminarEjercicios(): pass