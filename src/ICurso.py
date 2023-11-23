from abc import ABC, abstractmethod
class ICurso(ABC):
    #Alta Curso
    @abstractmethod
    def obtenerNickname(): pass
    @abstractmethod
    def ExisteCurso(nombreCurso): pass
    @abstractmethod
    def seleccionarProfesor(nickname): pass
    @abstractmethod
    def ingresarDatosCurso (nombre, descripcion, dificultad): pass
    @abstractmethod
    def obtenerAsignaturasEspecializacion(): pass
    @abstractmethod
    def seleccionarAsignatura(nombreAsignatura): pass
    @abstractmethod
    def necesitaPrevia(confirmacion): pass
    @abstractmethod
    def SETobtenerCursosHabilitados(): pass
    @abstractmethod
    def seleccionarPrevias(SET): pass
    @abstractmethod
    def crearLeccion(tema, objetivo): pass
    @abstractmethod
    def crearEjercicioCompletarPalabra(descripcion,frase, MAPrespuesta): pass
    @abstractmethod
    def crearEjercicioMultipleOpcion(descripcion,pregunta, opciones, opcionCorrecta): pass
    @abstractmethod
    def ConfirmarAltaCurso(): pass

    #Agregar leccion
    @abstractmethod
    def SETObtenerCursosNoHabilitados(): pass
    @abstractmethod
    def seleccionarCurso(nombreCurso): pass
    @abstractmethod
    def crearDatosLeccion(tema, objetivo): pass
    @abstractmethod
    def ingresarFraseCompletar(frase, MAPsolucion): pass
    @abstractmethod
    def DarDeAltaEjercicio(): pass
    @abstractmethod
    def DarDeAltaLeccion(): pass

    #Agregar ejercicio
    @abstractmethod
    def MAPobtenerLecciones(): pass
    @abstractmethod
    def agregarEjercicio(lec, descripcion ,frase, MAPsolucion): pass
    @abstractmethod
    def agregarEjercicio(lec, descripcion, frase, solucion): pass
    @abstractmethod
    def seleccionarLeccion(self, orden):pass

    #AlTA Asignatura
    @abstractmethod
    def IngresarAsignatura(nombreAsignatura): pass
    @abstractmethod
    def ConfirmarAsignatura(): pass
    @abstractmethod
    def ConsultarAsignatura(): pass
    #Consultar Estadisticas
    @abstractmethod
    def ObtenerEstudiantes(): pass
    @abstractmethod
    def MAPobtenerCursosInscripto(nickname): pass
    @abstractmethod
    def MAPobtenerAvanceCursos(): pass
    @abstractmethod
    def ObtenerProfesores(): pass 
    @abstractmethod
    def MAPobtenerPromedioCursos(): pass
    @abstractmethod
    def SETobtenerCursos(): pass
    @abstractmethod
    def obtenerPromedio(): pass
    @abstractmethod
    def habilitarCurso(): pass
    #Consultar curso
    @abstractmethod
    def obtenerCurso(nombreCurso): pass
    @abstractmethod
    def  MAPobtenerLeccionesDeCurso(): pass
    @abstractmethod
    def  MAPobtenerEjercicios(leccion): pass
    #Eliminar curso
    @abstractmethod
    def eliminarCurso(): pass