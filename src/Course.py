from src.CourseManager import CourseManager
from src.Lesson import Lesson
from src.Student import Student
class Course:
    def __init__(self, Name, Description, Level, Professor=None, subject = None):
       self.__Name = Name
       self.__Description=Description
       self.__Dificultad=Level
       self.__ProfessorCourse = Professor
       self.__subjectCourse = subject
       self.__Prerequisites= dict()
       self.__Habilitado = False
       self.__MAPalumnosInscriptos=dict()
       self.__MAPLessons= dict()

    def getName(self):
        return self.__Name
    def getPrerequisites(self):
        return self.__Prerequisites
    def getDescription(self):
        return self.__Description
    def getDificultad(self):
        return self.__Dificultad
    def getSubject(self):
        return self.__subjectCourse
    def getNaMonthubject(self):
        return self.__subjectCourse.getName()
    def getHabilitado(self):
        return self.__Habilitado
    def esPrerequisite(self, NameCourse):
        if NameCourse in self.__Prerequisites:
            return True
        else: 
            return False
    def setHabilitar(self):
        if self.__Habilitado == False:
            self.__Habilitado = True

    def inscribirStudent(self, Student):
        self.__MAPalumnosInscriptos[Student.getNickname()]=Student
    def getcountLessons(self):
        return len(self.__MAPLessons)
    def setProfessor(self, Professor):
        self.__ProfessorCourse = Professor
    def setHabilitado(habilitado):pass
    def removerPrerequisite(self, NameCourse):
        if NameCourse in self.__Prerequisites:
            del self.__Prerequisites[NameCourse]

    def getDataCourse():pass
    def añadirLesson(self, lec):
        self.__MAPLessons[lec.getOrder()] =lec
    def añadirPrerequisite(self, Prerequisite):
        self.__Prerequisites[Prerequisite.getName()]=Prerequisite

    def GetAvanceCourse(self, nickStudent):
        cantidadExercisesApproved = 0
        for l in self.__MAPLessons.values():
            Exercises = l.MAPgetColExercises()
            for e in Exercises.values():
                if e.esAprovado(nickStudent):
                    cantidadExercisesApproved += 1
        return (cantidadExercisesApproved/self.getcountExercises())*100

    def GetPromedioCourse(self): 
        cantAlumnosInscriptos = len(self.__MAPalumnosInscriptos)
        sumaAvanceAlumno = 0
        for a in self.__MAPalumnosInscriptos.values():
            avanceAlumno = self.GetAvanceCourse(a.getNickname())
            sumaAvanceAlumno += avanceAlumno
        if cantAlumnosInscriptos == 0:
            return 0
        else:
            return sumaAvanceAlumno/cantAlumnosInscriptos
            
    def GetSiguienteLesson(Order):pass
    def GetLesson(self, Order):
        return self.__MAPLessons[Order]
    
    
    def MAPgetLessons(self): 
        Lessons = dict()
        for lk, lv in self.__MAPLessons.items():
            Lessons[lk] = lv.getTopic()
        return Lessons
    def nuevoExercise(les, Description, Sentence, MAPSolution):pass
    def nuevoExercise(les, Description, Sentence, Solution):pass
    def MakeCourseAvailable(): pass
    def getcountExercises(self): 
        cant = 0
        for l in self.__MAPLessons.values():
            cant += l.getcountExercises()
        return cant
    def MAPgetColLessons(self):
        return self.__MAPLessons
    def eliminarLessons(self):
        for l in self.__MAPLessons.values():
            l.eliminarExercises()
        self.__MAPLessons.clear()
    def eliminarPrerequisites(nomCourse): pass
    def getProfessor(self):
        return self.__ProfessorCourse
    def getNameProfessor(self):
        return self.__ProfessorCourse.getName()
    def MAPgetStudents(self):
        return self.__MAPalumnosInscriptos
    def getNicknameProfessor(): pass
    def getCantInscriptos(self):
        return len(self.__MAPalumnosInscriptos)
    def eliminarRegistrations(self):
        pass
    def borrarPrerequisites(): pass