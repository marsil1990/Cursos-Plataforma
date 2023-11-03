from src.DTUsuario import DTUsuario
class DTProfesor(DTUsuario):
    def __init__ (self, Nickname, Contraseña, Nombre, Descripcion, Instituto):
        super().__init__(Nickname, Contraseña, Nombre, Descripcion)
        self.__instituto = Instituto

    def getInstituto(self):
        return self.__instituto
    
