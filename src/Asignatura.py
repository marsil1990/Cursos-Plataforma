class Asignatura:
    def __init__ (self, nombre):
        self.__Nombre = nombre
        self.__SETobservers = None
        self.__MAPCursos = dict()
    def getNombre(self):
        return self.__Nombre
    def AgregarSuscriptor(u): pass
    def removerUsuario(nombre): pass
    def SETgetDataCursosHab(): pass
    def agregar(observer): pass
    def eliminar(observer): pass
    def EnviarNotificacion(curso): pass
    def asociarCursoAsignatura(self, curso):
        self.__MAPCursos[curso.getNombre()] = curso
    def removerCurso(Nombre): pass
   