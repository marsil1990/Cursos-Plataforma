from copy import copy
from src.ICourse import ICourse
from src.SubjectManager import SubjectManager
from src.UserManager import UserManager
from src.Subject import Subject
from src.CourseManager import CourseManager
from src.Course import Course
from src.Lesson import Lesson
from src.DTCourse import DTCourse
class CtrCourse(ICourse) :
    def __init__(self):
       self.__profRec = None
       self.__NameCourseRec = None
       self.__DescriptionRec = None
       self.__dificultadRec= None
       self.__subjectRec= None
       self.__RequiresPrerequisiteRec= False
       self.__SETPrerequisitesRec= None
       self.__MAPLessonsRec= dict()
       self.__canLessons = None
       self.__ultimaLesson= None
       self.__CourseRecAdd = None
       self.__TopicRec= None
       self.__GoalRec= None
       self.__TypeExerciseRec= None
       self.__DescriptionEjRec= None
       self.__SentenceEjRec= None
       self.__MAPSolutionFCRec= None
       self.__SolutionTRec= None
       self.__MAPExercisesNuevos= None
       self.__LessonSeLessonada= None
       self.__NameRecordado= None
       self.__MAPCoursesRecordados= None
     
    #Register Course
    def GetNickname(self):
        mu = UserManager()
        nickNaMonthProfessors = mu.GetProfessors()
        return nickNaMonthProfessors

    
    def ExistsCourse(self, NameCourse):
        mc = CourseManager()
        return mc.ExistsCourse(NameCourse)
    def SelectProfessor(self, nickname): 
        mu = UserManager()
        self.__profRec  = mu.GetUser(nickname)
        
    
    def EnterDatasCourse (self, Name, Description, dificultad):
        self.__NameCourseRec = Name
        self.__DescriptionRec = Description
        self.__dificultadRec = dificultad
    
    def GetSubjectsSpecialization(self):
        subjectsEspecializado = self.__profRec.SETGetSpecializationes()
        return subjectsEspecializado
        

    
    def SelectSubject(self, NaMonthubject):
        mi = SubjectManager()
        self.__subjectRec = mi.GetSubject(NaMonthubject)
    
    def SelectLesson(self, Order, NameCourse):
        mc = CourseManager()
        self.__ultimaLesson = mc.GetLesson(NameCourse, Order)

    def RequiresPrerequisite(self, confirmacion):
        self.__RequiresPrerequisiteRec = confirmacion
    
    def SETGetCoursesAvailable(self):
        return self.__profRec.SETgetDataCoursesHab(self.__subjectRec.getName())
    
    def SelectPrerequisites(self, cadena):
        c = cadena.replace(" ","")
        Prerequisites = c.split(',')
        mc = CourseManager()
        CoursesPrevios = mc.SETGetCourses(Prerequisites)
        self.__SETPrerequisitesRec = CoursesPrevios
        



    
    def CreateLesson(self, Topic, Goal, CourseName):
        mc = CourseManager()
        Course = mc.GetCourse(CourseName)
        n = Course.getcountLessons() + 1
        self.__ultimaLesson =  Lesson(n, Topic, Goal)
        self.__MAPLessonsRec[n]= Lesson(n, Topic, Goal)

    def CreateExerciseCompleteWord(self, Description,Sentence, MAPrespuesta):
        self.__ultimaLesson.añadirExerciseCompletar(Description, Sentence, MAPrespuesta)

    def CreateExerciseMultipleChoice(self, Description,Question, Options, CorrectOption):
        self.__ultimaLesson.añadirExerciseMultiple(Description,Question, Options, CorrectOption)

    def ConfirmRegisterCourse(self):
        nuevoCourse = Course(self.__NameCourseRec, self.__DescriptionRec, self.__dificultadRec,
                           self.__profRec, self.__subjectRec)
        self.__profRec.asociarCourseProfessor(nuevoCourse)
        if self.__RequiresPrerequisiteRec:
            for p in self.__SETPrerequisitesRec:
                nuevoCourse.añadirPrerequisite(p)
        self.__subjectRec.asociarCourseSubject(nuevoCourse)
        mc = CourseManager()
        mc.AddCourse(nuevoCourse)
        nuevoCourse.setProfessor(self.__profRec)

    #Add Lesson
    #Course no Available de un Professor de nickname "nickname"
    def SETGetCoursesNoAvailable(self, nickname):
        mu = UserManager()
        prof = mu.GetUser(nickname)
        return prof.SETGetCoursesNoAvailable()
    
    def SelectCourse(self, NameCourse):
        mc = CourseManager()
        self.__CourseRecAdd = mc.GetCourse(NameCourse)
        
    
    def CreateDatasLesson(self, Topic, Goal):
        self.__TopicRec = Topic
        self.__GoalRec = Goal
    
    def EnterSentenceCompletar(Sentence, MAPSolution): pass
    
    def DarDeRegisterExercise():
        pass
    
    def DarDeRegisterLesson(self):
        self.__CourseRecAdd.añadirLesson(self.__ultimaLesson)
        self.__MAPLessonsRec.clear()
        self.__ultimaLesson = None

    #Add Exercise
    
    def MAPGetLessons(self):
        Lessons = self.__CourseRecAdd.MAPgetLessons()
        return Lessons
    
    def AddExercise(lec, Description ,Sentence, MAPSolution): pass
    
    def AddExercise(lec, Description, Sentence, Solution): pass

    #Register subject
    
    def EnterSubject(self,NaMonthubject):
        self.__subjectRec = NaMonthubject
    
    def ConfirmSubject(self):
        mi = SubjectManager()
        if mi.ExistsSubject(self.__subjectRec):
            return False
        else:
            i = Subject(self.__subjectRec)
            mi.AddSubject(i)
            return True
    
    def ConsultSubject(self):
        mi = SubjectManager()
        return mi.SETSubjectsAvailables()
    #Consult Statistics
    
    def GetStudents(self):
        mu = UserManager()
        Students = mu.SETGetStudents()
        return Students
    
    def MAPGetCoursesInscripto(nickname): pass
    
    def MAPGetAdvancedCourses(self, nicknaMonthtudent= None, nicknameProfessor = None, Course = None):
        if nicknaMonthtudent!= None:
            mu = UserManager()
            User = mu.GetUser(nickname=nicknaMonthtudent)
            CoursesInscriptos = User.MAPGetCoursesInscriptos()
            for c in CoursesInscriptos.values():
                avanceCourse = c.GetAvanceCourse(nicknaMonthtudent)
                print(f"Course: {c.getName()}, Avance: {avanceCourse}%")
        elif nicknameProfessor != None:
            mu = UserManager()
            User = mu.GetUser(nickname=nicknameProfessor)
            CoursesProfessor = User.MAPCourses()
            for c in CoursesProfessor.values():
                print(f"Name del Course: {c.getName()}, Promedio: {c.GetPromedioCourse()}")
        else:
            mc = CourseManager()
            c = mc.GetCourse(Course)
            print(f"Name del Course: {c.getName()}, Promedio: {c.GetPromedioCourse()}")




    def GetProfessors(): pass 
    
    def MAPGetPromedioCourses(): pass
    
    def SETGetCourses(self):
        mc = CourseManager()
        Courses =  mc.GetAllCourses()
        return Courses
    
    def GetPromedio(): pass
    
    def MakeCourseAvailable(self):
        correcto = False
        if self.__CourseRecAdd.getcountLessons()!= 0:
            Lessons = self.__CourseRecAdd.MAPgetColLessons()
            cantidadLessons = 0
            for l in Lessons.values():
                if l.getcountExercises()==0:
                    break
                else:
                    cantidadLessons +=1
            if cantidadLessons == self.__CourseRecAdd.getcountLessons():
                correcto = True
                self.__CourseRecAdd.setHabilitar()
                
        return correcto


                


    #Consult Course
    
    def GetCourse(self,NameCourse):
        mc = CourseManager()
        c = mc.GetCourse(NameCourse)
        CourseDt = DTCourse(Course=c)
        return CourseDt

    
    def  MAPGetLessonsDeCourse(): pass
    
    def  MAPGetExercises(Lesson): pass
    #Eliminar Course
    
    def deleteCourse(self, CourseName):
        mc = CourseManager()
        mc.deleteCourse(CourseName)

    def Notify(self, Course):
        mc = CourseManager()
        c = mc.GetCourse(Course)
        subjectCourse = c.getSubject()
        subjectCourse.EnviarNotificacion(c.getName())