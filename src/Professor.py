from src.User import User
from src.DTCourse import DTCourse
class Professor(User):

    def __init__(self, nickname, contraseña, Name, Description, Institute):
        super().__init__(nickname, contraseña, Name, Description)
        self.__Institute = Institute
        self.__MAPSpecialization = dict()
        self.__MAPCourses = dict()
        self.__MAPsuscrito = dict()
        self.__SETNotifications = set()

    def getInstitute(self):
        return self.__Institute
    
    def AddSpecialization(self, Subject):
        self.__MAPSpecialization[Subject] = Subject

    def SETGetSpecializationes(self):
        Specializationes = set()
        for e in self.__MAPSpecialization:
            Specializationes.add(e)
        return Specializationes

    def asociarCourseProfessor(self, Course): 
        self.__MAPCourses[Course.getName()] = Course

    def SETgetDataCoursesHab(self, Subject):
        CoursesAvailable = set()
        for c in self.__MAPCourses.values():
            if c.getHabilitado() and c.getSubject().getName() == Subject:
                #CoursesData = DTCourse(c)
                CoursesAvailable.add(c.getName())
        return CoursesAvailable


    def SETGetCoursesNoAvailable(self):
        CoursesNoAvailable = set()
        for c in self.__MAPCourses.values():
            if not c.getHabilitado():
                #CoursesData = DTCourse(c)
                CoursesNoAvailable.add(c.getName())
        return CoursesNoAvailable
    
    def MAPCourses(self):
        return self.__MAPCourses


    def SETGetNomSubjectSuscrito(self):
        nomSubject = set()
        for a in self.__MAPsuscrito:
            nomSubject.add(a.getName())
        return nomSubject
    
    def agreagarSuscripcion(self, Subject):
        self.__MAPsuscrito[Subject.getName()]= Subject.getName()

    def eliminarSuscripcion(self, NaMonthubject):
        del self.__MAPsuscrito[NaMonthubject]  

    def SETDevolverNotifications(self):
        return self.__SETNotifications
    
    def elimiarNotifications(self):
        self.__SETNotifications.clear()
        
    def Notify(self, DTnuevoCourse):
        self.__SETNotifications.add(DTnuevoCourse)

    def deleteCourse(NameCourse):
        pass
   
