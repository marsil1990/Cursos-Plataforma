from src.DTUsuario import DTUsuario
from src.Estudiante import Estudiante
from src.DTInscripcion import DTInscripcion
from src.DTFecha import DTFecha
class DTEstudiante(DTUsuario):
    def __init__(self, Nickname=None, Contrasena=None, Nombre=None, Descripcion=None, Pais=None, Fecha=None, estudiante = None):
        if estudiante is None:
            super().__init__(Nickname, Contrasena, Nombre, Descripcion)
            self.__Pais = Pais
            self.__Fecha = Fecha
        else:
            super().__init__(estudiante.getNickname(), estudiante.getContrasena(), estudiante.getNombre(), estudiante.getDescripcion())
            self.__Pais = estudiante.getPais()
            self.__Fecha = estudiante.getFechaNac()
            self.__inscripciones = dict()
            ins = estudiante.MAPgetInscripciones()
            for ik, iv in ins.items():
                self.__inscripciones[ik] = DTInscripcion(inscripcion=iv)


    def getPais(self):
        return self.__Pais

    def getFecha(self):
        return self.__Fecha
    
    def getInscripcion(self, nombreCurso):
        return self.__inscripciones[nombreCurso]
   
    