from src.Course import Course
class Subject:
    def __init__ (self, Name):
        self.__name = Name
        self.__SETobservers = set()
        self.__MAPCourses = dict()
    def getName(self):
        return self.__name
    def AddSuscriptor(self, u): 
        self.__SETobservers.add(u.getNickname())
    def removerUser(Name): pass
    def getDataEnabledCourses(): pass
    def Add(observer): pass
    def eliminar(self, observer):
        self.__SETobservers.remove(observer)
    def EnviarNotificacion(self, Course):
        for o in self.__SETobservers:
            CourseName = str(Course)
            notificacion = "Nuevo Course: "+ CourseName + " /  Subject: " + self.__name
            o.notify(notificacion)

    def asociarCourseSubject(self, Course):
        self.__MAPCourses[Course.getName()] = Course
    def removerCourse(Name): pass
   