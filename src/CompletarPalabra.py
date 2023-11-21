from src.Ejercicio import Ejercicio
class CompletarPalabra(Ejercicio):
    def __init__(self, Id, descripcion, frase, palabrasFaltantes):
        super().__init__(Id, descripcion)
        self.__Frase = frase
        self.__MAPPalabrasFaltantes = palabrasFaltantes
        

    def  getFrase(self):
        return self.__Frase
    def getPalabrasFaltantes(self):
        return self.__MAPPalabrasFaltantes
    def ingresarSolucion(MAPsolucion):
        pass
    