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
    def getCantidadPalabras(self):
        return len(self.__MAPPalabrasFaltantes)
    def ingresarSolucion(self, MAPsolucion):
        count = 0
        for i in self.__MAPPalabrasFaltantes:
            if self.__MAPPalabrasFaltantes[i] == MAPsolucion[i]:
                count += 1
        return count == self.getCantidadPalabras()
        

    