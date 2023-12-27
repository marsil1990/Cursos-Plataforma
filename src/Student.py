from src.User import User

class Student(User):
    def __init__(self, Nickname,  Password,  Name,  Description,  Country, DateNac):
        super().__init__(Nickname, Password, Name, Description)
        self.__Country = Country
        self.__DateNac = DateNac
        self.__MAPCoursesInscriptos = dict()
        self.__MAPRegistrations = dict()
        self.__MAPsuscrito = dict()
        self.__SETNotifications = set()

    def getCountry(self):
        return self.__Country
    
    def getDateNac(self):
        return self.__DateNac
    
    def MAPGetCoursesInscriptos(self):
        return self.__MAPCoursesInscriptos
    
    def Notify(self, DTnuevoCourse):
        self.__SETNotifications.add(DTnuevoCourse)

    def  MAPgetRegistrations(self):
        return self.__MAPRegistrations
    
    def inscribirseCourse(self, NameCourse, Course, aprobarCourse = False, f= None):
        from src.Registration import Registration
        nuevaRegistration = Registration(f, Course, self)
        if aprobarCourse:
           nuevaRegistration.setAprobada(True)
        
        self.__MAPCoursesInscriptos[NameCourse] = Course
        self.__MAPRegistrations[NameCourse] =  nuevaRegistration
        Course.inscribirStudent(self)
    
    def SETGetNomAsignaturaSuscrito(self):
        nomAsignatura = set()
        for a in self.__MAPsuscrito:
            nomAsignatura.add(a)
        return nomAsignatura
    
    def SETDevolverNotifications(self):
        return self.__SETNotifications
    
    def elimiarNotifications(self):
        self.__SETNotifications.clear()

    def MAPGetCourses():pass

    def getRegistration(self,CourseName):
        return self.__MAPRegistrations[CourseName]
    
    def agreagarSuscripcion(self, asignatura):
        self.__MAPsuscrito[asignatura.getName()]= asignatura.getName()
    
    def eliminarSuscripcion(self, NameAsignatura):
        del self.__MAPsuscrito[NameAsignatura]

    def removerCourse( NameCourse):pass
    
    