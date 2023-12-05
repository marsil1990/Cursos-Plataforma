class Ejercicio:
    def __init__(self, identificacion, descripcion): 
       self.__Id = identificacion
       self.__Descripcion = descripcion
       self.__MAPEstudiantesAprobaron = dict()

    def getId(self):
        return self.__Id
    def getDescripcion(self):
        return self.__Descripcion
    def esAprovado(self, nicknameEstudiante):
        if nicknameEstudiante in self.__MAPEstudiantesAprobaron:
            return True
        else: 
            return False
    def addEstudianteAprobado(self,nicknameEstudiante, inscripcion):
        self.__MAPEstudiantesAprobaron[nicknameEstudiante] = inscripcion