from src.Fabrica import Fabrica
from src.DTFecha import DTFecha
from datetime import datetime

def altaAsignatura():
    a = Fabrica()
    ctrCurso = a.getICurso()
    ingresar_Asignatura = input("Ingrese Asignatura: ")
    while ingresar_Asignatura.strip() == "":
        ingresar_Asignatura = input("No puede ser vacío, Ingrese Asignatura: ")
    ctrCurso.IngresarAsignatura(ingresar_Asignatura)
    conf = ctrCurso.ConfirmarAsignatura()
    if conf:
        print("El Asignatura se ingreso correctamente")
    else: print("El Asignatura ya existe")

def consultarAsignatura():
    a = Fabrica()
    ctrCurso = a.getICurso()
    setAsignaturas = ctrCurso.ConsultarAsignatura()
    for i in setAsignaturas:
        print(i[0].upper()+i[1:])


def altaUsusario():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    nickname = input("Ingresar nickname: ")
    while ctrUsuario.NicknameDisponible(nickname):
        nickname = input("nickname igresado no está disponible, ingrese otro: ")
    contrasena = input("Ingresar contraseña (minimo 6 caraceres): ")
    while len(contrasena) < 6 :
        contrasena = input("La contraseña debe tener minimo 6 caracteres, intente nuevamente: ")
    nombre = input("Ingresar nombre: ")
    descripcion = input("Ingresar descripción: ")
    tipoUsuario = input("Eres profesor o estudiante (p/e): ")
    ctrUsuario.IngresarDatosUsuario(nickname,contrasena,descripcion, nombre)
    if (tipoUsuario.lower().strip()== "e" ):
        nombrePais = input("Ingrese País donde vive: ")
        print("Ingrese fecha de nacimiento: ")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        ano = int(input("Año: "))
        fechaNacimiento = DTFecha(dia, mes, ano)
        ctrUsuario.IngresarDatoEstudiante(nombrePais,fechaNacimiento)
        ctrUsuario.ConfirmarAltaEstudiante()
    elif (tipoUsuario.lower().strip() == "p"):
        instituto = input("Ingrese instituto donde trabaja: ")
        ctrUsuario.IngresarInstituto(instituto)
        setAsignaturasDisponibles = ctrUsuario.ObtenerAsignaturasDisponibles()
        #mostrar los Asignaturas
        for i in setAsignaturasDisponibles:
            print(i)
        continuar = True
        while continuar:
            especializacion = input("Elige Asignatura diponible: ")
            if ctrUsuario.existeAsignatura(especializacion):
                ctrUsuario.AgregarEspecializacion(especializacion)
            else:
                print("El Asignatura ingresado no es correcto, intene otra vez: ")
            cont = input("Deseas agregar otro Asignatura Si/No: ")
            if cont.strip().lower() ==  "no":
                continuar = False
                    
        ctrUsuario.ConfirmarAltaProfesor()
    else:
        print("Tipo de usuario ingresado no es correcto")


def consultarUsuario():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    SETnicknameUsuarios = ctrUsuario.ObtenerNicknameUsuarios()
    if len(SETnicknameUsuarios) != 0:
        for u in SETnicknameUsuarios:
            print(u)
        nickname_usuario = input("Ingresar nickname del usuario: ")
        if(ctrUsuario.NicknameDisponible(nickname_usuario)):
            ctrUsuario.seleccionarUsuario(nickname_usuario)
        else: 
            print("El nickname ingresado no es correcto")
    else: 
        print ("No hay usuarios registrados")
    

def altaCurso():
    a = Fabrica()
    ctrCurso = a.getICurso()
    nicknameProfesores = ctrCurso.obtenerNickname()
    for p in nicknameProfesores:
        print(p)
    nickname = input("Ingrese el nickname del profesor: ")
    while(not (nickname in nicknameProfesores)):
        nickname = input("Nickname incorrecto, ingrese nickname del profesor: ")
    ctrCurso.seleccionarProfesor(nickname)
    nombreCurso = input("Nombre del Curso: ")
    while (ctrCurso.ExisteCurso(nombreCurso)):
        nombreCurso = input("Nombre del Curso ya existe, ingrese otro: ")
    descripcionCurso = input("Descripción del curso: ")
    nivelCurso = input("Nivel del curso (Principiante(p)/Intermedio(i)/Avanzado(a): ")
    while (nivelCurso.strip().lower() != "p" and nivelCurso.strip().lower() != "i" and 
            nivelCurso.strip().lower() != "a"):
        nivelCurso = input("Ingrese solo p, i o a: ")
    ctrCurso.ingresarDatosCurso(nombreCurso, descripcionCurso, nivelCurso)
    setAsignaturas =  ctrCurso.obtenerAsignaturasEspecializacion()
    for i in setAsignaturas:
        print(i)
    asignatura = input("Ingrese Asignatura: ")
    while (not(asignatura in setAsignaturas)):
        asignatura = input("Incorrecto, Ingrese Asignatura nuevamente: ")
    ctrCurso.seleccionarAsignatura(asignatura)
    previa = input("Necesita cursos previos aprobados Si/No: ")
    conf = False
    if previa.strip().lower() == "si":
        conf = True
        ctrCurso.necesitaPrevia(conf) 
        colCursosHabilitados = ctrCurso.SETobtenerCursosHabilitados()
        print("Cursos creados por el mismo profesor")
        if len(colCursosHabilitados) != 0:
            for c in colCursosHabilitados:
                 print(c)
            previas = input("Ingresa separados por coma los cursos que serán previos")
            ctrCurso.seleccionarPrevias(previas)
        else: print("No tiene curso habilitados")
    ctrCurso.ConfirmarAltaCurso()
    agregarLecciones = input("Quieres agregar lecciones Si/No: ")
    while agregarLecciones.strip().lower() =="si":
        ctrCurso.seleccionarCurso(nombreCurso)
        tema = input("Ingresar tema de la lección: ")
        objetivo = input("Ingresar objetivo de la lección: ")
        #ctrCurso.crearDatosLeccion(tema, objetivo)
        ctrCurso.crearLeccion(tema, objetivo, nombreCurso)
        agregarEjercicios = input("Quieres agregar ejercicios Si/No: ")
        while agregarEjercicios.strip().lower() == "si":
            tipoEjercicio = input("Ingresa tipo de ejercicio(solo el número): 1 - Completar, 2 - MultileOpción: ")
            if tipoEjercicio.strip() == "1":
                descripcion = input("Agrega descripción: ")
                frase = input("Ingresa la frase, en los lugares donde irían las palabras a completar escribe ---: ")
                cantCaractere = frase.count("---")
                soluciones = dict()
                espacio = cantCaractere
                while espacio > 0:
                    palabra = input(f"Ingrese la palabra para el espacio número {espacio}: ")
                    soluciones[espacio] = palabra
                    espacio -= 1
                ctrCurso.crearEjercicioCompletarPalabra(descripcion, frase, soluciones)
            elif tipoEjercicio.strip() == "2":
                descripcion = input("Agrega descripción: ")
                pregunta = input("Ingresa pregunta o problema: ")
                opcionCorrecta = input("Ingrese la opción correcta (número de la misa): ")
                opciones = dict()
                continuarAgregando = True
                op = 1
                while continuarAgregando:
                    opc = input("Ingrese una opción: ")
                    opciones[op] = opc
                    op +=1
                    continuar_agregando = input("Desea continuar agregando opciones Si/No: ")
                    if continuar_agregando.strip().lower() == "no":
                        continuarAgregando = False
                        op = 1
                ctrCurso.crearEjercicioMultipleOpcion(descripcion, pregunta, opciones, opcionCorrecta)
            else: print("Ingreso de opción incorrecta")
            agregarEjercicios = input("Quieres agregar otro ejercicio Si/No: ")
        ctrCurso.DarDeAltaLeccion()
        agregarLecciones = input("Quieres agregar otra lección S/N: ")
        

def habilitarCurso():
    a = Fabrica()
    ctrCurso = a.getICurso()
    nicknameProfesores = ctrCurso.obtenerNickname()
    nicknameProfesor = input("Ingrese nickname del profesor: ")
    while(not (nicknameProfesor in nicknameProfesores)):
        nicknameProfesor = input("Nickname incorrecto, ingrese nickname del profesor: ")
    colCursosNohabilitados =  ctrCurso.SETObtenerCursosNoHabilitados(nicknameProfesor)
    for c in colCursosNohabilitados:
        print (c)
    curso = input("Ingresar Curso: ")
    while (not ctrCurso.ExisteCurso(curso)):
        curso = input("Nombre del Curso incorrecto, ingrese nuevamente: ")
    ctrCurso.seleccionarCurso(curso)
    correcto = ctrCurso.habilitarCurso()
    if correcto:
        print("Se habilito correcamente")
    else:
        print("No se habilito")

def agregarLeccion():
    a = Fabrica()
    ctrCurso = a.getICurso()
    nicknameProfesor = input("Ingrese nickname del profesor: ")
    nicknameProfesores = ctrCurso.obtenerNickname()
    while(not (nicknameProfesor in nicknameProfesores)):
        nicknameProfesor = input("Nickname incorrecto, ingrese nickname del profesor: ")
    colCursosNohabilitados =  ctrCurso.SETObtenerCursosNoHabilitados(nicknameProfesor)
    for c in colCursosNohabilitados:
        print (c)
    curso = input("Ingresar Curso: ")
    while (not ctrCurso.ExisteCurso(curso)):
        curso = input("Nombre del Curso incorrecto, ingrese nuevamente: ")
    ctrCurso.seleccionarCurso(curso)
    tema = input("Ingresar tema de la lección: ")
    objetivo = input("Ingresar objetivo de la lección: ")
    #ctrCurso.crearDatosLeccion(tema, objetivo)
    ctrCurso.crearLeccion(tema, objetivo, curso)
    agregarEjercicios = input("Quieres agregar ejercicios Si/No: ")
    while agregarEjercicios.strip().lower() == "si":
        tipoEjercicio = input("Ingresa tipo de ejercicio(solo el número): 1 - Completar, 2 - MultileOpción: ")
        if tipoEjercicio.strip() == "1":
            descripcion = input("Agrega descripción: ")
            frase = input("Ingresa la frase, en los lugares donde irían las palabras a completar escribe ---: ")
            cantCaractere = frase.count("---")
            soluciones = dict()
            espacio = cantCaractere
            while espacio > 0:
                palabra = input(f"Ingrese la palabra para el espacio número {espacio}: ")
                soluciones[espacio] = palabra
                espacio -= 1
            ctrCurso.crearEjercicioCompletarPalabra(descripcion, frase, soluciones)
        elif tipoEjercicio.strip() == "2":
            descripcion = input("Agrega descripción: ")
            pregunta = input("Ingresa pregunta o problema: ")
            opcionCorrecta = input("Ingrese la opción correcta (número de la misa): ")
            opciones = dict()
            continuarAgregando = True
            op = 1
            while continuarAgregando:
                opc = input("Ingrese una opción: ")
                opciones[op] = opc
                op +=1
                continuar_agregando = input("Desea continuar agregando opciones Si/No: ")
                if continuar_agregando.strip().lower() == "no":
                    continuarAgregando = False
                    op = 1
            ctrCurso.crearEjercicioMultipleOpcion(descripcion, pregunta, opciones, opcionCorrecta)
        else: print("Ingreso de opción incorrecta")
        agregarEjercicios = input("Quieres agregar otro ejercicio Si/No: ")
    ctrCurso.DarDeAltaLeccion()

def agregarEjercicio():
    a = Fabrica()
    ctrCurso = a.getICurso()
    nicknameProfesor = input("Ingrese nickname del profesor: ")
    nicknameProfesores = ctrCurso.obtenerNickname()
    while(not (nicknameProfesor in nicknameProfesores)):
        nicknameProfesor = input("Nickname incorrecto, ingrese nickname del profesor: ")
    colCursosNohabilitados =  ctrCurso.SETObtenerCursosNoHabilitados(nicknameProfesor)
    for c in colCursosNohabilitados:
        print (c)
    curso = input("Ingresar Curso: ")
    while (not ctrCurso.ExisteCurso(curso)):
        curso = input("Nombre del Curso incorrecto, ingrese nuevamente: ")
    ctrCurso.seleccionarCurso(curso)
    lecciones = ctrCurso.MAPobtenerLecciones()
    for lk, lv in lecciones.items():
        print(f"{lk}:{lv}")
    orden = int(input("Ingresar lección (número): "))
    while not orden in lecciones.keys():
        orden = int(input("incorrecto, Ingresar lección número): "))
    ctrCurso.seleccionarLeccion(orden, curso)
    tipoEjercicio = input("Ingresa tipo de ejercicio(solo el número): 1 - Completar, 2 - MultileOpción: ")
    seguirAgregando = True
    while seguirAgregando == True:
        if tipoEjercicio.strip() == "1":
            descripcion = input("Agrega descripción: ")
            frase = input("Ingresa la frase, en los lugares donde irían las palabras a completar escribe ---: ")
            cantCaractere = frase.count("---")
            soluciones = dict()
            espacio = cantCaractere
            while espacio > 0:
                palabra = input(f"Ingrese la palabra para el espacio número {espacio}")
                soluciones[espacio] = palabra
                espacio -= 1
            ctrCurso.crearEjercicioCompletarPalabra(descripcion, frase, soluciones)
        elif tipoEjercicio.strip() == "2":
            descripcion = input("Agrega descripción: ")
            pregunta = input("Ingresa pregunta o problema: ")
            opcionCorrecta = input("Ingrese la opción correcta (número de la misa): ")
            opciones = dict()
            continuarAgregando = True
            op = 1
            while continuarAgregando:
                opc = input("Ingrese una opción: ")
                opciones[op] = opc
                op +=1
                continuar_agregando = input("Desea continuar agregando opciones Si/No: ")
                if continuar_agregando.strip().lower() == "no":
                    continuarAgregando = False
                    op = 1
            ctrCurso.crearEjercicioMultipleOpcion(descripcion, pregunta, opciones, opcionCorrecta)
        else: 
            tipoEjercicio = input("opción incorrecta. Ingresa tipo de ejercicio(solo el número): 1 - Completar, 2 - MultileOpción: ")
        s = input("Quiere seguir agregando ejercicios S/N: ")
        if s.strip().lower() == "n":
            seguirAgregando = False

def inscripcionCurso():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    nickname = input("Ingresar nickname: ")
    if ctrUsuario.NicknameDisponible(nickname):
        ctrUsuario.IngresarNickname(nickname)
        cursosHabilitados = ctrUsuario.ObtenerCursosHabilitadosParaInscripcion(nickname)
        if not cursosHabilitados:
            print("El estudiante no tien cursos habilitados disponibles")
        else:
            i = 1
            print("---Cursos disponibles---")
            for c in cursosHabilitados:
                print(f"{1}) curso: {c.getNombre()}")
                print(f"- Descripcion: {c.getDesc()}")
                print(f"- Cantidad de lecciones: {c.getcantLecciones()}")
                print(f"- Cantidad de ejercicios: {c.getcantEjercicios()}")

            nombreDelCurso = input("Escriba el nombre del curso: ")
            
            ctrUsuario.IngresarCursoSeleccionado(nombreDelCurso)
            fecha_actual = datetime.now()
            f = DTFecha(fecha_actual.year, fecha_actual.month, fecha_actual.day)
            inscripcionCorrecta = ctrUsuario.FinalizarInscripcionACurso(nickname, f)
            if inscripcionCorrecta:
                print( "Se realizo correctamente la inscripcion.")
            
            else:
               print("Surgio un problema durante la inscripcion pruebe nuevamente.");
            
    else: print("No existe usuario con ese nickname")

def consultarCurso():
    a = Fabrica()
    ctrCurso = a.getICurso()
    cursos = ctrCurso.SETobtenerCursos()
    for c in cursos:
        print(c.getNombre())
    curso  =  input("Ingrese nombre del curso: ")
    while (not ctrCurso.ExisteCurso(curso)):
        curso = input("Nombre del Curso incorrecto, ingrese nuevamente: ")
    cursoDt = ctrCurso.obtenerCurso(curso)
    print(f"Nombre del curso: {cursoDt.getNombre()}")
    print(f"Dificultad del curso: {cursoDt.getDificultad()}")
    print(f"Asignatura: {cursoDt.getNombreAsignatura()}")
    print(f"Habilitado: {cursoDt.getHabilitado()}")
    if cursoDt.getcantLecciones()!= 0:
        lecciones = cursoDt.getLecciones()
        for lv in lecciones.values():
            print(f"lección número {lv.getOrden()} \n Tema: {lv.getTema()} \n Objetivo: {lv.getObjetivo()}")
            ejercicios =  lv.getEjercicios()
            if len(ejercicios) != 0:
                for ej in ejercicios.values():
                    print(f"Descripción del ejercicio: {ej.getDescripcion()}")
            else: print("No tiene ejercicios.")
    else: print("No tiene lecciones.")
    estudiantesInscriptos = cursoDt.MAPgetEstudiantesInscriptos()
    if len(estudiantesInscriptos) !=0:
        for e in estudiantesInscriptos.values():
            ins = e.getInscripcion(curso)
            fechIns = ins.getFechaDeInscripcion()
            print(f"Nombre estudiante: {e.getNombre()} \n Fecha de inscripción: {fechIns.getDia()}/{fechIns.getMes()}/{fechIns.getAno()}")
    else: 
        print("No tiene estudiantes inscriptos")

def cargarDatos():
    f = Fabrica()
    ctrCurso = f.getICurso()
    ctrUsuario = f.getIUsuario()
    #ASIGNATURA DAR ALTA
    ctrCurso.IngresarAsignatura("Matematica")
    ctrCurso.ConfirmarAsignatura()
    #USUARIO DAR ALTA (profesor)
    ctrUsuario.IngresarDatosUsuario("prof","123456","Profesor de Matemática","Prof")
    ctrUsuario.IngresarInstituto("IFD")
    ctrUsuario.AgregarEspecializacion("Matematica")
    ctrUsuario.ConfirmarAltaProfesor()
    #USUARIO DAR ALTA ESTUDIANTE
    ctrUsuario.IngresarDatosUsuario("Marcos","123456","Soy estudiante","Marcos")
    dia = 15
    mes = 12
    ano = 1990
    fechaNacimiento = DTFecha(ano, mes, dia)
    ctrUsuario.IngresarDatoEstudiante("Uruguay",fechaNacimiento)
    ctrUsuario.ConfirmarAltaEstudiante()
    #ALTA CURSO (matematica1)
    ctrCurso.seleccionarProfesor("prof")
    ctrCurso.ingresarDatosCurso("matematica1", "Ecuaciones", "p")
    ctrCurso.seleccionarAsignatura("Matematica")
    ctrCurso.necesitaPrevia(False)
    ctrCurso.ConfirmarAltaCurso()
    #AGREGAR LECCION Y EJERCICIOS A matematica1 (una 2 lecciones y 2 ejercicios en solo la lección 1)
    #LECCION 1
    #ejercicio 1 - completar
    ctrCurso.seleccionarCurso("matematica1")
    ctrCurso.crearLeccion("Ecuaciones","Resolver ecuaciones de primer grado", "matematica1")
    soluciones = dict()
    soluciones[1]="10"
    ctrCurso.crearEjercicioCompletarPalabra("Ecuaciones de primer grado", "x + 10 = 20, entonces x = ---", soluciones)
    #ejercicio 2 - multiple opción    
    opcionCorrecta = "-30"
    opciones = dict()
    opciones[1] = "-30"
    opciones[2] = "30"
    ctrCurso.crearEjercicioMultipleOpcion("Elige la opción correcta", "x + 30 = 0, entonces x = ", opciones, opcionCorrecta)
    ctrCurso.DarDeAltaLeccion()
    #LECCION2
    ctrCurso.seleccionarCurso("matematica1")
    ctrCurso.crearLeccion("Inecuaciones","Resolver inecuaciones de primer grado", "matematica1")
    ctrCurso.DarDeAltaLeccion()
    #ALTA CURSO (matematica2)
    ctrCurso.seleccionarProfesor("prof")
    ctrCurso.ingresarDatosCurso("matematica2", "Ecuaciones", "i")
    ctrCurso.seleccionarAsignatura("Matematica")
    ctrCurso.necesitaPrevia(True)
    ctrCurso.seleccionarPrevias("matematica1")
    ctrCurso.ConfirmarAltaCurso()


def realizarEjercicio():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    ctrCurso = a.getICurso()
    nickname = input("Ingresar nickname: ")
    if ctrUsuario.NicknameDisponible(nickname):
        ctrUsuario.IngresarNickname(nickname)
        cursosInscriptosNoAprobados = ctrUsuario.obtenerCursosInscriptoNoAprobado(nickname)
        print("Cursos que aún no ha aprobado: ")
        if len(cursosInscriptosNoAprobados) != 0:
            for i in cursosInscriptosNoAprobados:
                print(f"- {i.getCursoInscripto()} ")
            curso  =  input("Ingrese nombre del curso: ")
            while (not ctrCurso.ExisteCurso(curso)):
                curso = input("Nombre del Curso incorrecto, ingrese nuevamente: ")
            ctrUsuario.IngresarCursoSeleccionado(curso)
            ejerciciosNoAprobados = ctrUsuario.obtenerEjerciciosNoAprobados()
            print("Ejercicios no aprobados:")
            for e in ejerciciosNoAprobados:
                print(f"Ejercicio id: {e.getId()}, Descripción: {e.getDescripcion()}")
            
            ejercicioSeleccionar = int(input("Ingrese el identificador del ejercicio que desea realizar: "))
            ctrUsuario.recordarEjercicio(ejercicioSeleccionar)
            ej = ctrUsuario.mostrarEjercicio()
            if ej:
                r = (input("Ingresa lo faltante separado por coma: ")).replace(" ", "").split(",")
                cant = ctrUsuario.cantidadPalabrasACompletar()
                resolucion = dict()
                count = 1
                while cant >= count:
                    resolucion[count] = r[count-1]
                    count+=1
                if ctrUsuario.resolverCompletarPalabra(resolucion):
                    print("Felicitaciones, las palabras ingresadas son correctas")
                else: print("Las palabras ingresadas NO son correctas")
            else:
                opcion = input("Ingrese una de las opciones (número): ")
                if ctrUsuario.resolverMultipleOpcion(opcion):
                    print("Felicitaciones la opción igresada es la correcta")
                    
                else: print("Ingresaste la opción incorrecta: ")
        else: print("Todos los cursos han sido aprobados")
        
    else: print("Nickname incorrecto")




def main():
    seguir = True
    while seguir == True:
        print("Elija los siguientes casos de usos: ")
        print(" 1- ALTA DE ASIGNATURA")
        print(" 2- CONSULTAR ASIGNATURA")
        print(" 3- ALTA USUARIO")
        print(" 4- CONSULTAR USUARIOS")
        print(" 5- ALTA DE CURSO")
        print(" 6- HABILITAR CURSO")
        print(" 7- AGREGAR LECCIÓN")
        print(" 8- AGREGAR EJERCICIO")
        print(" 9- INSCRIBIRSE A UN CURSO")
        print(" 10- CONSULTAR CURSO")
        print(" 11- CARGAR DATOS")
        print(" 12- REALIZAR EJERCICIO")
        print(" 0- SALIR")
        eleccion = input("elección: ").strip()
        
    #ALTA Asignatura
        if eleccion == "1":
            altaAsignatura()
    #CONSULTAR Asignatura
        elif eleccion == "2":
            consultarAsignatura()
    #ALTA DE USUARIO:
        elif eleccion == "3":
            altaUsusario()
    #CONSULTAR USUARIO:
        elif eleccion == "4":
            consultarUsuario()
    
        elif eleccion == "5":
            altaCurso()
            
        elif eleccion == "6":
            habilitarCurso()
        
        elif eleccion == "7":
            agregarLeccion()
            
        elif eleccion == "8":
            agregarEjercicio()

        elif eleccion == "9":
            inscripcionCurso()

        elif eleccion == "10":
            consultarCurso()

        elif eleccion == "11":
            cargarDatos()

        elif eleccion == "12":
            realizarEjercicio()

        elif eleccion == "0":
            seguir = False


if __name__ == "__main__":
    main()
