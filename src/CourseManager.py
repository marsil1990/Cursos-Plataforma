from src.DTCourse import DTCourse
class CourseManager(object):
    __instancia = None
    __MAPCourses = None
    def __new__(cls):
        if CourseManager.__instancia is None:
            CourseManager.__instancia = object.__new__(cls)
            CourseManager.__MAPCourses = dict()
        return CourseManager.__instancia
    
    
    def GetCourse(self, NameCourse):
        return self.__MAPCourses[NameCourse]
    def  GetCoursesAvailables(self):
        CoursesAvailables = set()
        for c in self.__MAPCourses.values():
            CoursesAvailables.add(c.getName())
        return CoursesAvailables

    def ExistsCourse(self, NameCourse):
        return NameCourse in self.__MAPCourses
    
    def GetLesson(self, NameCourse, Order):
        return self.__MAPCourses[NameCourse].GetLesson(Order)

    def SETGetCoursesNoHab(): pass
    def SETCoursesInscriptoNoAprobado(): pass
    def SETExercisesNoApproved(): pass

    #Devuelve los Courses que se encuentran en la lista de string "NameCourses"
    def SETGetCourses(self, NameCourses):
        CoursesPrevios = set()
        for prev in NameCourses:
            CoursesPrevios.add(self.__MAPCourses[prev])
        return CoursesPrevios
            

    def eliminarPrerequisite(NomCourses): pass

        
    def AddCourse(self, Course):
        self.__MAPCourses[Course.getName()] = Course
        
        
    def GetAllCourses(self):
        Courses = set()
        for c in self.__MAPCourses.values():
            Courses.add(DTCourse(Course=c))
        return Courses
    def getCourses(self):
        return self.__MAPCourses

    def deleteCourse(self,NameCourse):
        self.__MAPCourses[NameCourse].eliminarLessons()
        self.__MAPCourses[NameCourse].eliminarRegistrations()
        for c in self.__MAPCourses.values():
            if c.esPrerequisite(NameCourse):
                c.removerPrerequisite(NameCourse)
        del self.__MAPCourses[NameCourse]