from src.DTCurso import DTCurso
class ManejadorCurso(object):
    __instancia = None
    __MAPCursos = None
    def __new__(cls):
        if ManejadorCurso.__instancia is None:
            ManejadorCurso.__instancia = object.__new__(cls)
            ManejadorCurso.__MAPCursos = dict()
        return ManejadorCurso.__instancia
    
    
    def obtenerCurso(self, nombreCurso):
        return self.__MAPCursos[nombreCurso]
    def  SETobtenerCursosDisponibles(self):
        cursosDisponibles = set()
        for c in self.__MAPCursos.values():
            cursosDisponibles.add(c.getNombre())
        return cursosDisponibles

    def ExisteCurso(self, nombreCurso):
        return nombreCurso in self.__MAPCursos
    
    def obtenerLeccion(self, nombreCurso, orden):
        return self.__MAPCursos[nombreCurso].obtenerLeccion(orden)

    def SETobtenerCursosNoHab(): pass
    def SETCursosInscriptoNoAprobado(): pass
    def SETejerciciosNoAprobados(): pass

    #Devuelve los cursos que se encuentran en la lista de string "nombreCursos"
    def SETobtenerCursos(self, nombreCursos):
        cursosPrevios = set()
        for prev in nombreCursos:
            cursosPrevios.add(self.__MAPCursos[prev])
        return cursosPrevios
            

    def eliminarPrevia(NomCursos): pass

        
    def agregarCurso(self, curso):
        self.__MAPCursos[curso.getNombre()] = curso
        
        
    def SETobtenerTodosCursos(self):
        cursos = set()
        for c in self.__MAPCursos.values():
            cursos.add(DTCurso(curso=c))
        return cursos
    def getCursos(self):
        return self.__MAPCursos

    def eliminarCurso(self,nombreCurso):
        self.__MAPCursos[nombreCurso].eliminarLecciones()
        self.__MAPCursos[nombreCurso].eliminarInscripciones()
        for c in self.__MAPCursos.values():
            if c.esPrevia(nombreCurso):
                c.removerPrevia(nombreCurso)
        del self.__MAPCursos[nombreCurso]