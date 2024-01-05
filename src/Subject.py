from src.Course import Course
from src.UserManager import UserManager
class Subject:
    def __init__ (self, name):
        self.__name = name
        self.__SETobservers = set()
        self.__MAPCourses = dict()
    def getName(self):
        return self.__name
    def AddSuscriptor(self, u): 
        self.__SETobservers.add(u.getNickname())
    def removerUser(Name): pass
    def getDataEnabledCourses(): pass
    def Add(observer): pass
    def  remove(self, observer):
        self.__SETobservers.remove(observer)
    def sendNotificacion(self, course):
        for o in self.__SETobservers:
            courseName = str(course)
            notification = "Nuevo Course: "+ courseName + " /  Subject: " + self.__name
            mu = UserManager()
            u = mu.getUser(o)
            u.notify(notification)

    def associateCourseSubject(self, course):
        self.__MAPCourses[course.getName()] = Course
    def removerCourse(Name): pass
   