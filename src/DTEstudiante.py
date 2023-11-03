from src.DTUsuario import DTUsuario
class DTEstudiante(DTUsuario):
    def __init__(self, Nickname, Contrasena, Nombre, Descripcion, Pais, Fecha):
        super().__init__(Nickname, Contrasena, Nombre, Descripcion)
        self.__Pais = Pais
        self.__Fecha = Fecha

    def getPais(self):
        return self.__Pais

    def getFecha(self):
        return self.__Fecha
   
    