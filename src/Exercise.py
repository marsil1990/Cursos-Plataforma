class Exercise:
    def __init__(self, identificacion, Description): 
       self.__Id = identificacion
       self.__description = Description
       self.__MAPapprovedStudents = dict()

    def getId(self):
        return self.__Id
    def getDescription(self):
        return self.__description
    def esAprovado(self, nickName):
        if nickName in self.__MAPapprovedStudents:
            return True
        else: 
            return False
    def addApprovedStudent(self,nickName, Registration):
        self.__MAPapprovedStudents[nickName] = Registration
    def removeStudentsApproved(self):
        self.__MAPapprovedStudents.clear()
        del self.__MAPapprovedStudents