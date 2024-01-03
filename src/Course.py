from src.CourseManager import CourseManager
from src.Lesson import Lesson
from src.Student import Student
class Course:
    def __init__(self, name, description, level, professor=None, subject = None):
       self.__name = name
       self.__description=description
       self.__difficulty=level
       self.__professorCourse = professor
       self.__subjectCourse = subject
       self.__prerequisites= dict()
       self.__enabled = False
       self.__MAPenrolledStudents=dict()
       self.__MAPLessons= dict()

    def getName(self):
        return self.__name
    def getPrerequisites(self):
        return self.__prerequisites
    def getDescription(self):
        return self.__description
    def getDifficulty(self):
        return self.__difficulty
    def getSubject(self):
        return self.__subjectCourse
    def getNameSubject(self):
        return self.__subjectCourse.getName()
    def getEnabled(self):
        return self.__enabled
    def isPrerequisite(self, nameCourse):
        if nameCourse in self.__prerequisites:
            return True
        else: 
            return False
    def setEnabled(self):
        if self.__enabled == False:
            self.__enabled = True

    def enrollStudent(self, student):
        self.__MAPenrolledStudents[student.getNickname()]=student
    def getcountLessons(self):
        return len(self.__MAPLessons)
    def setProfessor(self, Professor):
        self.__professorCourse = Professor
    def setEnabled(habilitado):pass
    def removerPrerequisite(self, nameCourse):
        if nameCourse in self.__prerequisites:
            del self.__prerequisites[nameCourse]

    def getDataCourse():pass
    def addLesson(self, lec):
        self.__MAPLessons[lec.getOrder()] =lec
    def añadirPrerequisite(self, Prerequisite):
        self.__prerequisites[Prerequisite.getName()]=Prerequisite

    def getCourseProgress(self, nickStudent):
        getApprovedExercisesCount = 0
        for l in self.__MAPLessons.values():
            Exercises = l.MAPgetColExercises()
            for e in Exercises.values():
                if e.esAprovado(nickStudent):
                    getApprovedExercisesCount += 1
        return (getApprovedExercisesCount/self.getcountExercises())*100

    def getCourseAverage(self): 
        getEnrolledStudentsCount = len(self.__MAPenrolledStudents)
        sumStudentProgress = 0
        for a in self.__MAPenrolledStudents.values():
            studentProgress = self.getCourseProgress(a.getNickname())
            sumStudentProgress += studentProgress
        if getEnrolledStudentsCount == 0:
            return 0
        else:
            return sumStudentProgress/getEnrolledStudentsCount
            
    def GetSiguienteLesson(Order):pass
    def getLesson(self, Order):
        return self.__MAPLessons[Order]
    
    
    def MAPgetLessons(self): 
        lessons = dict()
        for lk, lv in self.__MAPLessons.items():
            lessons[lk] = lv.getTopic()
        return lessons
    def nuevoExercise(les, Description, Sentence, MAPSolution):pass
    def nuevoExercise(les, Description, Sentence, Solution):pass
    def makeCourseAvailable(): pass
    def getcountExercises(self): 
        cant = 0
        for l in self.__MAPLessons.values():
            cant += l.getcountExercises()
        return cant
    def MAPgetColLessons(self):
        return self.__MAPLessons
    def removeLessons(self):
        for l in self.__MAPLessons.values():
            l.removeExercises()
        self.__MAPLessons.clear()
    def removePrerequisites(nomCourse): pass
    def getProfessor(self):
        return self.__professorCourse
    def getNameProfessor(self):
        return self.__professorCourse.getName()
    def MAPgetStudents(self):
        return self.__MAPenrolledStudents
    def getNicknameProfessor(): pass
    def getnumberOfEnrollees(self):
        return len(self.__MAPenrolledStudents)
    def eliminarRegistrations(self):
        pass
    def borrarPrerequisites(): pass