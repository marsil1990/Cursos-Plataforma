from src.User import User

class Student(User):
    def __init__(self, nickname,  password,  name,  description,  country, dateNac):
        super().__init__(nickname, password, name, description)
        self.__country = country
        self.__dateNac = dateNac
        self.__MAPCoursesInscriptos = dict()
        self.__MAPRegistrations = dict()
        self.__MAPsubscription = dict()
        self.__SETNotifications = set()

    def getCountry(self):
        return self.__country
    
    def getBirthDate(self):
        return self.__dateNac
    
    def MAPgetEnrolledCourses(self):
        return self.__MAPCoursesInscriptos
    
    def notify(self, DTnuevoCourse):
        self.__SETNotifications.add(DTnuevoCourse)

    def  MAPgetRegistrations(self):
        return self.__MAPRegistrations
    
    def enrollInCourse(self, nameCourse, course, approveCourse = False, f= None):
        from src.Registration import Registration
        newRegistration = Registration(f, course, self)
        if approveCourse:
           newRegistration.setApproved(True)
        
        self.__MAPCoursesInscriptos[nameCourse] = course
        self.__MAPRegistrations[nameCourse] =  newRegistration
        course.enrollStudent(self)
    
    def getSubscribedSubjectName(self):
        nomAsignatura = set()
        for a in self.__MAPsubscription:
            nomAsignatura.add(a)
        return nomAsignatura
    
    def getNotifications(self):
        return self.__SETNotifications
    
    def removeNotifications(self):
        self.__SETNotifications.clear()

    def MAPgetCourses():pass

    def getRegistration(self,courseName):
        return self.__MAPRegistrations[courseName]
    
    def addSuscription(self, asignatura):
        self.__MAPsubscription[asignatura.getName()]= asignatura.getName()
    
    def removeSubscription(self, nameAsignatura):
        del self.__MAPsubscription[nameAsignatura]

    def removerCourse( nameCourse):pass
    
    