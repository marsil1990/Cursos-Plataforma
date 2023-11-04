from src.Usuario import Usuario
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

    def asociarCursoProfesor(curso): 
        pass
    def MAPobtenerCursos():
        pass

    def eliminarCurso(nombreCurso):
        pass
   
