from src.ManejadorCurso import ManejadorCurso
from src.Leccion import Leccion
class Curso:
    def __init__(self, nombre, descripcion, nivel, profesor=None, asignatura = None):
       self.__Nombre = nombre
       self.__Descripcion=descripcion
       self.__Dificultad=nivel
       self.__ProfesorCurso = profesor
       self.__AsignaturaCurso = asignatura
       self.__Previas= dict()
       self.__Habilitado = False
       self.__MAPalumnosInscriptos=None
       self.__MAPLecciones= dict()

    def getNombre(self):
        return self.__Nombre
    def getPrevias(self):
        return self.__Previas
    def getDescripcion(self):
        return self.__Descripcion
    def getDificultad(self):
        return self.__Dificultad
    def getAsignatura(self):
        return self.__AsignaturaCurso
    def getHabilitado(self):
        return self.__Habilitado
    
    def setHabilitar(self):
        if self.__Habilitado == False:
            self.__Habilitado = True

    def inscribirEstudiante(estudiante):pass
    def getCantLecciones(self):
        return len(self.__MAPLecciones)
    def setProfesor(self, profesor):
        self.__ProfesorCurso = profesor
    def setHabilitado(habilitado):pass
    def removerPrevia(nombreCurso):pass
    def getDataCurso():pass
    def añadirLeccion(self, lec):
        self.__MAPLecciones[lec.getOrden()] =lec
    def añadirPrevia(self, previa):
        self.__Previas[previa.getNombre()]=previa

    def obtenerAvanceCurso(nickEstudiante):pass
    def obtenerPromedioCurso(): pass
    def obtenerSiguienteLeccion(orden):pass
    def MAPgetLecciones(self): 
        lecciones = dict()
        for lk, lv in self.__MAPLecciones.items():
            lecciones[lk] = lv.getTema()
        return lecciones
    def nuevoEjercicio(lec, descripcion, frase, MAPsolucion):pass
    def nuevoEjercicio(lec, descripcion, frase, solucion):pass
    def habilitarCurso(): pass
    def getCantEjercicios(): pass
    def MAPgetColLecciones(self):
        return self.__MAPLecciones
    def eliminarLecciones(): pass
    def eliminarPrevias(nomCurso): pass
    def getProfesor(self):
        return self.__ProfesorCurso
    def MAPgetEstudiantes(): pass
    def getNicknameProfesor(): pass
    def getCantInscriptos(): pass
    def borrarPrevias(): pass