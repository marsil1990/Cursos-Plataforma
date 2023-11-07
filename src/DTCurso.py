class DTCurso :
    def __init__(self, nombre=None, descripcion=None, dificultad=None, nombreProfesor=None, 
                 asignatura=None, estado=None, cantLecciones=None, cantEjercicios=None, cantInscriptos=None):
       self.__Nombre = nombre
       self.__Descripcion = descripcion
       self.__Dificultad = dificultad
       self.__NombreProfesor = nombreProfesor
       self.__NombreAsignaturaCurso = asignatura
       self.__MAPinscriptos = dict()
       self.__Habilitado = estado
       self.__cantLecciones = cantLecciones
       self.__cantEjercicios = cantEjercicios
       self.__cantInscriptos = cantInscriptos

    def DTCurso(curso):
        cursoData = DTCurso(curso.getNombre(), curso.getDesc(), curso.getDificultad(), curso.getNombreProfesor(),
                        curso.getAsignatura(), curso.getHabilitado(), curso.getcantLecciones(),
                         curso.getcantEjercicios(), curso.getCantInscriptos() )
        return cursoData
    def getNombre(): pass
    def getDesc(): pass
    def getDificultad(): pass
    def getNombreProfesor(): pass
    def getNombreIdiomaCurso(): pass
    def getHabilitado(): pass
    def getcantLecciones(): pass
    def getcantEjercicios(): pass
    def getCantInscriptos(): pass
    def MAPgetEstudiantesInscriptos(): pass