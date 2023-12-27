from src.Registration import Registration
class DTRegistration:
    def __init__(self, Date = None, CourseIns = None, Student = None, Registration = None):
        if Registration is None:
            self.__DateDeRegistration = Date
            self.__CourseInscripto = CourseIns
            self.__StudentInscripto = Student
        else:
            self.__DateDeRegistration = Registration.getDateDeRegistration()
            self.__CourseInscripto = Registration.getCourseInscripto().getName()
            self.__StudentInscripto = Registration.getStudentInscripto()

    def getDateDeRegistration(self):
        return self.__DateDeRegistration
    def getCourseInscripto(self):
        return self.__CourseInscripto
    def getStudentInscripto(self):
        return self.__StudentInscripto