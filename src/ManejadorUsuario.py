from src.Profesor import Profesor
from src.Estudiante import Estudiante
class ManejadorUsuario(object):
    __instancia = None
    __MAPUsuarios = dict()
    
    def __new__(cls):
        if ManejadorUsuario.__instancia is None:
            ManejadorUsuario.__instancia = object.__new__(cls)
        return ManejadorUsuario.__instancia

    def ExisteUsuario(self, nickname):
        if nickname in self.__MAPUsuarios:
            return True
        else:
            return False
        
    def agregarUsuario(self, nuevoUsuario):
        self.__MAPUsuarios[nuevoUsuario.getNickname()] = nuevoUsuario


    def obtenerUsuario(self, nickname):
        return self.__MAPUsuarios[nickname]
    
    def SETobtenerEstudiantes(self):
        nickNameestudiantes = set()
        for e in self.__MAPUsuarios.values():
            if type(e) == Estudiante:
                nickNameestudiantes.add(e.getNickname())
        return nickNameestudiantes


    #Retorna nicknames de los profesores
    def obtenerProfesores(self):
        nicknameProfesores = set()
        for p in self.__MAPUsuarios.values():
            if type(p) == Profesor:
                nicknameProfesores.add(p.getNickname())
        return nicknameProfesores
    
    def obtenerNombres():pass

    #Obtener todos los nickname
    def obtenerNickname(self):
        SETnickname = set()
        if self.__MAPUsuarios != None:
            for u in self.__MAPUsuarios:
               SETnickname.add(u)
        return SETnickname

    def obtenerNombresProfesor():pass
    def agregarCursoColeccion(curso):pass
    def aprobarEjercicio(ejercicio, nickname, nombreCurso):pass
    
