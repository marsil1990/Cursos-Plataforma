from abc import ABC, abstractmethod
class ICourse(ABC):
    #Register Course
    @abstractmethod
    def GetNickname(): pass
    @abstractmethod
    def ExistsCourse(NameCourse): pass
    @abstractmethod
    def SelectProfessor(nickname): pass
    @abstractmethod
    def EnterDatasCourse (Name, Description, dificultad): pass
    @abstractmethod
    def GetSubjectsSpecialization(): pass
    @abstractmethod
    def SelectSubject(NaMonthubject): pass
    @abstractmethod
    def RequiresPrerequisite(confirmacion): pass
    @abstractmethod
    def SETGetCoursesAvailable(): pass
    @abstractmethod
    def SelectPrerequisites(SET): pass
    @abstractmethod
    def CreateLesson(Topic, Goal): pass
    @abstractmethod
    def CreateExerciseCompleteWord(Description,Sentence, MAPrespuesta): pass
    @abstractmethod
    def CreateExerciseMultipleChoice(self, Description,Question, Options, CorrectOption): pass
    @abstractmethod
    def ConfirmRegisterCourse(): pass

    #Add Lesson
    @abstractmethod
    def SETGetCoursesNoAvailable(): pass
    @abstractmethod
    def SelectCourse(NameCourse): pass
    @abstractmethod
    def CreateDatasLesson(Topic, Goal): pass
    @abstractmethod
    def EnterSentenceCompletar(Sentence, MAPSolution): pass
    @abstractmethod
    def DarDeRegisterExercise(): pass
    @abstractmethod
    def DarDeRegisterLesson(): pass

    #Add Exercise
    @abstractmethod
    def MAPGetLessons(): pass
    @abstractmethod
    def AddExercise(les, Description ,Sentence, MAPSolution): pass
    @abstractmethod
    def AddExercise(les, Description, Sentence, Solution): pass
    @abstractmethod
    def SelectLesson(self, Order):pass

    #Register Subject
    @abstractmethod
    def EnterSubject(NaMonthubject): pass
    @abstractmethod
    def ConfirmSubject(): pass
    @abstractmethod
    def ConsultSubject(): pass
    #Consult Statistics
    @abstractmethod
    def GetStudents(): pass
    @abstractmethod
    def MAPGetCoursesInscripto(nickname): pass
    @abstractmethod
    def MAPGetAdvancedCourses(): pass
    @abstractmethod
    def GetProfessors(): pass 
    @abstractmethod
    def MAPGetPromedioCourses(): pass
    @abstractmethod
    def SETGetCourses(): pass
    @abstractmethod
    def GetPromedio(): pass
    @abstractmethod
    def MakeCourseAvailable(): pass
    #Consult Course
    @abstractmethod
    def GetCourse(NameCourse): pass
    @abstractmethod
    def  MAPGetLessonsDeCourse(): pass
    @abstractmethod
    def  MAPGetExercises(Lesson): pass
    #Eliminar Course
    @abstractmethod
    def deleteCourse(): pass