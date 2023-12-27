from src.Subject import Subject
class SubjectManager(object):
    __instancia = None
    __MAPSubjects = None
    
    def __new__(cls):
        if SubjectManager.__instancia is None:
            SubjectManager.__instancia = object.__new__(cls)
            SubjectManager.__MAPSubjects = dict()
        return SubjectManager.__instancia
    


    def getInstancia(): pass
    def AddSubject(self, subject):
        self.__MAPSubjects[subject.getName()] = subject

    def SETSubjectsAvailables(self):
        SETSubjects  = set()
        for i in self.__MAPSubjects.values():
            nomIdioma = i.getName()#.strip().lower()
            SETSubjects.add(nomIdioma)
        return SETSubjects

        
    def GetSubject(self, NaMonthubject):
        return self.__MAPSubjects[NaMonthubject]
        

    def ExistsSubject(self, NaMonthubject):
        Name_minuscula = NaMonthubject#.lower().strip()
        setSubject = self.SETSubjectsAvailables()
        return Name_minuscula in setSubject
            
    #def __del__(): pass

