from src.Usuario import Usuario
class Estudiante(Usuario):

    __FechaNac = None
    __SETNotificaciones = None
    __MAPCursosInscriptos = None
    __MAPInscripciones = None


    def __init__(self, Nickname,  Contrasena,  Nombre,  Descripcion,  Pais, FechaNac):
        super().__init__(Nickname, Contrasena, Nombre, Descripcion)
        self.__pais = Pais
        self.__FechaNac = FechaNac

    def getPais(self):
        return self.__pais
    def getFechaNac(self):
        return self.__FechaNac
    def MAPObtenerCursosInscriptos():pass
    def notificar(DTnuevocurso):pass
    def  MAPgetInscripciones():pass
    def inscribirseCurso( nombreCurso, curso,aprobarCurso = False, f= None):pass
    def SETObtenerNomIdiomaSuscrito():pass 
    def SETDevolverNotificaciones():pass
    def MAPobtenerCursos():pass
    def getInscripcion( cursoNombre):pass
    def removerCurso( nombreCurso):pass
    
    