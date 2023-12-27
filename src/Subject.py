from src.Course import Course
class Subject:
    def __init__ (self, Name):
        self.__Name = Name
        self.__SETobservers = set()
        self.__MAPCourses = dict()
    def getName(self):
        return self.__Name
    def AddSuscriptor(self, u): 
        self.__SETobservers.add(u.getNickname())
    def removerUser(Name): pass
    def SETgetDataCoursesHab(): pass
    def Add(observer): pass
    def eliminar(self, observer):
        self.__SETobservers.remove(observer)
    def EnviarNotificacion(self, Course):
        for o in self.__SETobservers:
            CourseName = str(Course)
            notificacion = "Nuevo Course: "+ CourseName + " /  Subject: " + self.__Name
            o.Notify(notificacion)

    def asociarCourseSubject(self, Course):
        self.__MAPCourses[Course.getName()] = Course
    def removerCourse(Name): pass
   