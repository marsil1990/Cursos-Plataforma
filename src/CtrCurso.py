from src.ICurso import ICurso
from src.ManejadorIdioma import ManejadorIdioma
from src.ManejadorUsuario import ManejadorUsuario
from src.Idioma import Idioma
class CtrCurso(ICurso) :
    profRec = None
    nombreCursoRec = None
    descripcionRec = None
    dificultadRec= None
    idiomaRec= None
    necesitaPreviaRec= None
    SETpreviasRec= None
    MAPleccionesRec= None
    ultimaLeccion= None
    cursoRecAgregar= None
    temaRec= None
    objetivoRec= None
    tipoejercicioRec= None
    descripcionEjRec= None
    fraseEjRec= None
    MAPsolucionFCRec= None
    solucionTRec= None
    MAPejerciciosNuevos= None
    leccionSeleccionada= None
    nombreRecordado= None
    MAPcursosRecordados= None
     
    #Alta Curso
    def obtenerNickname(self):
        mu = ManejadorUsuario()
        nickNamesProfesores = mu.obtenerProfesores()
        return nickNamesProfesores

    
    def ExisteCurso(nombreCurso): pass
    
    def seleccionarProfesor(nickname): pass
    
    def ingresarDatosCurso (nombre, descripcion, dificultad): pass
    
    def obtenerIdiomasEspecializacion(): pass
    
    def seleccionarIdioma(nombreIdioma): pass
    
    def necesitaPrevia(confirmacion): pass
    
    def SETobtenerCursosHabilitados(): pass
    
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

    #AlTA IDIOMA
    
    def IngresarIdioma(self,nombreIdioma):
        self.idiomaRec = nombreIdioma
    
    def ConfirmarIdioma(self):
        mi = ManejadorIdioma()
        if mi.existeIdioma(self.idiomaRec):
            return False
        else:
            i = Idioma(self.idiomaRec)
            mi.agregarIdioma(i)
            return True
    
    def ConsultarIdioma(self):
        mi = ManejadorIdioma()
        return mi.SETIdiomasDisponibles()
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