from abc import ABC, abstractmethod
class ICourse(ABC):
    #Register Course
    @abstractmethod
    def getNickname(): pass
    @abstractmethod
    def existsCourse(nameCourse): pass
    @abstractmethod
    def selectProfessor(nickname): pass
    @abstractmethod
    def enterDatasCourse (name, description, dificultad): pass
    @abstractmethod
    def getSubjectsSpecialization(): pass
    @abstractmethod
    def selectSubject(nameSubject): pass
    @abstractmethod
    def requirisPrerequisite(confirmacion): pass
    @abstractmethod
    def SETgetCoursesAvailable(): pass
    @abstractmethod
    def selectPrerequisites(setP): pass
    @abstractmethod
    def createLesson(topic, goal): pass
    @abstractmethod
    def createExerciseCompleteWord(description,sentence, MAPrespuesta): pass
    @abstractmethod
    def createExerciseMultipleChoice(self, description,question, options, correctOption): pass
    @abstractmethod
    def confirmRegisterCourse(): pass

    #Add Lesson
    @abstractmethod
    def getCoursesNoAvailable(): pass
    @abstractmethod
    def selectCourse(nameCourse): pass
    @abstractmethod
    def createDatasLesson(topic, goal): pass
    @abstractmethod
    def enterSentenceCompletar(sentence, MAPSolution): pass
    
    @abstractmethod
    def confirmLesson(): pass

    #Add Exercise
    @abstractmethod
    def MAPgetLessons(): pass
    @abstractmethod
    def addExercise(les, description ,sentence, MAPSolution): pass
    @abstractmethod
    def addExercise(les, description, sentence, solution): pass
    @abstractmethod
    def SelectLesson(self, order):pass

    #Register Subject
    @abstractmethod
    def enterSubject(nameSubject): pass
    @abstractmethod
    def confirmSubject(): pass
    @abstractmethod
    def consultSubject(): pass
    #Consult Statistics
    @abstractmethod
    def GetStudents(): pass
    @abstractmethod
    def MAPgetCoursesInscripto(nickname): pass
    @abstractmethod
    def MAPGetAdvancedCourses(): pass
    @abstractmethod
    def getProfessors(): pass 
    @abstractmethod
    def MAPgetCourseAverages(): pass
    @abstractmethod
    def SETgetCourses(): pass
    @abstractmethod
    def GetPromedio(): pass
    @abstractmethod
    def makeCourseAvailable(): pass
    #Consult Course
    @abstractmethod
    def getCourse(nameCourse): pass
    @abstractmethod
    def  MAPgetLessonsDeCourse(): pass
    @abstractmethod
    def  MAPgetExercises(lesson): pass
    #Delete Course
    @abstractmethod
    def deleteCourse(): pass

    @abstractmethod
    def deleteCourse(self, courseName):pass

    @abstractmethod
    def notify(self, course):pass