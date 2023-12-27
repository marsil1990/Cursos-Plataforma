from src.Student import Student
class Registration:
    def __init__(self, Date, Course, Student):
        self.__UltimaLessonAprobada = None
        self.__DateDeRegistration = Date 
        self.__CourseInscripto = Course
        self.__aprobada = False
        self.__StudentInscripto = Student

    def getUltimaLessonAprobada(self):
        return self.__UltimaLessonAprobada
    def getDateDeRegistration(self):
        return self.__DateDeRegistration
    def getAprobada(self):
        return self.__aprobada 
    def getCourseInscripto(self):
        return self.__CourseInscripto
    def getStudentInscripto(self):
        return self.__StudentInscripto
    def setAprobada(self, aprobada):
        self.__aprobada = aprobada    
    def setNuevaLessonAprobada(self, Lesson):
        self.__UltimaLessonAprobada = Lesson
   