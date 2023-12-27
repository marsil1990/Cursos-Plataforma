from abc import ABC, abstractmethod
class IUser(ABC):
    @abstractmethod
    def EnterDatasUser(nickname, Password, Description, Name): 
        pass
    @abstractmethod
    def  EnterDataStudent(NameCountry,DateBirth):
        pass
    @abstractmethod
    def  NicknameAvailable(nickname):
        pass
    @abstractmethod
    def  RegisterStudent():
        pass
    @abstractmethod
    def  ConfirmRegisterStudent():
        pass
    @abstractmethod
    def  EnterInstitute(NameCountry):
        pass
    @abstractmethod
    def  GetSubjectsAvailables():
        pass
    @abstractmethod
    def  AddSpecialization(NaMonthubject):
        pass
    @abstractmethod
    def  ConfirmRegisterProfessor():
        pass
    @abstractmethod
    def  RegisterProfessor():
        pass
    @abstractmethod
     #Consult User
    @abstractmethod
    def GetNicknameUsers():
        pass
    @abstractmethod
    def  SelectUser(nickname):
        pass
    @abstractmethod
    def  SelectStudent(nickname):
        pass
    @abstractmethod
    def SelectProfessor(nickname):
        pass
     #Consult Notifications
    @abstractmethod
    def  EnterNickname(nickname):
        pass
    @abstractmethod
    def  GetNotifications():
        pass
    @abstractmethod
    def  DeleteNotifiaciones():
        pass
     #SUSCRIBIRSE A NOTIFIACIONES
    @abstractmethod
    def GetSubjectUnsubscribed (nickname):
        pass
    @abstractmethod
    def  AgreagarSuscripcion(nomSubject):
        pass
    @abstractmethod
    def  ExistsSubject(subject):
        pass
     #ElIMIAR SUSCRIPCIÓN
    @abstractmethod
    def GetSubscriptions(nickname):
        pass
    @abstractmethod
    def  DeleteSubscriptions():
        pass
     #INSCRIBIRSE A Course
    @abstractmethod
    def  GetCoursesAvailableforRegistration(nickName):
        pass
    @abstractmethod
    def  EnterCourseSeleccionado(NameCourse):
        pass
    @abstractmethod
    def  FinalizarRegistrationACourse(nickname, Date = None, aprobado = False):
        pass
    #Execute Exercise
    @abstractmethod
    def  ExistsUser(nickname):
        pass
    @abstractmethod
    def  RememberUser(nickname):
        pass
    def  GetCoursesInscriptoNoAprobado():
        pass
    @abstractmethod
    def  GetExercisesNoApproved():
        pass
    @abstractmethod
    def  RememberExercise(numero, Exercise):
        pass
    @abstractmethod
    def  mostrarExercise():
        pass
    @abstractmethod
    def  mostrarExerciseaux():
        pass
    @abstractmethod
    def  ResolveCompleteWord(map, Conjunto_Solution, imprimir=False):
        pass
    @abstractmethod
    def  ResolveMultipleChoice(Solution, imprimir=False):
        pass
    @abstractmethod
    def cantidadWordsACompletar():
        pass
    
