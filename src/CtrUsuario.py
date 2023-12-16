from src.IUsuario import IUsuario
from src.DTFecha import DTFecha
from src.DTCurso import DTCurso
from src.ManejadorUsuario import ManejadorUsuario
from src.Estudiante import Estudiante
from src.DTEstudiante import DTEstudiante
from src.Profesor import Profesor
from src.DTProfesor import DTProfesor
from src.ManejadorAsignatura import ManejadorAsignatura
from src.ManejadorCurso import ManejadorCurso
from src.DTInscripcion import DTInscripcion
from src.DTEjercicio import DTEjercicio
from src.CompletarPalabra import CompletarPalabra
from src.MultiOpcion import MultiOpcion
class CtrUsuario(IUsuario):
    __instancia = None
    __nickNameRec = None
    __nombreCursoRec = None
    __cursoRecordado =  None
    __nuevoUsuarioNicknameRec = None
    __nuevoUsuarioContrasenia = None
    __nuevoUsuarioDescripcion= None
    __nuevoUsuarioNombreRec= None
    __nuevoUsuarioNombrePaisRec= None
    __nuevoUsuarioFechaNacimientoRec= None
    __nuevoUsuarioInstitutoRec= None
    __SETnuevoUsuarioEspecializacion = None 
    __SETAsignaturasRecordados = set()
    __usuarioRecordado = None
    __ejercicioRecordado = None
    __ejercicioMultipleOpcion= None
    __ejercicioDeCompletarPalabra = None
    __leccionRecordada = None
    __estudianteRecordar = None

    
    
    def __new__(cls):
        if CtrUsuario.__instancia is None:
           CtrUsuario.__instancia = object.__new__(cls)
        return CtrUsuario.__instancia
    
    
    
    
    #public
    #ALTA USUARIO
    def IngresarDatosUsuario(self, nickname, contrasena, descripcion, nombre): 
        self.__nuevoUsuarioNicknameRec = nickname
        self.__nuevoUsuarioContrasenia = contrasena
        self.__nuevoUsuarioDescripcion = descripcion
        self.__nuevoUsuarioNombreRec = nombre
    
    def  IngresarDatoEstudiante(self, nombrePais,fechaNacimiento):
        self.__nuevoUsuarioNombrePaisRec = nombrePais
        self.__nuevoUsuarioFechaNacimientoRec = fechaNacimiento

    #Devuelve true si el nickname ya esta
    def  NicknameDisponible(self, nickname):
        mu = ManejadorUsuario()
        if mu.ExisteUsuario(nickname):
           return True
        else:
            return False

    def  AltaEstudiante(self):
        mu = ManejadorUsuario()
        nuevoEstudiante = Estudiante(self.__nuevoUsuarioNicknameRec, self.__nuevoUsuarioContrasenia,
                                     self.__nuevoUsuarioNombreRec, self.__nuevoUsuarioDescripcion,
                                     self.__nuevoUsuarioNombrePaisRec, self.__nuevoUsuarioFechaNacimientoRec)
        mu.agregarUsuario(nuevoEstudiante)
    
    def  ConfirmarAltaEstudiante(self):
        if not self.NicknameDisponible(self.__nuevoUsuarioNicknameRec):
            self.AltaEstudiante()

    
    def  IngresarInstituto(self, nombreInstituto):
        self.__nuevoUsuarioInstitutoRec= nombreInstituto
    
    def  ObtenerAsignaturasDisponibles(self):
        mi = ManejadorAsignatura()
        Asignaturas = mi.SETAsignaturasDisponibles()
        return Asignaturas
    
    def  AgregarEspecializacion(self, nombreAsignatura):
        self.__SETAsignaturasRecordados.add(nombreAsignatura)
    
    def  ConfirmarAltaProfesor(self):
        mu = ManejadorUsuario()
        prof = Profesor(self.__nuevoUsuarioNicknameRec, self.__nuevoUsuarioContrasenia, self.__nuevoUsuarioNombreRec,
                        self.__nuevoUsuarioDescripcion, self.__nuevoUsuarioInstitutoRec)
        for i in self.__SETAsignaturasRecordados:
           prof.AgregarEspecializacion(i)
        mu.agregarUsuario(prof)
    
    def  AltaProfesor():
        pass
    
     #CONSULTAR USUARIO
    
    def ObtenerNicknameUsuarios(self):
        mu = ManejadorUsuario()
        SETnicknameUsuarios = mu.obtenerNickname()
        return SETnicknameUsuarios
    
    def  seleccionarUsuario(self, nickname):
        mu = ManejadorUsuario()
        usuario = mu.obtenerUsuario(nickname)
        if type(usuario)== Profesor :
            prof = self.seleccionarProfesor(nickname)
            print(f"Nombre: {prof.getNombre()}")
            print(f"Descripción: {prof.getDescripcion()}")
            print(f"Instituto: {prof.getInstituto()}")
            Asignaturas = usuario.SETobtenerEspecializaciones()
            for i in Asignaturas:
                print(f"Asignatura: {i}")
        elif type(usuario)== Estudiante: 
            es = self.seleccionarEstudiante(nickname)
            print(f"Nombre: {es.getNombre()}")
            print(f"Descripción: {es.getDescripcion()}")
            print(f"Pais: {es.getPais()}")
            print(f"Fecha de Nacimiento: {es.getFecha().getDia()} /{es.getFecha().getMes()}/{es.getFecha().getAno()} ")



    
    def  seleccionarEstudiante(self, nickname):
        mu = ManejadorUsuario()
        estudiante = mu.obtenerUsuario(nickname)
        es = DTEstudiante(estudiante.getNickname(), estudiante.getContrasena(),
                          estudiante.getNombre(), estudiante.getDescripcion(), 
                          estudiante.getPais(), estudiante.getFechaNac())
        return es

    
    def seleccionarProfesor(self, nickname):
        mu = ManejadorUsuario()
        profesor = mu.obtenerUsuario(nickname)
        prof = DTProfesor(profesor.getNickname(), profesor.getContrasena(),
                          profesor.getNombre(), profesor.getDescripcion(), 
                          profesor.getInstituto())
        return prof
     #CONSULTAR NOTIFICACIONES
    
    def  IngresarNickname(self, nickname):
        self.__nickNameRec = nickname
    
    def  obtenerNotificaciones(self, nickname):
        mu = ManejadorUsuario()
        ususario = mu.obtenerUsuario(nickname=nickname)
        notificaciones =  ususario.SETDevolverNotificaciones()
        return notificaciones
    
    def  EliminarNotifiaciones(self, nickname):
        mu = ManejadorUsuario()
        usuario = mu.obtenerUsuario(nickname=nickname)
        usuario.elimiarNotificaciones()
     #SUSCRIBIRSE A NOTIFIACIONES
    
    def ObtenerAsignaturaNoSuscripto(self, nickname):
        mu = ManejadorUsuario()
        ma = ManejadorAsignatura()
        usuario = mu.obtenerUsuario(nickname=nickname)
        asignaturaSuscrito = usuario.SETObtenerNomAsignaturaSuscrito()
        asignaturaDiponible = ma.SETAsignaturasDisponibles()
        asignaturasSuscripciones = set()
        for a in asignaturaDiponible:
            if not a in asignaturaSuscrito:
                asignaturasSuscripciones.add(a)
        return asignaturasSuscripciones



    
    def  AgreagarSuscripcion(self, nickname, nomAsignatura):
        mu = ManejadorUsuario()
        ma = ManejadorAsignatura()
        usuario = mu.obtenerUsuario(nickname=nickname)
        asignatura = ma.obtenerAsignatura(nombreAsignatura=nomAsignatura)
        usuario.agreagarSuscripcion(asignatura)
        asignatura.AgregarSuscriptor(usuario)
    
    def  existeAsignatura(self, asign):
        mi = ManejadorAsignatura()
        return mi.existeAsignatura(asign)
    
     #ElIMIAR SUSCRIPCIÓN
    
    def obtenerSuscripciones(self, nickname):
        mu = ManejadorUsuario()
        usuario = mu.obtenerUsuario(nickname=nickname)
        suscripciones = usuario.SETObtenerNomAsignaturaSuscrito()
        return suscripciones
    
    def  eliminarSuscripciones(self, nickname, eleccionAsignatura):
        ma = ManejadorAsignatura()
        mu = ManejadorUsuario()
        asignatura = ma.obtenerAsignatura(eleccionAsignatura)
        usuario = mu.obtenerUsuario(nickname=nickname)
        usuario.eliminarSuscripcion(eleccionAsignatura)
        asignatura.eliminar(nickname)
    

        
     #INSCRIBIRSE A CURSO
    
    def  ObtenerCursosHabilitadosParaInscripcion(self, nickname):
        mc = ManejadorCurso()
        mu = ManejadorUsuario()
        estudiante = mu.obtenerUsuario(nickname)
        cursosInscriptos = estudiante.MAPObtenerCursosInscriptos()
        nombreCursos = mc.SETobtenerCursosDisponibles()
        listNombreCursos = []
        for curDis in nombreCursos:
            listNombreCursos.append(curDis)
        cursos = mc.SETobtenerCursos(listNombreCursos)
        cursosHabilitados = set()
        cursosDisponibles = set()
        for c in cursos:
            if c.getHabilitado():
                cursosHabilitados.add(c)
        #//Si no existe cursos Habilitado con el null indicamos que no existe cursos para inscribirse.
        if len(cursosHabilitados)==0:
            return cursosHabilitados
        
        #itero en todos los cursos habilitados
        for c in cursosHabilitados:
            #si tengo cursos inscriptos
            if len(cursosInscriptos) != 0 and not (c.getNombre() in cursosInscriptos):
                MAPprevias = c.getPrevias()
                tieneLasPrevias = True
                if len(MAPprevias) != 0:
                    for p in MAPprevias:
                        if not p in cursosInscriptos:
                            tieneLasPrevias = False
                        else:
                            if not estudiante.getInscripcion(p).getAprobada():
                                tieneLasPrevias = False
                if tieneLasPrevias:
                    cursoDisponible = DTCurso(curso=c)
                    cursosDisponibles.add(cursoDisponible)
            else:
                if len(cursosInscriptos)==0: 
                    previas = c.getPrevias()
                    if len(previas) == 0:
                        cursoDisponible = DTCurso(curso=c)
                        cursosDisponibles.add(cursoDisponible)
     
        return cursosDisponibles
    
    def  IngresarCursoSeleccionado(self, nombreCurso):
        self.__nombreCursoRec = nombreCurso
    
    def  FinalizarInscripcionACurso(self, nickname, fecha = None, aprobado = False):
        mu = ManejadorUsuario()
        mc = ManejadorCurso()
        try:
           estudiante = mu.obtenerUsuario(nickname)
           curso = mc.obtenerCurso(self.__nombreCursoRec);
           estudiante.inscribirseCurso(curso.getNombre(),curso, aprobado, fecha)
           return True
        except:
           return False


    #REALIZAR EJERCICIO
    
    def  existeUsuario(nickname):
        pass
    
    def  recordarUsuario(nickname):
        pass
    def  obtenerCursosInscriptoNoAprobado(self, nickname):
        mu = ManejadorUsuario()
        estudiante = mu.obtenerUsuario(nickname)
        self.__estudianteRecordar = estudiante
        cursosInscriptos= estudiante.MAPgetInscripciones()
        cursosInscriptosNoAprobados = set()
        for i in cursosInscriptos.values():
            if i.getAprobada() == False :
                cursosInscriptosNoAprobados.add(DTInscripcion(inscripcion=i))
        return cursosInscriptosNoAprobados


    
    def  obtenerEjerciciosNoAprobados(self):
        mc = ManejadorCurso()
        mu = ManejadorUsuario()
        est = mu.obtenerUsuario(self.__nickNameRec)
        inscripcion = est.getInscripcion(self.__nombreCursoRec)
        ultimaLeccionAprobada = inscripcion.getUltimaLeccionAprobada()
        cur = mc.obtenerCurso(self.__nombreCursoRec)
        self.__cursoRecordado = cur
        ejerciciosNoAprobados = set()
        if ultimaLeccionAprobada is not None:
            orden = ultimaLeccionAprobada.getOrden()
            nextLeccion = cur.obtenerLeccion(orden + 1)
            self.__leccionRecordada = nextLeccion
            ejercicios = nextLeccion.MAPgetColEjercicios()
            for e in ejercicios.values():
                if not e.esAprovado(self.__nickNameRec):
                    ejerciciosNoAprobados.add(DTEjercicio(ejercicio=e))
            return ejerciciosNoAprobados
        else:
            nextLeccion = cur.obtenerLeccion(1)
            self.__leccionRecordada = nextLeccion
            ejercicios = nextLeccion.MAPgetColEjercicios()
            for e in ejercicios.values():
                if not e.esAprovado(self.__nickNameRec):
                    ejerciciosNoAprobados.add(DTEjercicio(ejercicio=e))
            return ejerciciosNoAprobados
                


        
    
    def  recordarEjercicio(self, Id):
        self.__ejercicioRecordado = Id
    
    def  mostrarEjercicio(self):
        ej = self.__leccionRecordada.obtenerEjercicio(self.__ejercicioRecordado)
        if type(ej)== CompletarPalabra:
            self.__ejercicioDeCompletarPalabra=ej
            print("Completar: ")
            print(f"frase: {ej.getFrase()}")
            return True
        else:
            self.__ejercicioMultipleOpcion = ej
            print("Elije la opción correcta: ")
            opciones = ej.getOpciones()
            print (f"Problema o ejercicio:\n {ej.getOracion()}")
            for ok, ov in opciones.items():
                print(f"Opción {ok}: {ov}")
            return False
        
         

    
    def  mostrarEjercicioaux():
        pass
    
    def  resolverCompletarPalabra(self, conjunto_solucion):
        if self.__ejercicioDeCompletarPalabra.ingresarSolucion(conjunto_solucion):
            inscripcion = self.__estudianteRecordar.getInscripcion(self.__nombreCursoRec)
            self.__ejercicioDeCompletarPalabra.addEstudianteAprobado(self.__nickNameRec, inscripcion)
            ejercicios = self.__leccionRecordada.MAPgetColEjercicios()
            cantEjer = self.__leccionRecordada.getCantEjercicios()
            orden = self.__leccionRecordada.getOrden()
            cantAprobados = 0
            for e in ejercicios.values():
                if e.esAprovado(self.__nickNameRec):
                    cantAprobados +=1
            if cantAprobados == cantEjer:
                inscripcion.setNuevaLeccionAprobada(self.__leccionRecordada)
            if self.__cursoRecordado.getCantLecciones() == orden:
                inscripcion.setAprobada(True)
            return True
        else:
            return False


    def  resolverMultipleOpcion(self, solucion):
        if self.__ejercicioMultipleOpcion.getOpcionCorrecta() == solucion:
            inscripcion = self.__estudianteRecordar.getInscripcion(self.__nombreCursoRec)
            self.__ejercicioMultipleOpcion.addEstudianteAprobado(self.__nickNameRec, inscripcion)
            ejercicios = self.__leccionRecordada.MAPgetColEjercicios()
            cantEjer = self.__leccionRecordada.getCantEjercicios()
            orden = self.__leccionRecordada.getOrden()
            cantAprobados = 0
            for e in ejercicios.values():
                if e.esAprovado(self.__nickNameRec):
                    cantAprobados +=1
            if cantAprobados == cantEjer:
                inscripcion.setNuevaLeccionAprobada(self.__leccionRecordada)
            if self.__cursoRecordado.getCantLecciones() == orden:
                inscripcion.setAprobada(True)
            return True
        else: return False
        
    
    def cantidadPalabrasACompletar(self):
        return self.__ejercicioDeCompletarPalabra.getCantidadPalabras()

    #def __del__(): pass