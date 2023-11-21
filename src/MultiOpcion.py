from src.Ejercicio import Ejercicio
class MultiOpcion(Ejercicio):
    def __init__(self, Id, descripcion, pregunta, opciones, opcionCorrecta):
        super().__init__(Id, descripcion)
        self.__oracion = pregunta
        self.__MAPopciones = opciones
        self.__opcionCorrecta = opcionCorrecta

    def getOracion(self):
        return self.__oracion
    def getOpciones(self):
        return self.__MAPopciones
    def getOpcionCorrecta(self):
        return self.__opcionCorrecta