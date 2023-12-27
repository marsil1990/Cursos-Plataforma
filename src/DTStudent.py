from src.DTUser import DTUser
from src.Student import Student
from src.DTRegistration import DTRegistration
from src.DTDate import DTDate
class DTStudent(DTUser):
    def __init__(self, Nickname=None, Password=None, Name=None, Description=None, Country=None, Date=None, Student = None):
        if Student is None:
            super().__init__(Nickname, Password, Name, Description)
            self.__Country = Country
            self.__Date = Date
        else:
            super().__init__(Student.getNickname(), Student.getPassword(), Student.getName(), Student.getDescription())
            self.__Country = Student.getCountry()
            self.__Date = Student.getDateNac()
            self.__Registrations = dict()
            ins = Student.MAPgetRegistrations()
            for ik, iv in ins.items():
                self.__Registrations[ik] = DTRegistration(Registration=iv)


    def getCountry(self):
        return self.__Country

    def getDate(self):
        return self.__Date
    
    def getRegistration(self, NameCourse):
        return self.__Registrations[NameCourse]
   
    