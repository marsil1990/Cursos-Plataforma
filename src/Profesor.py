from src.Usuario import Usuario
from src.DTCurso import DTCurso
class Profesor(Usuario):

    def __init__(self, nickname, contraseña, nombre, descripcion, instituto):
        super().__init__(nickname, contraseña, nombre, descripcion)
        self.__Instituto = instituto
        self.__MAPEspecializacion = dict()
        self.__MAPCursos = dict()

    def getInstituto(self):
        return self.__Instituto
    
    def AgregarEspecializacion(self, Asignatura):
        self.__MAPEspecializacion[Asignatura] = Asignatura

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
            if c.getHabilitado():
                #cursosData = DTCurso(c)
                cursosHabilitados.add(c.getNombre())
        return cursosHabilitados


    def SETobtenerCursosNoHabilitados():
        pass

    def eliminarCurso(nombreCurso):
        pass
   
