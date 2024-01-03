from src.User import User

class Student(User):
    def __init__(self, Nickname,  Password,  Name,  Description,  Country, DateNac):
        super().__init__(Nickname, Password, Name, Description)
        self.__country = Country
        self.__dateNac = DateNac
        self.__MAPCoursesInscriptos = dict()
        self.__MAPRegistrations = dict()
        self.__MAPsubscription = dict()
        self.__SETNotifications = set()

    def getCountry(self):
        return self.__country
    
    def getDateNac(self):
        return self.__dateNac
    
    def MAPgetCoursesInscriptos(self):
        return self.__MAPCoursesInscriptos
    
    def notify(self, DTnuevoCourse):
        self.__SETNotifications.add(DTnuevoCourse)

    def  MAPgetRegistrations(self):
        return self.__MAPRegistrations
    
    def inscribirseCourse(self, nameCourse, Course, aprobarCourse = False, f= None):
        from src.Registration import Registration
        nuevaRegistration = Registration(f, Course, self)
        if aprobarCourse:
           nuevaRegistration.setAprobada(True)
        
        self.__MAPCoursesInscriptos[nameCourse] = Course
        self.__MAPRegistrations[nameCourse] =  nuevaRegistration
        Course.enrollStudent(self)
    
    def SETGetNomAsignaturaSuscrito(self):
        nomAsignatura = set()
        for a in self.__MAPsubscription:
            nomAsignatura.add(a)
        return nomAsignatura
    
    def getNotifications(self):
        return self.__SETNotifications
    
    def removeNotifications(self):
        self.__SETNotifications.clear()

    def MAPgetCourses():pass

    def getRegistration(self,CourseName):
        return self.__MAPRegistrations[CourseName]
    
    def addSuscription(self, asignatura):
        self.__MAPsubscription[asignatura.getName()]= asignatura.getName()
    
    def removeSubscription(self, NameAsignatura):
        del self.__MAPsubscription[NameAsignatura]

    def removerCourse( nameCourse):pass
    
    