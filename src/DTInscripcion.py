from src.Inscripcion import Inscripcion
class DTInscripcion:
    def __init__(self, fecha = None, cursoIns = None, estudiante = None, inscripcion = None):
        if inscripcion is None:
            self.__FechaDeInscripcion = fecha
            self.__CursoInscripto = cursoIns
            self.__EstudianteInscripto = estudiante
        else:
            self.__FechaDeInscripcion = inscripcion.getFechaDeInscripcion()
            self.__CursoInscripto = inscripcion.getCursoInscripto()
            self.__EstudianteInscripto = inscripcion.getEstudianteInscripto()

    def getFechaDeInscripcion(self):
        return self.__FechaDeInscripcion
    def getCursoInscripto(self):
        return self.__CursoInscripto
    def getEstudianteInscripto(self):
        return self.__EstudianteInscripto