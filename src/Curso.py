from src.ManejadorCurso import ManejadorCurso
from src.Leccion import Leccion
from src.Estudiante import Estudiante
class Curso:
    def __init__(self, nombre, descripcion, nivel, profesor=None, asignatura = None):
       self.__Nombre = nombre
       self.__Descripcion=descripcion
       self.__Dificultad=nivel
       self.__ProfesorCurso = profesor
       self.__AsignaturaCurso = asignatura
       self.__Previas= dict()
       self.__Habilitado = False
       self.__MAPalumnosInscriptos=dict()
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
    def getNombreAsignatura(self):
        return self.__AsignaturaCurso.getNombre()
    def getHabilitado(self):
        return self.__Habilitado
    def esPrevia(self, nombreCurso):
        if nombreCurso in self.__Previas:
            return True
        else: 
            return False
    def setHabilitar(self):
        if self.__Habilitado == False:
            self.__Habilitado = True

    def inscribirEstudiante(self, estudiante):
        self.__MAPalumnosInscriptos[estudiante.getNickname()]=estudiante
    def getCantLecciones(self):
        return len(self.__MAPLecciones)
    def setProfesor(self, profesor):
        self.__ProfesorCurso = profesor
    def setHabilitado(habilitado):pass
    def removerPrevia(self, nombreCurso):
        if nombreCurso in self.__Previas:
            del self.__Previas[nombreCurso]

    def getDataCurso():pass
    def añadirLeccion(self, lec):
        self.__MAPLecciones[lec.getOrden()] =lec
    def añadirPrevia(self, previa):
        self.__Previas[previa.getNombre()]=previa

    def obtenerAvanceCurso(self, nickEstudiante):
        cantidadEjerciciosAprobados = 0
        for l in self.__MAPLecciones.values():
            ejercicios = l.MAPgetColEjercicios()
            for e in ejercicios.values():
                if e.esAprovado(nickEstudiante):
                    cantidadEjerciciosAprobados += 1
        return (cantidadEjerciciosAprobados/self.getCantEjercicios())*100

    def obtenerPromedioCurso(self): 
        cantAlumnosInscriptos = len(self.__MAPalumnosInscriptos)
        sumaAvanceAlumno = 0
        for a in self.__MAPalumnosInscriptos.values():
            avanceAlumno = self.obtenerAvanceCurso(a.getNickname())
            sumaAvanceAlumno += avanceAlumno
        if cantAlumnosInscriptos == 0:
            return 0
        else:
            return sumaAvanceAlumno/cantAlumnosInscriptos
            
    def obtenerSiguienteLeccion(orden):pass
    def obtenerLeccion(self, orden):
        return self.__MAPLecciones[orden]
    
    
    def MAPgetLecciones(self): 
        lecciones = dict()
        for lk, lv in self.__MAPLecciones.items():
            lecciones[lk] = lv.getTema()
        return lecciones
    def nuevoEjercicio(lec, descripcion, frase, MAPsolucion):pass
    def nuevoEjercicio(lec, descripcion, frase, solucion):pass
    def habilitarCurso(): pass
    def getCantEjercicios(self): 
        cant = 0
        for l in self.__MAPLecciones.values():
            cant += l.getCantEjercicios()
        return cant
    def MAPgetColLecciones(self):
        return self.__MAPLecciones
    def eliminarLecciones(self):
        for l in self.__MAPLecciones.values():
            l.eliminarEjercicios()
        self.__MAPLecciones.clear()
    def eliminarPrevias(nomCurso): pass
    def getProfesor(self):
        return self.__ProfesorCurso
    def getNombreProfesor(self):
        return self.__ProfesorCurso.getNombre()
    def MAPgetEstudiantes(self):
        return self.__MAPalumnosInscriptos
    def getNicknameProfesor(): pass
    def getCantInscriptos(self):
        return len(self.__MAPalumnosInscriptos)
    def eliminarInscripciones(self):
        pass
    def borrarPrevias(): pass