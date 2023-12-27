from src.DTStudent import DTStudent
from src.DTLesson import DTLesson

class DTCourse :
    def __init__(self, Name=None, Description=None, dificultad=None, NameProfessor=None, 
                 Subject=None, estado=None, cantLessons=None, cantExercises=None, cantInscriptos=None, course = None):
        if course is None:
            self.__Course = None
            self.__Name = Name
            self.__Description = Description
            self.__Dificultad = dificultad
            self.__NameProfessor = NameProfessor
            self.__NaMonthubjectCourse = Subject
            self.__Habilitado = estado
            self.__cantLessons = cantLessons
            self.__cantExercises = cantExercises
            self.__cantInscriptos = cantInscriptos
            self.__lessons = dict()
            self.__MAPinscriptos = dict()
        else:
            from src.Course import Course
            self.__Name = course.getName()
            self.__Description= course.getDescription()
            self.__Dificultad= course.getDificultad()
            self.__NameProfessor = course.getNameProfessor()
            self.__NaMonthubjectCourse = course.getSubject().getName()
            self.__Habilitado= course.getHabilitado()
            self.__cantLessons = course.getcountLessons()
            self.__cantExercises = course.getcountExercises()
            self.__cantInscriptos = course.getCantInscriptos()
            self.__MAPinscriptos = dict()
            self.__lessons = dict()
            Students = course.MAPgetStudents()
            for ek, ev in Students.items():
                self.__MAPinscriptos[ek] = DTStudent(Student=ev)
            lessons = course.MAPgetColLessons()
            for lk, lv in lessons.items():
                self.__lessons[lk] = DTLesson(lesson=lv)
                   
        
    def getName(self): 
        return self.__Name
    def getDesc(self):
        return self.__Description
    def getDificultad(self):
        return self.__Dificultad
    def getNameProfessor(self):
        return self.__NameProfessor
    def getNaMonthubject(self):
        return self.__NaMonthubjectCourse
    def getHabilitado(self):
        if self.__Habilitado:
            return "Si" 
        else:
            return "No"
    def getcountLessons(self):
        return self.__cantLessons
    def getcountExercises(self):
        return self.__cantExercises
    def getCantInscriptos(self):
        return self.__cantInscriptos
    def MAPgetStudentsInscription(self):
        return self.__MAPinscriptos
    def getLessons(self):
        return self.__lessons
