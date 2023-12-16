from src.Usuario import Usuario
from src.DTCurso import DTCurso
class Profesor(Usuario):

    def __init__(self, nickname, contraseña, nombre, descripcion, instituto):
        super().__init__(nickname, contraseña, nombre, descripcion)
        self.__Instituto = instituto
        self.__MAPEspecializacion = dict()
        self.__MAPCursos = dict()
        self.__MAPsuscrito = dict()
        self.__SETnotificaciones = set()

    def getInstituto(self):
        return self.__Instituto
    
    def AgregarEspecializacion(self, asignatura):
        self.__MAPEspecializacion[asignatura] = asignatura

    def SETobtenerEspecializaciones(self):
        especializaciones = set()
        for e in self.__MAPEspecializacion:
            especializaciones.add(e)
        return especializaciones

    def asociarCursoProfesor(self, curso): 
        self.__MAPCursos[curso.getNombre()] = curso

    def SETgetDataCursosHab(self, asignatura):
        cursosHabilitados = set()
        for c in self.__MAPCursos.values():
            if c.getHabilitado() and c.getAsignatura().getNombre() == asignatura:
                #cursosData = DTCurso(c)
                cursosHabilitados.add(c.getNombre())
        return cursosHabilitados


    def SETobtenerCursosNoHabilitados(self):
        cursosNoHabilitados = set()
        for c in self.__MAPCursos.values():
            if not c.getHabilitado():
                #cursosData = DTCurso(c)
                cursosNoHabilitados.add(c.getNombre())
        return cursosNoHabilitados
    
    def MAPcursos(self):
        return self.__MAPCursos


    def SETObtenerNomAsignaturaSuscrito(self):
        nomAsignatura = set()
        for a in self.__MAPsuscrito:
            nomAsignatura.add(a.getNombre())
        return nomAsignatura
    
    def agreagarSuscripcion(self, asignatura):
        self.__MAPsuscrito[asignatura.getNombre()]= asignatura.getNombre()

    def eliminarSuscripcion(self, nombreAsignatura):
        del self.__MAPsuscrito[nombreAsignatura]  

    def SETDevolverNotificaciones(self):
        return self.__SETnotificaciones
    
    def elimiarNotificaciones(self):
        self.__SETnotificaciones.clear()
        
    def notificar(self, DTnuevocurso):
        self.__SETnotificaciones.add(DTnuevocurso)

    def eliminarCurso(nombreCurso):
        pass
   
