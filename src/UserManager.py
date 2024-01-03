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
        
    def AddUser(self, nuevoUser):
        self.__MAPUsers[nuevoUser.getNickname()] = nuevoUser


    def GetUser(self, nickname):
        return self.__MAPUsers[nickname]
    
    def SETGetStudents(self):
        nickNaMonthtudents = set()
        for e in self.__MAPUsers.values():
            if type(e) == Student:
                nickNaMonthtudents.add(e.getNickname())
        return nickNaMonthtudents


    #Retorna nicknaMonth de los Professors
    def GetProfessors(self):
        nicknameProfessors = set()
        for p in self.__MAPUsers.values():
            if type(p) == Professor:
                nicknameProfessors.add(p.getNickname())
        return nicknameProfessors
    
    def GetNaMonth():pass

    #Get todos los nickname
    def GetNickname(self):
        SETnickname = set()
        if self.__MAPUsers != None:
            for u in self.__MAPUsers:
               SETnickname.add(u)
        return SETnickname

    def GetNaMonthProfessor():pass
    def addCourseColeccion(Course):pass
    def aprobarExercise(Exercise, nickname, nameCourse):pass
    
