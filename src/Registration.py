from src.Student import Student
class Registration:
    def __init__(self, Date, Course, Student):
        self.__UltimaLessonAprobada = None
        self.__dateDeRegistration = Date 
        self.__courseInscripto = Course
        self.__aprobada = False
        self.__studentInscripto = Student

    def getUltimaLessonAprobada(self):
        return self.__UltimaLessonAprobada
    def getDateDeRegistration(self):
        return self.__dateDeRegistration
    def getAprobada(self):
        return self.__aprobada 
    def getCourseInscripto(self):
        return self.__courseInscripto
    def getStudentInscripto(self):
        return self.__studentInscripto
    def setAprobada(self, aprobada):
        self.__aprobada = aprobada    
    def setNuevaLessonAprobada(self, Lesson):
        self.__UltimaLessonAprobada = Lesson
   