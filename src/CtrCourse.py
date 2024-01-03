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
       self.__nameCourseRec = None
       self.__descriptionRec = None
       self.__difficultyRec= None
       self.__subjectRec= None
       self.__requirisPrerequisiteRec= False
       self.__SETPrerequisitesRec= None
       self.__MAPLessonsRec= dict()
       self.__canLessons = None
       self.__ultimaLesson= None
       self.__CourseRecAdd = None
       self.__topicRec= None
       self.__goalRec= None
       self.__TypeExerciseRec= None
       self.__descriptionEjRec= None
       self.__SentenceEjRec= None
       self.__MAPSolutionFCRec= None
       self.__SolutionTRec= None
       self.__MAPExercisesNuevos= None
       self.__LessonSeLessonada= None
       self.__nameRecordado= None
       self.__MAPCoursesRecordados= None
     
    #Register Course
    def GetNickname(self):
        mu = UserManager()
        nickNaMonthProfessors = mu.GetProfessors()
        return nickNaMonthProfessors

    
    def existsCourse(self, nameCourse):
        mc = CourseManager()
        return mc.existsCourse(nameCourse)
    def selectProfessor(self, nickname): 
        mu = UserManager()
        self.__profRec  = mu.GetUser(nickname)
        
    
    def enterDatasCourse (self, name, description, dificultad):
        self.__nameCourseRec = name
        self.__descriptionRec = description
        self.__difficultyRec = dificultad
    
    def getSubjectsSpecialization(self):
        subjectsEspecializado = self.__profRec.SETGetSpecializationes()
        return subjectsEspecializado
        

    
    def selectSubject(self, NameSubject):
        mi = SubjectManager()
        self.__subjectRec = mi.GetSubject(NameSubject)
    
    def SelectLesson(self, order, nameCourse):
        mc = CourseManager()
        self.__ultimaLesson = mc.getLesson(nameCourse, order)

    def requirisPrerequisite(self, confirmacion):
        self.__requirisPrerequisiteRec = confirmacion
    
    def SETgetCoursesAvailable(self):
        return self.__profRec.getDataEnabledCourses(self.__subjectRec.getName())
    
    def selectPrerequisites(self, cadena):
        c = cadena.replace(" ","")
        Prerequisites = c.split(',')
        mc = CourseManager()
        CoursesPrevios = mc.SETgetCourses(Prerequisites)
        self.__SETPrerequisitesRec = CoursesPrevios
        



    
    def createLesson(self, topic, goal, courseName):
        mc = CourseManager()
        Course = mc.getCourse(courseName)
        n = Course.getcountLessons() + 1
        self.__ultimaLesson =  Lesson(n, topic, goal)
        self.__MAPLessonsRec[n]= Lesson(n, topic, goal)

    def createExerciseCompleteWord(self, description,sentence, MAPrespuesta):
        self.__ultimaLesson.addCompletionExercise(description, sentence, MAPrespuesta)

    def createExerciseMultipleChoice(self, description,question, options, correctOption):
        self.__ultimaLesson.addExerciseMultiple(description,question, options, correctOption)

    def confirmRegisterCourse(self):
        nuevoCourse = Course(self.__nameCourseRec, self.__descriptionRec, self.__difficultyRec,
                           self.__profRec, self.__subjectRec)
        self.__profRec.associateCourseProfessor(nuevoCourse)
        if self.__requirisPrerequisiteRec:
            for p in self.__SETPrerequisitesRec:
                nuevoCourse.añadirPrerequisite(p)
        self.__subjectRec.asociarCourseSubject(nuevoCourse)
        mc = CourseManager()
        mc.addCourse(nuevoCourse)
        nuevoCourse.setProfessor(self.__profRec)

    #Add Lesson
    #Course no Available de un Professor de nickname "nickname"
    def getCoursesNoAvailable(self, nickname):
        mu = UserManager()
        prof = mu.GetUser(nickname)
        return prof.getCoursesNoAvailable()
    
    def selectCourse(self, nameCourse):
        mc = CourseManager()
        self.__CourseRecAdd = mc.getCourse(nameCourse)
        
    
    def createDatasLesson(self, topic, goal):
        self.__topicRec = topic
        self.__goalRec = goal
    
    def enterSentenceCompletar(sentence, MAPSolution): pass
    
  
    
    def confirmLesson(self):
        self.__CourseRecAdd.addLesson(self.__ultimaLesson)
        self.__MAPLessonsRec.clear()
        self.__ultimaLesson = None

    #Add Exercise
    
    def MAPgetLessons(self):
        Lessons = self.__CourseRecAdd.MAPgetLessons()
        return Lessons
    
    def addExercise(lec, Description ,Sentence, MAPSolution): pass
    
    def addExercise(lec, Description, Sentence, Solution): pass

    #Register subject
    
    def enterSubject(self,nameSubject):
        self.__subjectRec = nameSubject
    
    def confirmSubject(self):
        mi = SubjectManager()
        if mi.existsSubject(self.__subjectRec):
            return False
        else:
            i = Subject(self.__subjectRec)
            mi.AddSubject(i)
            return True
    
    def consultSubject(self):
        mi = SubjectManager()
        return mi.SETSubjectsAvailables()
    #Consult Statistics
    
    def GetStudents(self):
        mu = UserManager()
        Students = mu.SETGetStudents()
        return Students
    
    def MAPgetCoursesInscripto(nickname): pass
    
    def MAPGetAdvancedCourses(self, nicknaMonthtudent= None, nicknameProfessor = None, Course = None):
        if nicknaMonthtudent!= None:
            mu = UserManager()
            user = mu.GetUser(nickname=nicknaMonthtudent)
            coursesInscriptos = user.MAPgetCoursesInscriptos()
            for c in coursesInscriptos.values():
                avanceCourse = c.getCourseProgress(nicknaMonthtudent)
                print(f"Course: {c.getName()}, Avance: {avanceCourse}%")
        elif nicknameProfessor != None:
            mu = UserManager()
            user = mu.GetUser(nickname=nicknameProfessor)
            coursesProfessor = user.MAPCourses()
            for c in coursesProfessor.values():
                print(f"Name del Course: {c.getName()}, Promedio: {c.getCourseAverage()}")
        else:
            mc = CourseManager()
            c = mc.getCourse(Course)
            print(f"Name del Course: {c.getName()}, Promedio: {c.getCourseAverage()}")




    def GetProfessors(): pass 
    
    def MAPgetCourseAverages(): pass
    
    def SETgetCourses(self):
        mc = CourseManager()
        Courses =  mc.getAllCourses()
        return Courses
    
    def GetPromedio(): pass
    
    def makeCourseAvailable(self):
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
                self.__CourseRecAdd.setEnabled()
                
        return correcto


                


    #Consult Course
    
    def getCourse(self,nameCourse):
        mc = CourseManager()
        c = mc.getCourse(nameCourse)
        CourseDt = DTCourse(Course=c)
        return CourseDt

    
    def  MAPgetLessonsDeCourse(): pass
    
    def  MAPgetExercises(lesson): pass
    #Eliminar Course
    
    def deleteCourse(self, courseName):
        mc = CourseManager()
        mc.deleteCourse(courseName)

    def notify(self, course):
        mc = CourseManager()
        c = mc.getCourse(course)
        subjectCourse = c.getSubject()
        subjectCourse.EnviarNotificacion(c.getName())