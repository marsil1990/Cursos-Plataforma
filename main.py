from src.Fabrica import Fabrica
from src.DTFecha import DTFecha



def main():
    a = Fabrica()
    ctrUsuario = a.getIUsuario()
    ctrCurso = a.getICurso()
    
    seguir = True
    while seguir == True:
        print("Elija los siguientes casos de usos: ")
        print(" 1- ALTA DE IDIOMA")
        print(" 2- CONSULTAR IDIOMA")
        print(" 3- ALTA USUARIO")
        print(" 4- CONSULTAR USUARIOS")
        print(" 5- ALTA DE CURSO")
        print(" 0- SALIR")
        eleccion = input("elección: ").strip()
        
    #ALTA IDIOMA
        if eleccion == "1":
            ingresar_idioma = input("Ingrese idioma: ")
            ctrCurso.IngresarIdioma(ingresar_idioma)
            conf = ctrCurso.ConfirmarIdioma()
            if conf:
                print("El idioma se ingreso correctamente")
            else: print("El idioma ya existe")

    #CONSULTAR IDIOMA
        elif eleccion == "2":
            setIdiomas = ctrCurso.ConsultarIdioma()
            for i in setIdiomas:
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
                setIdiomasDisponibles = ctrUsuario.ObtenerIdiomasDisponibles()
                #mostrar los idiomas
                for i in setIdiomasDisponibles:
                    print(i)
                continuar = True
                while continuar:
                    especializacion = input("Elige idioma diponible: ")
                    if ctrUsuario.existeIdioma(especializacion):
                       ctrUsuario.AgregarEspecializacion(especializacion)
                    else:
                        print("El idioma ingresado no es correcto, intene otra vez: ")
                    cont = input("Deseas agregar otro idioma S/N")
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
        
        elif eleccion == "0":
            seguir = False


if __name__ == "__main__":
    main()
