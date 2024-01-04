from src.Professor import Professor
from src.Student import Student
class UserManager(object):
    __instance = None
    __MAPUsers = dict()
    
    def __new__(cls):
        if UserManager.__instance is None:
            UserManager.__instance = object.__new__(cls)
        return UserManager.__instance

    def existsUser(self, nickname):
        if nickname in self.__MAPUsers:
            return True
        else:
            return False
        
    def addUser(self, nuevoUser):
        self.__MAPUsers[nuevoUser.getNickname()] = nuevoUser


    def getUser(self, nickname):
        return self.__MAPUsers[nickname]
    
    def SETGetStudents(self):
        nickNameStudents = set()
        for e in self.__MAPUsers.values():
            if type(e) == Student:
                nickNameStudents.add(e.getNickname())
        return nickNameStudents


    #Retorna nicknaMonth de los Professors
    def getProfessors(self):
        nicknameProfessors = set()
        for p in self.__MAPUsers.values():
            if type(p) == Professor:
                nicknameProfessors.add(p.getNickname())
        return nicknameProfessors
    
  

    #Get todos los nickname
    def getNickname(self):
        SETnickname = set()
        if self.__MAPUsers != None:
            for u in self.__MAPUsers:
               SETnickname.add(u)
        return SETnickname


    def addCourseCol(Course):pass
    def approveExercise(Exercise, nickname, nameCourse):pass
    
