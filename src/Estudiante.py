from src.Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, Nickname,  Contrasena,  Nombre,  Descripcion,  Pais, FechaNac):
        super().__init__(Nickname, Contrasena, Nombre, Descripcion)
        self.__pais = Pais
        self.__FechaNac = FechaNac
        self.__MAPCursosInscriptos = dict()
        self.__MAPInscripciones = dict()
        self.__MAPsuscrito = dict()
        self.__SETnotificaciones = set()

    def getPais(self):
        return self.__pais
    
    def getFechaNac(self):
        return self.__FechaNac
    
    def MAPObtenerCursosInscriptos(self):
        return self.__MAPCursosInscriptos
    
    def notificar(self, DTnuevocurso):
        self.__SETnotificaciones.add(DTnuevocurso)

    def  MAPgetInscripciones(self):
        return self.__MAPInscripciones
    
    def inscribirseCurso(self, nombreCurso, curso, aprobarCurso = False, f= None):
        from src.Inscripcion import Inscripcion
        nuevaInscripcion = Inscripcion(f, curso, self)
        if aprobarCurso:
           nuevaInscripcion.setAprobada(True)
        
        self.__MAPCursosInscriptos[nombreCurso] = curso
        self.__MAPInscripciones[nombreCurso] =  nuevaInscripcion
        curso.inscribirEstudiante(self)
    
    def SETObtenerNomAsignaturaSuscrito(self):
        nomAsignatura = set()
        for a in self.__MAPsuscrito:
            nomAsignatura.add(a)
        return nomAsignatura
    
    def SETDevolverNotificaciones(self):
        return self.__SETnotificaciones
    
    def elimiarNotificaciones(self):
        self.__SETnotificaciones.clear()

    def MAPobtenerCursos():pass

    def getInscripcion(self,cursoNombre):
        return self.__MAPInscripciones[cursoNombre]
    
    def agreagarSuscripcion(self, asignatura):
        self.__MAPsuscrito[asignatura.getNombre()]= asignatura.getNombre()
    
    def eliminarSuscripcion(self, nombreAsignatura):
        del self.__MAPsuscrito[nombreAsignatura]

    def removerCurso( nombreCurso):pass
    
    