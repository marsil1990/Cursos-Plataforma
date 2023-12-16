from src.Curso import Curso
class Asignatura:
    def __init__ (self, nombre):
        self.__Nombre = nombre
        self.__SETobservers = set()
        self.__MAPCursos = dict()
    def getNombre(self):
        return self.__Nombre
    def AgregarSuscriptor(self, u): 
        self.__SETobservers.add(u.getNickname())
    def removerUsuario(nombre): pass
    def SETgetDataCursosHab(): pass
    def agregar(observer): pass
    def eliminar(self, observer):
        self.__SETobservers.remove(observer)
    def EnviarNotificacion(self, curso):
        for o in self.__SETobservers:
            cursoNombre = str(curso)
            notificacion = "Nuevo curso: "+ cursoNombre + " /  Asignatura: " + self.__Nombre
            o.notificar(notificacion)

    def asociarCursoAsignatura(self, curso):
        self.__MAPCursos[curso.getNombre()] = curso
    def removerCurso(Nombre): pass
   