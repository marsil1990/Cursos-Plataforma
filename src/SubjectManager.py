from src.Subject import Subject
class SubjectManager(object):
    __instance = None
    __MAPSubjects = None
    
    def __new__(cls):
        if SubjectManager.__instance is None:
            SubjectManager.__instance = object.__new__(cls)
            SubjectManager.__MAPSubjects = dict()
        return SubjectManager.__instance
    


    def getInstancia(): pass
    def AddSubject(self, subject):
        self.__MAPSubjects[subject.getName()] = subject

    def SETSubjectsAvailables(self):
        SETSubjects  = set()
        for i in self.__MAPSubjects.values():
            nomIdioma = i.getName()#.strip().lower()
            SETSubjects.add(nomIdioma)
        return SETSubjects

        
    def GetSubject(self, NameSubject):
        return self.__MAPSubjects[NameSubject]
        

    def existsSubject(self, NameSubject):
        Name_minuscula = NameSubject#.lower().strip()
        setSubject = self.SETSubjectsAvailables()
        return Name_minuscula in setSubject
            
    #def __del__(): pass

