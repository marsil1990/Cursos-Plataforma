from src.DTUser import DTUser
from src.Student import Student
from src.DTRegistration import DTRegistration
from src.DTDate import DTDate
class DTStudent(DTUser):
    def __init__(self, nickname=None, password=None, name=None, description=None, country=None, date=None, student = None):
        if Student is None:
            super().__init__(nickname, password, name, description)
            self.__country = country
            self.__date = date
        else:
            super().__init__(student.getNickname(), student.getPassword(), student.getName(), student.getDescription())
            self.__country = student.getCountry()
            self.__date = student.getBirthDate()
            self.__registrations = dict()
            reg = student.MAPgetRegistrations()
            for ik, iv in reg.items():
                self.__registrations[ik] = DTRegistration(registration=iv)


    def getCountry(self):
        return self.__country

    def getDate(self):
        return self.__date
    
    def getRegistration(self, nameCourse):
        return self.__registrations[nameCourse]
   
    