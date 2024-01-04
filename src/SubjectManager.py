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
    def addSubject(self, subject):
        self.__MAPSubjects[subject.getName()] = subject

    def SETSubjectsAvailables(self):
        subjects  = set()
        for i in self.__MAPSubjects.values():
            nameSubject = i.getName()#.strip().lower()
            subjects.add(nameSubject)
        return subjects

        
    def getSubject(self, NameSubject):
        return self.__MAPSubjects[NameSubject]
        

    def existsSubject(self, nameSubject):
        name = nameSubject#.lower().strip()
        setSubject = self.SETSubjectsAvailables()
        return name in setSubject
            
    #def __del__(): pass

