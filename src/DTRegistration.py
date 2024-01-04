from src.Registration import Registration
class DTRegistration:
    def __init__(self, date = None, courseIns = None, student = None, registration = None):
        if Registration is None:
            self.__dateOfRegistration = date
            self.__enrolledCourse = courseIns
            self.__enrolledStudent = student
        else:
            self.__dateOfRegistration = registration.getDateDeRegistration()
            self.__enrolledCourse = registration.getEnrolledCourse().getName()
            self.__enrolledStudent = registration.getEnrolledStudent()

    def getDateDeRegistration(self):
        return self.__dateOfRegistration
    def getEnrolledCourse(self):
        return self.__enrolledCourse
    def getEnrolledStudent(self):
        return self.__enrolledStudent