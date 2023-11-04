from src.ICurso import ICurso
from src.ManejadorAsignatura import ManejadorAsignatura
from src.ManejadorUsuario import ManejadorUsuario
from src.asignatura import Asignatura
class CtrCurso(ICurso) :
    def __init__(self):
       self.__profRec = None
       self.__nombreCursoRec = None
       self.__descripcionRec = None
       self.__dificultadRec= None
       self.__AsignaturaRec= None
       self.__necesitaPreviaRec= None
       self.SETpreviasRec= None
       self.MAPleccionesRec= None
       self.ultimaLeccion= None
       self.cursoRecAgregar= None
       self.temaRec= None
       self.objetivoRec= None
       self.tipoejercicioRec= None
       self.descripcionEjRec= None
       self.fraseEjRec= None
       self.MAPsolucionFCRec= None
       self.solucionTRec= None
       self.MAPejerciciosNuevos= None
       self.leccionSeleccionada= None
       self.nombreRecordado= None
       self.MAPcursosRecordados= None
     
    #Alta Curso
    def obtenerNickname(self):
        mu = ManejadorUsuario()
        nickNamesProfesores = mu.obtenerProfesores()
        return nickNamesProfesores

    
    def ExisteCurso(nombreCurso): pass
    
    def seleccionarProfesor(self, nickname): 
        mu = ManejadorUsuario()
        self.__profRec  = mu.obtenerUsuario(nickname)
        
    
    def ingresarDatosCurso (self, nombre, descripcion, dificultad):
        self.__nombreCursoRec = nombre
        self.__descripcionRec = descripcion
        self.__dificultadRec = dificultad
    
    def obtenerAsignaturasEspecializacion(self):
        AsignaturasEspecializado = self.__profRec.SETobtenerEspecializaciones()
        return AsignaturasEspecializado
        

    
    def seleccionarAsignatura(self, nombreAsignatura):
        mi = ManejadorAsignatura()
        self.__AsignaturaRec = mi.obtenerAsignatura(nombreAsignatura)
    
    def necesitaPrevia(self, confirmacion):
        self.__necesitaPreviaRec = confirmacion
    
    def SETobtenerCursosHabilitados(self):
        self.__AsignaturaRec.SETgetDataCursosHab()
    
    def seleccionarPrevias(SET): pass
    
    def crearLeccion(tema, objetivo): pass
    
    def crearEjercicioCompletarPalabra(descripcion,frase, MAPrespuesta): pass
    
    def crearEjercicioTraducir(descripcion,frase, traduccion): pass
    
    def ConfirmarAltaCurso(): pass

    #Agregar leccion
    
    def SETObtenerCursosNoHabilitados(): pass
    
    def seleccionarCurso(nombreCurso): pass
    
    def crearDatosLeccion(tema, objetivo): pass
    
    def ingresarFraseCompletar(frase, MAPsolucion): pass
    
    def DarDeAltaEjercicio(): pass
    
    def DarDeAltaLeccion(): pass

    #Agregar ejercicio
    
    def MAPobtenerLecciones(): pass
    
    def agregarEjercicio(lec, descripcion ,frase, MAPsolucion): pass
    
    def agregarEjercicio(lec, descripcion, frase, solucion): pass

    #AlTA Asignatura
    
    def IngresarAsignatura(self,nombreAsignatura):
        self.AsignaturaRec = nombreAsignatura
    
    def ConfirmarAsignatura(self):
        mi = ManejadorAsignatura()
        if mi.existeAsignatura(self.AsignaturaRec):
            return False
        else:
            i = Asignatura(self.AsignaturaRec)
            mi.agregarAsignatura(i)
            return True
    
    def ConsultarAsignatura(self):
        mi = ManejadorAsignatura()
        return mi.SETAsignaturasDisponibles()
    #Consultar Estadisticas
    
    def ObtenerEstudiantes(): pass
    
    def MAPobtenerCursosInscripto(nickname): pass
    
    def MAPobtenerAvanceCursos(): pass
    
    def ObtenerProfesores(): pass 
    
    def MAPobtenerPromedioCursos(): pass
    
    def SETobtenerCursos(): pass
    
    def obtenerPromedio(): pass
    
    def habilitarCurso(): pass
    #Consultar curso
    
    def obtenerCurso(nombreCurso): pass
    
    def  MAPobtenerLeccionesDeCurso(): pass
    
    def  MAPobtenerEjercicios(leccion): pass
    #Eliminar curso
    
    def eliminarCurso(): pass