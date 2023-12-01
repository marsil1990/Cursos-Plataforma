from src.DTEstudiante import DTEstudiante
from src.DTLeccion import DTLeccion

class DTCurso :
    def __init__(self, nombre=None, descripcion=None, dificultad=None, nombreProfesor=None, 
                 asignatura=None, estado=None, cantLecciones=None, cantEjercicios=None, cantInscriptos=None, curso = None):
        if curso is None:
            self.__curso = None
            self.__Nombre = nombre
            self.__Descripcion = descripcion
            self.__Dificultad = dificultad
            self.__NombreProfesor = nombreProfesor
            self.__NombreAsignaturaCurso = asignatura
            self.__Habilitado = estado
            self.__cantLecciones = cantLecciones
            self.__cantEjercicios = cantEjercicios
            self.__cantInscriptos = cantInscriptos
            self.__Lecciones = dict()
            self.__MAPinscriptos = dict()
        else:
            from src.Curso import Curso
            self.__Nombre = curso.getNombre()
            self.__Descripcion= curso.getDescripcion()
            self.__Dificultad= curso.getDificultad()
            self.__NombreProfesor = curso.getNombreProfesor()
            self.__NombreAsignaturaCurso = curso.getAsignatura().getNombre()
            self.__Habilitado= curso.getHabilitado()
            self.__cantLecciones = curso.getCantLecciones()
            self.__cantEjercicios = curso.getCantEjercicios()
            self.__cantInscriptos = curso.getCantInscriptos()
            self.__MAPinscriptos = dict()
            self.__Lecciones = dict()
            estudiantes = curso.MAPgetEstudiantes()
            for ek, ev in estudiantes.items():
                self.__MAPinscriptos[ek] = DTEstudiante(estudiante=ev)
            lecciones = curso.MAPgetColLecciones()
            for lk, lv in lecciones.items():
                self.__Lecciones[lk] = DTLeccion(leccion=lv)
            



 
        
        
    def getNombre(self): 
        return self.__Nombre
    def getDesc(self):
        return self.__Descripcion
    def getDificultad(self):
        return self.__Dificultad
    def getNombreProfesor(self):
        return self.__NombreProfesor
    def getNombreAsignatura(self):
        return self.__NombreAsignaturaCurso
    def getHabilitado(self):
        if self.__Habilitado:
            return "Si" 
        else:
            return "No"
    def getcantLecciones(self):
        return self.__cantLecciones
    def getcantEjercicios(self):
        return self.__cantEjercicios
    def getCantInscriptos(self):
        return self.__cantInscriptos
    def MAPgetEstudiantesInscriptos(self):
        return self.__MAPinscriptos
    def getLecciones(self):
        return self.__Lecciones
