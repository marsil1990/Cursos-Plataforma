from src.User import User
from src.DTCourse import DTCourse
class Professor(User):

    def __init__(self, nickname, contraseña, name, description, institute):
        super().__init__(nickname, contraseña, name, description)
        self.__Institute = institute
        self.__MAPSpecialization = dict()
        self.__MAPCourses = dict()
        self.__MAPsubscription = dict()
        self.__SETNotifications = set()

    def getInstitute(self):
        return self.__Institute
    
    def AddSpecialization(self, Subject):
        self.__MAPSpecialization[Subject] = Subject

    def SETGetSpecializationes(self):
        specializationes = set()
        for e in self.__MAPSpecialization:
            specializationes.add(e)
        return specializationes

    def associateCourseProfessor(self, Course): 
        self.__MAPCourses[Course.getName()] = Course

    def getDataEnabledCourses(self, Subject):
        CoursesAvailable = set()
        for c in self.__MAPCourses.values():
            if c.getEnabled() and c.getSubject().getName() == Subject:
                #CoursesData = DTCourse(c)
                CoursesAvailable.add(c.getName())
        return CoursesAvailable


    def getCoursesNoAvailable(self):
        coursesNoAvailable = set()
        for c in self.__MAPCourses.values():
            if not c.getEnabled():
                #CoursesData = DTCourse(c)
                coursesNoAvailable.add(c.getName())
        return coursesNoAvailable
    
    def MAPCourses(self):
        return self.__MAPCourses


    def getSubscribedSubjectName(self):
        nomSubject = set()
        for a in self.__MAPsubscription:
            nomSubject.add(a.getName())
        return nomSubject
    
    def addSuscription(self, Subject):
        self.__MAPsubscription[Subject.getName()]= Subject.getName()

    def removeSubscription(self, NameSubject):
        del self.__MAPsubscription[NameSubject]  

    def getNotifications(self):
        return self.__SETNotifications
    
    def removeNotifications(self):
        self.__SETNotifications.clear()
        
    def notify(self, DTnuevoCourse):
        self.__SETNotifications.add(DTnuevoCourse)

    def deleteCourse(nameCourse):
        pass
   
