from src.Course import Course
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
    def sendNotificacion(self, Course):
        for o in self.__SETobservers:
            CourseName = str(Course)
            notificacion = "Nuevo Course: "+ CourseName + " /  Subject: " + self.__name
            o.notify(notificacion)

    def associateCourseSubject(self, course):
        self.__MAPCourses[course.getName()] = Course
    def removerCourse(Name): pass
   