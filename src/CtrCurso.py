from copy import copy
from src.ICurso import ICurso
from src.ManejadorAsignatura import ManejadorAsignatura
from src.ManejadorUsuario import ManejadorUsuario
from src.asignatura import Asignatura
from src.ManejadorCurso import ManejadorCurso
from src.Curso import Curso
from src.Leccion import Leccion
class CtrCurso(ICurso) :
    def __init__(self):
       self.__profRec = None
       self.__nombreCursoRec = None
       self.__descripcionRec = None
       self.__dificultadRec= None
       self.__AsignaturaRec= None
       self.__necesitaPreviaRec= False
       self.__SETpreviasRec= None
       self.__MAPleccionesRec= dict()
       self.__canLecciones = None
       self.__ultimaLeccion= None
       self.__cursoRecAgregar = None
       self.__temaRec= None
       self.__objetivoRec= None
       self.__tipoejercicioRec= None
       self.__descripcionEjRec= None
       self.__fraseEjRec= None
       self.__MAPsolucionFCRec= None
       self.__solucionTRec= None
       self.__MAPejerciciosNuevos= None
       self.__leccionSeleccionada= None
       self.__nombreRecordado= None
       self.__MAPcursosRecordados= None
     
    #Alta Curso
    def obtenerNickname(self):
        mu = ManejadorUsuario()
        nickNamesProfesores = mu.obtenerProfesores()
        return nickNamesProfesores

    
    def ExisteCurso(self, nombreCurso):
        mc = ManejadorCurso()
        return mc.ExisteCurso(nombreCurso)
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
    
    def seleccionarLeccion(self, orden, nombreCurso):
        mc = ManejadorCurso()
        self.__ultimaLeccion = mc.obtenerLeccion(nombreCurso, orden)

    def necesitaPrevia(self, confirmacion):
        self.__necesitaPreviaRec = confirmacion
    
    def SETobtenerCursosHabilitados(self):
        return self.__profRec.SETgetDataCursosHab(self.__AsignaturaRec)
    
    def seleccionarPrevias(self, cadena):
        c = cadena.replace(" ","")
        previas = c.split(',')
        mc = ManejadorCurso()
        cursosPrevios = mc.SETobtenerCursos(previas)
        self.SETpreviasRec = cursosPrevios
        



    
    def crearLeccion(self, tema, objetivo, cursoNombre):
        mc = ManejadorCurso()
        curso = mc.obtenerCurso(cursoNombre)
        n = curso.getCantLecciones() + 1
        self.__ultimaLeccion =  Leccion(n, tema, objetivo)
        self.__MAPleccionesRec[n]= self.__ultimaLeccion

    def crearEjercicioCompletarPalabra(self, descripcion,frase, MAPrespuesta):
        self.__ultimaLeccion.añadirEjercicioCompletar(descripcion, frase, MAPrespuesta)

    def crearEjercicioMultipleOpcion(self, descripcion,pregunta, opciones, opcionCorrecta):
        self.__ultimaLeccion.añadirEjercicioMultiple(descripcion,pregunta, opciones, opcionCorrecta)

    def ConfirmarAltaCurso(self):
        nuevoCurso = Curso(self.__nombreCursoRec, self.__descripcionRec, self.__dificultadRec,
                           self.__profRec, self.__AsignaturaRec)
        self.__profRec.asociarCursoProfesor(nuevoCurso)
        if self.__necesitaPreviaRec:
            for p in self.SETpreviasRec:
                nuevoCurso.añadirPrevia(p)
        self.__AsignaturaRec.asociarCursoAsignatura(nuevoCurso)
        mc = ManejadorCurso()
        mc.agregarCurso(nuevoCurso)
        nuevoCurso.setProfesor(self.__profRec)

    #Agregar leccion
    #Curso no habilitados de un profesor de nickname "nickname"
    def SETObtenerCursosNoHabilitados(self, nickname):
        mu = ManejadorUsuario()
        prof = mu.obtenerUsuario(nickname)
        return prof.SETobtenerCursosNoHabilitados()
    
    def seleccionarCurso(self, nombreCurso):
        mc = ManejadorCurso()
        self.__cursoRecAgregar = mc.obtenerCurso(nombreCurso)
        
    
    def crearDatosLeccion(self, tema, objetivo):
        self.__temaRec = tema
        self.__objetivoRec = objetivo
    
    def ingresarFraseCompletar(frase, MAPsolucion): pass
    
    def DarDeAltaEjercicio():
        pass
    
    def DarDeAltaLeccion(self):
        lec = self.__ultimaLeccion
        self.__cursoRecAgregar.añadirLeccion( Leccion(lec.getOrden(), lec.getTema(), lec.getObjetivo()))
        self.__MAPleccionesRec.clear()
        self.__ultimaLeccion = None

    #Agregar ejercicio
    
    def MAPobtenerLecciones(self):
        lecciones = self.__cursoRecAgregar.MAPgetLecciones()
        return lecciones
    
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
    
    def habilitarCurso(self):
        correcto = False
        if self.__cursoRecAgregar.getCantLecciones()!= 0:
            lecciones = self.__cursoRecAgregar.MAPgetColLecciones()
            cantidadLecciones = 0
            for l in lecciones.values():
                if l.getCantEjercicios()==0:
                    break
                else:
                    cantidadLecciones +=1
            if cantidadLecciones == self.__cursoRecAgregar.getCantLecciones():
                correcto = True
                self.__cursoRecAgregar.setHabilitar()
                
        return correcto


                


    #Consultar curso
    
    def obtenerCurso(nombreCurso): pass
    
    def  MAPobtenerLeccionesDeCurso(): pass
    
    def  MAPobtenerEjercicios(leccion): pass
    #Eliminar curso
    
    def eliminarCurso(): pass