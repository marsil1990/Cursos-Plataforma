from src.DTStudent import DTStudent
from src.DTLesson import DTLesson

class DTCourse :
    def __init__(self, name=None, description=None, dificultad=None, nameProfessor=None, 
                 subject=None, estado=None, numberOfLessons=None, numberOfExercises=None, numberOfEnrollees=None, course = None):
        if course is None:
            self.__Course = None
            self.__name = name
            self.__description = description
            self.__difficulty = dificultad
            self.__nameProfessor = nameProfessor
            self.__nameSubjectCourse = subject
            self.__enabled = estado
            self.__numberOfLessons = numberOfLessons
            self.__numberOfExercises = numberOfExercises
            self.__numberOfEnrollees = numberOfEnrollees
            self.__lessons = dict()
            self.__MAPenrollment = dict()
        else:
            from src.Course import Course
            self.__name = course.getName()
            self.__description= course.getDescription()
            self.__difficulty= course.getDifficulty()
            self.__nameProfessor = course.getNameProfessor()
            self.__nameSubjectCourse = course.getSubject().getName()
            self.__enabled= course.getEnabled()
            self.__numberOfLessons = course.getcountLessons()
            self.__numberOfExercises = course.getcountExercises()
            self.__numberOfEnrollees = course.getnumberOfEnrollees()
            self.__MAPenrollment = dict()
            self.__lessons = dict()
            students = course.MAPgetStudents()
            for ek, ev in students.items():
                self.__MAPenrollment[ek] = DTStudent(Student=ev)
            lessons = course.MAPgetColLessons()
            for lk, lv in lessons.items():
                self.__lessons[lk] = DTLesson(lesson=lv)
                   
        
    def getName(self): 
        return self.__name
    def getDesc(self):
        return self.__description
    def getDifficulty(self):
        return self.__difficulty
    def getNameProfessor(self):
        return self.__nameProfessor
    def getNameSubject(self):
        return self.__nameSubjectCourse
    def getEnabled(self):
        if self.__enabled:
            return "yes" 
        else:
            return "No"
    def getcountLessons(self):
        return self.__numberOfLessons
    def getcountExercises(self):
        return self.__numberOfExercises
    def getnumberOfEnrollees(self):
        return self.__numberOfEnrollees
    def MAPgetStudentsInscription(self):
        return self.__MAPenrollment
    def getLessons(self):
        return self.__lessons
