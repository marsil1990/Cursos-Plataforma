class Usuario:
    def __init__(self, nickname,  contrasena,  nombre,  descripcion):
        self.__Nickname = nickname
        self.__Contrasena = contrasena
        self.__Nombre = nombre
        self.__Descripcion = descripcion
        __MAPsuscrito = dict()
        __SETnotificaciones = set()

    def getNickname(self):
        return self.__Nickname
    def getContrasena(self):
        return self.__Contrasena
    def getDescripcion(self):
        return self.__Descripcion
    def getNombre(self):
        return self.__Nombre
    def removerAsignatura( nomAsignatura):pass
    def ObtenerNomAsignaturaSuscrito():pass
    def AgregarAsignaturaSuscrito(i):pass
    def SETDevolverNotificaciones():pass
    def notificar(dtnuevocurso):pass
  