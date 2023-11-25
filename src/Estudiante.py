from src.Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, Nickname,  Contrasena,  Nombre,  Descripcion,  Pais, FechaNac):
        super().__init__(Nickname, Contrasena, Nombre, Descripcion)
        self.__pais = Pais
        self.__FechaNac = FechaNac
        self.__FechaNac = None
        self.__SETNotificaciones = set()
        self.__MAPCursosInscriptos = dict()
        self.__MAPInscripciones = dict()

    def getPais(self):
        return self.__pais
    def getFechaNac(self):
        return self.__FechaNac
    
    def MAPObtenerCursosInscriptos(self):
        return self.__MAPCursosInscriptos
    
    def notificar(DTnuevocurso):pass
    def  MAPgetInscripciones():pass
    def inscribirseCurso(self, nombreCurso, curso, aprobarCurso = False, f= None):
        from src.Inscripcion import Inscripcion
        nuevaInscripcion = Inscripcion(f, curso, self)
        if aprobarCurso:
           nuevaInscripcion.setAprobada(True)
        
        self.__MAPCursosInscriptos[nombreCurso] = curso
        self.__MAPInscripciones[nombreCurso] =  nuevaInscripcion
        curso.inscribirEstudiante(self)
    
    def SETObtenerNomAsignaturaSuscrito():pass 
    def SETDevolverNotificaciones():pass
    def MAPobtenerCursos():pass
    def getInscripcion(self,cursoNombre):
        return self.__MAPCursosInscriptos[cursoNombre]
    def removerCurso( nombreCurso):pass
    
    