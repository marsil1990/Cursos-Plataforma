from src.Student import Student
class Registration:
    def __init__(self, date, course, student):
        self.__LastApprovedLesson = None
        self.__dateOfRegistration = date 
        self.__enrolledCourse = course
        self.__approved = False
        self.__enrolledStudent = Student

    def getUltimaLessonAprobada(self):
        return self.__LastApprovedLesson
    def getDateDeRegistration(self):
        return self.__dateOfRegistration
    def getApproved(self):
        return self.__approved 
    def getEnrolledCourse(self):
        return self.__enrolledCourse
    def getEnrolledStudent(self):
        return self.__enrolledStudent
    def setApproved(self, approved ):
        self.__approved  = approved     
    def setNewLessonApproved(self, lesson):
        self.__LastApprovedLesson = lesson
   