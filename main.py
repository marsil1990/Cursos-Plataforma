from src.Fabrica import Fabrica
from src.DTFecha import DTFecha

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
    tipoUsuario = input("Eres profesor o estudiante (p/e)")
    ctrUsuario.IngresarDatosUsuario(nickname,contrasena,nombre,descripcion)
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
            cont = input("Deseas agregar otro Asignatura S/N")
            if cont.strip().lower() ==  "n":
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
    Asignatura = input("Ingrese Asignatura: ")
    while (not(Asignatura in setAsignaturas)):
        Asignatura = input("Incorrecto, Ingrese Asignatura nuevamente: ")
    ctrCurso.seleccionarAsignatura(Asignatura)
    previa = input("Necesita cursos previos aprobados S/N: ")
    conf = False
    if previa.strip().lower() == "s":
        conf = True
        ctrCurso.necesitaPrevia(conf) 
        colCursosHabilitados = ctrCurso.SETobtenerCursosHabilitados()
        print("Cursos creados por el mismo profesor")
        for c in colCursosHabilitados:
            print(c)
        previas = input("Ingresa separados por coma los cursos que serán previos")
        ctrCurso.seleccionarPrevias(previas)
    ctrCurso.ConfirmarAltaCurso()
    agregarLecciones = input("Quieres agregar lecciones S/N: ")
    while agregarLecciones.strip().lower() =="s":
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
                soluciones = dict()
                continuarAgregandoPalabras = True
                espacio = 1
                while continuarAgregandoPalabras:
                    palabra = input(f"Ingrese la palabra para el espacio número {espacio}")
                    soluciones[espacio] = palabra
                    espacio += 1
                    continueAgregando = input("Desea continuar agregando palabras Si/No: ")
                    if continueAgregando.strip().lower() == "no":
                        continuarAgregandoPalabras = False
                        espacio = 1
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
            soluciones = dict()
            continuarAgregandoPalabras = True
            espacio = 1
            while continuarAgregandoPalabras:
                palabra = input(f"Ingrese la palabra para el espacio número {espacio}")
                soluciones[espacio] = palabra
                espacio += 1
                continueAgregando = input("Desea continuar agregando palabras Si/No: ")
                if continueAgregando.strip().lower() == "no":
                    continuarAgregandoPalabras = False
                    espacio = 1
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
            soluciones = dict()
            continuarAgregandoPalabras = True
            espacio = 1
            while continuarAgregandoPalabras:
                palabra = input(f"Ingrese la palabra para el espacio número {espacio}")
                soluciones[espacio] = palabra
                espacio += 1
                continueAgregando = input("Desea continuar agregando palabras Si/No: ")
                if continueAgregando.strip().lower() == "no":
                    continuarAgregandoPalabras = False
                    espacio = 1
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


def realizarEjercicio(): pass



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
            realizarEjercicio()
            
        elif eleccion == "0":
            seguir = False


if __name__ == "__main__":
    main()
