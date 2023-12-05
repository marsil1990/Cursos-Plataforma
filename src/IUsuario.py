from abc import ABC, abstractmethod
class IUsuario(ABC):
    @abstractmethod
    def IngresarDatosUsuario(nickname, contrasena, descripcion, nombre): 
        pass
    @abstractmethod
    def  IngresarDatoEstudiante(nombrePais,fechaNacimiento):
        pass
    @abstractmethod
    def  NicknameDisponible(nickname):
        pass
    @abstractmethod
    def  AltaEstudiante():
        pass
    @abstractmethod
    def  ConfirmarAltaEstudiante():
        pass
    @abstractmethod
    def  IngresarInstituto(nombrePais):
        pass
    @abstractmethod
    def  ObtenerAsignaturasDisponibles():
        pass
    @abstractmethod
    def  AgregarEspecializacion(nombreAsignatura):
        pass
    @abstractmethod
    def  ConfirmarAltaProfesor():
        pass
    @abstractmethod
    def  AltaProfesor():
        pass
    @abstractmethod
     #CONSULTAR USUARIO
    @abstractmethod
    def ObtenerNicknameUsuarios():
        pass
    @abstractmethod
    def  seleccionarUsuario(nickname):
        pass
    @abstractmethod
    def  seleccionarEstudiante(nickname):
        pass
    @abstractmethod
    def seleccionarProfesor(nickname):
        pass
     #CONSULTAR NOTIFICACIONES
    @abstractmethod
    def  IngresarNickname(nickname):
        pass
    @abstractmethod
    def  obtenerNotificaciones():
        pass
    @abstractmethod
    def  EliminarNotifiaciones():
        pass
     #SUSCRIBIRSE A NOTIFIACIONES
    @abstractmethod
    def ObtenerAsignaturaNoSuscripto(nickname):
        pass
    @abstractmethod
    def  AgreagarSuscripcion(nomAsignatura):
        pass
    @abstractmethod
    def  existeAsignatura(Asignatura):
        pass
     #ElIMIAR SUSCRIPCIÓN
    @abstractmethod
    def obtenerSuscripciones(nickname):
        pass
    @abstractmethod
    def  seleccionarSuscripciones(setString):
        pass
    @abstractmethod
    def  eliminarSuscripciones():
        pass
     #INSCRIBIRSE A CURSO
    @abstractmethod
    def  ObtenerCursosHabilitadosParaInscripcion(nickName):
        pass
    @abstractmethod
    def  IngresarCursoSeleccionado(nombreCurso):
        pass
    @abstractmethod
    def  FinalizarInscripcionACurso(nickname, fecha = None, aprobado = False):
        pass
    #REALIZAR EJERCICIO
    @abstractmethod
    def  existeUsuario(nickname):
        pass
    @abstractmethod
    def  recordarUsuario(nickname):
        pass
    def  obtenerCursosInscriptoNoAprobado():
        pass
    @abstractmethod
    def  obtenerEjerciciosNoAprobados():
        pass
    @abstractmethod
    def  recordarEjercicio(numero, ejercicio):
        pass
    @abstractmethod
    def  mostrarEjercicio():
        pass
    @abstractmethod
    def  mostrarEjercicioaux():
        pass
    @abstractmethod
    def  resolverCompletarPalabra(map, Conjunto_solucion, imprimir=False):
        pass
    @abstractmethod
    def  resolverMultipleOpcion(solucion, imprimir=False):
        pass
    @abstractmethod
    def cantidadPalabrasACompletar():
        pass
    
