from src.Fabrica import Fabrica
from src.DTFecha import DTFecha



def main():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    ctrCurso = a.getICurso()
    
    seguir = True
    while seguir == True:
        print("Elija los siguientes casos de usos: ")
        print(" 1- ALTA DE Asignatura")
        print(" 2- CONSULTAR Asignatura")
        print(" 3- ALTA USUARIO")
        print(" 4- CONSULTAR USUARIOS")
        print(" 5- ALTA DE CURSO")
        print(" 0- SALIR")
        eleccion = input("elección: ").strip()
        
    #ALTA Asignatura
        if eleccion == "1":
            ingresar_Asignatura = input("Ingrese Asignatura: ")
            ctrCurso.IngresarAsignatura(ingresar_Asignatura)
            conf = ctrCurso.ConfirmarAsignatura()
            if conf:
                print("El Asignatura se ingreso correctamente")
            else: print("El Asignatura ya existe")

    #CONSULTAR Asignatura
        elif eleccion == "2":
            setAsignaturas = ctrCurso.ConsultarAsignatura()
            for i in setAsignaturas:
                print(i[0].upper()+i[1:])

    #ALTA DE USUARIO:
        
        elif eleccion == "3":
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


        #CONSULTAR USUARIO:
        elif eleccion == "4":
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
        
        elif eleccion == "5":
            nicknameProfesores = ctrCurso.obtenerNickname()
            for p in nicknameProfesores:
                print(p)
            nickname = input("Ingrese el nickname del profesor: ")
            ctrCurso.seleccionarProfesor()
            nombreCurso = input("Nombre del Curso: ")
            descripcionCuros = input("Descripción del curso: ")
            nivelCurso = input("Nivel del curso (Principiante(p)/Intermedio(i)/Avanzado(a)")
            ctrCurso.ingresarDatosCurso(nombreCurso, descripcionCuros, nivelCurso)
            setIAsignaturas =  ctrCurso.obtenerAsignaturasEspecializacion()
            for i in setAsignaturas:
                print(i)
            Asignatura = input("Ingrese Asignatura: ")
            ctrCurso.seleccionarAsignatura(Asignatura)
            previa = input("Necesita cursos previos aprobados S/N: ")
            conf = False
            if previa == "s":
                conf = True
                #ctrCurso.necesitaPrevia(confirmacion) inecesaría
                colCursosHabilitados = ctrCurso.SETobtenerCursosHabilitados()
                print("Acontinuación se muestran los cursos previos, cursos creados por el mismo profesor")
                for c in colCursosHabilitados:
                    print(c)
                previas = input("Ingresa separados por coma los cursos que serán previos")
                ctrCurso.seleccionarPrevias(previas)
                ctrCurso.ConfirmarAltaCurso()
            
            


        
        elif eleccion == "0":
            seguir = False


if __name__ == "__main__":
    main()
