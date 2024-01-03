from src.Registration import Registration
class DTRegistration:
    def __init__(self, date = None, courseIns = None, student = None, registration = None):
        if Registration is None:
            self.__dateDeRegistration = date
            self.__courseInscripto = courseIns
            self.__studentInscripto = student
        else:
            self.__dateDeRegistration = registration.getDateDeRegistration()
            self.__courseInscripto = registration.getCourseInscripto().getName()
            self.__studentInscripto = registration.getStudentInscripto()

    def getDateDeRegistration(self):
        return self.__dateDeRegistration
    def getCourseInscripto(self):
        return self.__courseInscripto
    def getStudentInscripto(self):
        return self.__studentInscripto