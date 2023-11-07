class ManejadorCurso(object):
    __inctancia = None
    __MAPCursos = None
    def __new__(cls):
        if ManejadorCurso.__inctancia is None:
            ManejadorCurso.__inctancia = object.__new__(cls)
            ManejadorCurso.__MAPCursos = dict()
        return ManejadorCurso.__inctancia
    
    
    def obtenerCurso(nombreCurso): pass
    def  SETobtenerCursosDisponibles(): pass
    def ExisteCurso(nombreCurso): pass
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
        self.__MAPCursos[curso.getNombre()]
    def SETobtenerTodosCursos(): pass
    def eliminarCurso(nombreCurso): pass