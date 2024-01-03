from src.DTCourse import DTCourse
class CourseManager(object):
    __instance = None
    __MAPCourses = None
    def __new__(cls):
        if CourseManager.__instance is None:
            CourseManager.__instance = object.__new__(cls)
            CourseManager.__MAPCourses = dict()
        return CourseManager.__instance
    
    
    def getCourse(self, nameCourse):
        return self.__MAPCourses[nameCourse]
    def  getCoursesAvailables(self):
        CoursesAvailables = set()
        for c in self.__MAPCourses.values():
            CoursesAvailables.add(c.getName())
        return CoursesAvailables

    def existsCourse(self, nameCourse):
        return nameCourse in self.__MAPCourses
    
    def getLesson(self, nameCourse, Order):
        return self.__MAPCourses[nameCourse].getLesson(Order)

    def getDisabledCourses(): pass
    def setEnrolledUnapprovedCourses(): pass
    def SETExercisesNoApproved(): pass

    #Devuelve los Courses que se encuentran en la lista de string "nameCourses"
    def SETgetCourses(self, nameCourses):
        coursesPrevios = set()
        for prev in nameCourses:
            coursesPrevios.add(self.__MAPCourses[prev])
        return coursesPrevios
            

    def removePrerequisite(NomCourses): pass

        
    def addCourse(self, Course):
        self.__MAPCourses[Course.getName()] = Course
        
        
    def getAllCourses(self):
        courses = set()
        for c in self.__MAPCourses.values():
            courses.add(DTCourse(course=c))
        return courses
    def getCourses(self):
        return self.__MAPCourses

    def deleteCourse(self,nameCourse):
        self.__MAPCourses[nameCourse].removeLessons()
        self.__MAPCourses[nameCourse].eliminarRegistrations()
        for c in self.__MAPCourses.values():
            if c.isPrerequisite(nameCourse):
                c.removerPrerequisite(nameCourse)
        del self.__MAPCourses[nameCourse]