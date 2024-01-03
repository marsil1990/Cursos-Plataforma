from src.DTUser import DTUser
class DTProfessor(DTUser):
    def __init__ (self, nickname, contraseña, name, description, institute):
        super().__init__(nickname, contraseña, name, description)
        self.__institute = institute

    def getInstitute(self):
        return self.__institute
    
