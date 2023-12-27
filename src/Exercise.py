class Exercise:
    def __init__(self, identificacion, Description): 
       self.__Id = identificacion
       self.__Description = Description
       self.__MAPStudentsAprobaron = dict()

    def getId(self):
        return self.__Id
    def getDescription(self):
        return self.__Description
    def esAprovado(self, nicknaMonthtudent):
        if nicknaMonthtudent in self.__MAPStudentsAprobaron:
            return True
        else: 
            return False
    def addStudentAprobado(self,nicknaMonthtudent, Registration):
        self.__MAPStudentsAprobaron[nicknaMonthtudent] = Registration
    def eliminarStudentsApproved(self):
        self.__MAPStudentsAprobaron.clear()
        del self.__MAPStudentsAprobaron