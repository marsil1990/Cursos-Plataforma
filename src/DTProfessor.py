from src.DTUser import DTUser
class DTProfessor(DTUser):
    def __init__ (self, Nickname, Contraseña, Name, Description, Institute):
        super().__init__(Nickname, Contraseña, Name, Description)
        self.__Institute = Institute

    def getInstitute(self):
        return self.__Institute
    
