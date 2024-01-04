from abc import ABC, abstractmethod
class IUser(ABC):
    @abstractmethod
    def enterDatasUser(nickname, password, description, name): 
        pass
    @abstractmethod
    def  enterDataStudent(nameCountry,dateBirth):
        pass
    @abstractmethod
    def  nicknameAvailable(nickname):
        pass
    @abstractmethod
    def  registerStudent():
        pass
    @abstractmethod
    def  confirmRegisterStudent():
        pass
    @abstractmethod
    def  enterInstitute(nameCountry):
        pass
    @abstractmethod
    def  getSubjectsAvailables():
        pass
    @abstractmethod
    def  addSpecialization(nameSubject):
        pass
    @abstractmethod
    def  confirmregisterProfessor():
        pass
    @abstractmethod
    def  registerProfessor():
        pass
    @abstractmethod
     #Consult User
    @abstractmethod
    def getNicknameUsers():
        pass
    @abstractmethod
    def  selectUser(nickname):
        pass
    @abstractmethod
    def  selectStudent(nickname):
        pass
    @abstractmethod
    def selectProfessor(nickname):
        pass
     #Consult Notifications
    @abstractmethod
    def  enterNickname(nickname):
        pass
    @abstractmethod
    def  GetNotifications():
        pass
    @abstractmethod
    def  deleteNotifiaciones():
        pass
     #SUSCRIBIRSE A NOTIFIACIONES
    @abstractmethod
    def getSubjectUnsubscribed (nickname):
        pass
    @abstractmethod
    def  addSuscription(nomSubject):
        pass
    @abstractmethod
    def  existsSubject(subject):
        pass
     #ElIMIAR SUSCRIPCIÓN
    @abstractmethod
    def GetSubscriptions(nickname):
        pass
    @abstractmethod
    def  deleteSubscriptions(nickname, choiceSubject):
        pass
     #INSCRIBIRSE A Course
    @abstractmethod
    def  getCoursesAvailableforRegistration(nickName):
        pass
    @abstractmethod
    def  enterCourseSeleccionado(nameCourse):
        pass
    @abstractmethod
    def  finalizarRegistrationACourse(nickname, Date = None, aprobado = False):
        pass
    #Execute Exercise
    @abstractmethod
    def  existsUser(nickname):
        pass
    @abstractmethod
    def  rememberUser(nickname):
        pass
    def  getCoursesInscriptoNoAprobado():
        pass
    @abstractmethod
    def  getExercisesNoApproved():
        pass
    @abstractmethod
    def  rememberExercise(numero, Exercise):
        pass
    @abstractmethod
    def  mostrarExercise():
        pass
    @abstractmethod
    def  mostrarExerciseaux():
        pass
    @abstractmethod
    def  resolveCompleteWord(map, conjunto_Solution, imprimir=False):
        pass
    @abstractmethod
    def  resolveMultipleChoice(solution, imprimir=False):
        pass
    @abstractmethod
    def cantidadWordsACompletar():
        pass
    
