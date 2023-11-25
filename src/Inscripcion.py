from src.Estudiante import Estudiante
class Inscripcion:
    def __init__(self, fecha, curso, estudiante):
        self.__UltimaLeccionAprobada = None
        self.__FechaDeInscripcion = fecha 
        self.__CursoInscripto = estudiante
        self.__aprobada = False
        self.__estudianteInscripto = estudiante

    def getUltimaLeccionAprobada(self):
        return self.__UltimaLeccionAprobada
    def getFechaDeInscripcion(self):
        return self.__FechaDeInscripcion
    def getAprobada(self):
        return self.__aprobada 
    def getCursoInscripto(self):
        return self.__CursoInscripto
    def getEstudianteInscripto(self):
        return self.__estudianteInscripto
    def setAprobada(self, aprobada):
        self.__aprobada = aprobada    
    def setNuevaLeccionAprobada(self, leccion):
        self.__UltimaLeccionAprobada = leccion
   