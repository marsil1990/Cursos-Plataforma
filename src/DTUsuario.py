class DTUsuario :
    def __init__(self, Nickname, Contrasena, Nombre, Descripcion):
        self.__Nickname = Nickname
        self.__Contrasena = Contrasena
        self.__Nombre = Nombre
        self.__Descripcion = Descripcion
    def getNickname(self):
        return self.__Nickname
    def getContraseña(self):
        return self.__Contrasena
    def getDescripcion(self):
        return self.__Descripcion
    def getNombre(self):
        return self.__Nombre
   