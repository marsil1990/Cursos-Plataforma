from src.Ejercicio import Ejercicio
class Leccion:
    def __init__(self, orden, tema, objetivo, ejercicios = None):
        self.__orden = orden
        self.__tema = tema
        self.__objetivo = objetivo
        self.__MAPEjercicio = ejercicios
    
    def getOrden(self): 
        return self.__orden
    def getTema(self):
        return self.__tema
    def getObjetivo(self):
        return self.__objetivo
    def añadirEjercicio(descripcion, frase,  MAPrespuesta): pass
    def añadirEjercicio(descripcion, frase, traduccion): pass
    def contarEjercicios(tot, ap, nickestudiante): pass
    def SETobtenerNoAprobados(): pass
    def obtenerEjercicio(nombreEjercicio): pass
    def getCantEjercicios(): pass
    def setOrden(orden): pass
    def MAPgetColEjercicios(): pass
    def eliminarEjercicios(): pass