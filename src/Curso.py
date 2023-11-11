from src.ManejadorCurso import ManejadorCurso
class Curso:
    def __init__(self, nombre, descripcion, nivel, profesor=None, asignatura = None):
       self.__Nombre = nombre
       self.__Descripcion=descripcion
       self.__Dificultad=nivel
       self.__ProfesorCurso = profesor
       self.__AsignaturaCurso = asignatura
       self.__Previas= dict()
       self.__Habilitado = True
       self.__MAPalumnosInscriptos=None
       self.__MAPLecciones=None

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
    def setHabilitado(self):
        if self.__Habilitado == False:
            return True
        else: return False
    def inscribirEstudiante(estudiante):pass
    def getCantLecciones():pass
    def setProfesor(self, profesor):
        self.__ProfesorCurso = profesor
    def setHabilitado(habilitado):pass
    def removerPrevia(nombreCurso):pass
    def getDataCurso():pass
    def añadirLeccion(lec):pass
    def añadirPrevia(self, previa):
        self.__Previas[previa.getNombre()]=previa

    def obtenerAvanceCurso(nickEstudiante):pass
    def obtenerPromedioCurso(): pass
    def obtenerSiguienteLeccion(orden):pass
    def SETgetLecciones(): pass
    def nuevoEjercicio(lec, descripcion, frase, MAPsolucion):pass
    def nuevoEjercicio(lec, descripcion, frase, solucion):pass
    def habilitarCurso(): pass
    def getCantEjercicios(): pass
    def MAPgetColLecciones(): pass
    def eliminarLecciones(): pass
    def eliminarPrevias(nomCurso): pass
    def getProfesor(self):
        return self.__ProfesorCurso
    def MAPgetEstudiantes(): pass
    def getNicknameProfesor(): pass
    def getCantInscriptos(): pass
    def borrarPrevias(): pass