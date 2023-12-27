from src.IUser import IUser  
from src.DTDate import DTDate
from src.DTCourse import DTCourse
from src.UserManager import UserManager
from src.Student import Student
from src.DTStudent import DTStudent
from src.Professor import Professor
from src.DTProfessor import DTProfessor
from src.SubjectManager import SubjectManager
from src.CourseManager import CourseManager
from src.DTRegistration import DTRegistration
from src.DTExercise import DTExercise
from src.CompleteWord import CompleteWord
from src.MultipleChoice import MultipleChoice
class CtrUser(IUser):
    __instancia = None
    __nickNameRec = None
    __NameCourseRec = None
    __CourseRecordado =  None
    __nuevoUserNicknameRec = None
    __nuevoUserContrasenia = None
    __nuevoUserDescription= None
    __nuevoUserNameRec= None
    __nuevoUserNameCountryRec= None
    __nuevoUserDateBirthRec= None
    __nuevoUserInstituteRec= None
    __SETnuevoUserSpecialization = None 
    __SETSubjectRecordados = set()
    __UserRecordado = None
    __ExerciseRecordado = None
    __ExerciseMultipleChoice= None
    __ExerciseDeCompleteWord = None
    __LessonRecordada = None
    __StudentRemember = None

    
    
    def __new__(cls):
        if CtrUser.__instancia is None:
           CtrUser.__instancia = object.__new__(cls)
        return CtrUser.__instancia
    
    
    
    
    #public
    #Register User
    def EnterDatasUser(self, nickname, Password, Description, Name): 
        self.__nuevoUserNicknameRec = nickname
        self.__nuevoUserContrasenia = Password
        self.__nuevoUserDescription = Description
        self.__nuevoUserNameRec = Name
    
    def  EnterDataStudent(self, NameCountry,DateBirth):
        self.__nuevoUserNameCountryRec = NameCountry
        self.__nuevoUserDateBirthRec = DateBirth

    #Devuelve true si el nickname ya esta
    def  NicknameAvailable(self, nickname):
        mu = UserManager()
        if mu.ExistsUser(nickname):
           return True
        else:
            return False

    def  RegisterStudent(self):
        mu = UserManager()
        nuevoStudent = Student(self.__nuevoUserNicknameRec, self.__nuevoUserContrasenia,
                                     self.__nuevoUserNameRec, self.__nuevoUserDescription,
                                     self.__nuevoUserNameCountryRec, self.__nuevoUserDateBirthRec)
        mu.AddUser(nuevoStudent)
    
    def  ConfirmRegisterStudent(self):
        if not self.NicknameAvailable(self.__nuevoUserNicknameRec):
            self.RegisterStudent()

    
    def  EnterInstitute(self, NameInstitute):
        self.__nuevoUserInstituteRec= NameInstitute
    
    def GetSubjectsAvailables(self):
        mi = SubjectManager()
        Subjects = mi.SETSubjectsAvailables()
        return Subjects
    
    def  AddSpecialization(self, NaMonthubject):
        self.__SETSubjectRecordados.add(NaMonthubject)
    
    def  ConfirmRegisterProfessor(self):
        mu = UserManager()
        prof = Professor(self.__nuevoUserNicknameRec, self.__nuevoUserContrasenia, self.__nuevoUserNameRec,
                        self.__nuevoUserDescription, self.__nuevoUserInstituteRec)
        for i in self.__SETSubjectRecordados:
           prof.AddSpecialization(i)
        mu.AddUser(prof)
    
    def  RegisterProfessor():
        pass
    
     #Consutl User
    
    def GetNicknameUsers(self):
        mu = UserManager()
        SETnicknameUsers = mu.GetNickname()
        return SETnicknameUsers
    
    def  SelectUser(self, nickname):
        mu = UserManager()
        User = mu.GetUser(nickname)
        if type(User)== Professor :
            prof = self.SelectProfessor(nickname)
            print(f"Name: {prof.getName()}")
            print(f"Descripción: {prof.getDescription()}")
            print(f"Institute: {prof.getInstitute()}")
            Subject = User.SETGetSpecializationes()
            for i in Subject:
                print(f"Subject: {i}")
        elif type(User)== Student: 
            es = self.SelectStudent(nickname)
            print(f"Name: {es.getName()}")
            print(f"Descripción: {es.getDescription()}")
            print(f"Country: {es.getCountry()}")
            print(f"Date de Birth: {es.getDate().getDay()} /{es.getDate().getMonth()}/{es.getDate().getYear()} ")



    
    def  SelectStudent(self, nickname):
        mu = UserManager()
        Student = mu.GetUser(nickname)
        es = DTStudent(Student.getNickname(), Student.getPassword(),
                          Student.getName(), Student.getDescription(), 
                          Student.getCountry(), Student.getDateNac())
        return es

    
    def SelectProfessor(self, nickname):
        mu = UserManager()
        Professor = mu.GetUser(nickname)
        prof = DTProfessor(Professor.getNickname(), Professor.getPassword(),
                          Professor.getName(), Professor.getDescription(), 
                          Professor.getInstitute())
        return prof
     #Consutl Notifications
    
    def  EnterNickname(self, nickname):
        self.__nickNameRec = nickname
    
    def  GetNotifications(self, nickname):
        mu = UserManager()
        ususario = mu.GetUser(nickname=nickname)
        Notifications =  ususario.SETDevolverNotifications()
        return Notifications
    
    def  DeleteNotifiaciones(self, nickname):
        mu = UserManager()
        User = mu.GetUser(nickname=nickname)
        User.elimiarNotifications()
     #SUSCRIBIRSE A NOTIFIACIONES
    
    def GetSubjectUnsubscribed (self, nickname):
        mu = UserManager()
        ma = SubjectManager()
        User = mu.GetUser(nickname=nickname)
        Subjectuscrito = User.SETGetNomSubjectuscrito()
        SubjectDiponible = ma.SETSubjectsAvailables()
        SubjectSubscriptions = set()
        for a in SubjectDiponible:
            if not a in Subjectuscrito:
                SubjectSubscriptions.add(a)
        return SubjectSubscriptions



    
    def  AgreagarSuscripcion(self, nickname, nomSubject):
        mu = UserManager()
        ma = SubjectManager()
        User = mu.GetUser(nickname=nickname)
        Subject = ma.GetSubject(NaMonthubject=nomSubject)
        User.agreagarSuscripcion(Subject)
        Subject.AddSuscriptor(User)
    
    def  ExistsSubject(self, asign):
        mi = SubjectManager()
        return mi.ExistsSubject(asign)
    
     #ElIMIAR SUSCRIPCIÓN
    
    def GetSubscriptions(self, nickname):
        mu = UserManager()
        User = mu.GetUser(nickname=nickname)
        Subscriptions = User.SETGetNomSubjectuscrito()
        return Subscriptions
    
    def  DeleteSubscriptions(self, nickname, eleccionSubject):
        ma = SubjectManager()
        mu = UserManager()
        Subject = ma.GetSubject(eleccionSubject)
        User = mu.GetUser(nickname = nickname)
        User.eliminarSuscripcion(eleccionSubject)
        Subject.eliminar(nickname)
    

        
     #INSCRIBIRSE A Course
    
    def  GetCoursesAvailableforRegistration(self, nickname):
        mc = CourseManager()
        mu = UserManager()
        Student = mu.GetUser(nickname)
        CoursesInscriptos = Student.MAPGetCoursesInscriptos()
        NameCourses = mc.GetCoursesAvailables()
        listNameCourses = []
        for curDis in NameCourses:
            listNameCourses.append(curDis)
        Courses = mc.SETGetCourses(listNameCourses)
        CoursesAvailable = set()
        CoursesAvailables = set()
        for c in Courses:
            if c.getHabilitado():
                CoursesAvailable.add(c)
        #//Si no Exists Courses Habilitado con el null indicamos que no Exists Courses para inscribirse.
        if len(CoursesAvailable)==0:
            return CoursesAvailable
        
        #itero en todos los Courses Available
        for c in CoursesAvailable:
            #si tengo Courses inscriptos
            if len(CoursesInscriptos) != 0 and not (c.getName() in CoursesInscriptos):
                MAPPrerequisites = c.getPrerequisites()
                tieneLasPrerequisites = True
                if len(MAPPrerequisites) != 0:
                    for p in MAPPrerequisites:
                        if not p in CoursesInscriptos:
                            tieneLasPrerequisites = False
                        else:
                            if not Student.getRegistration(p).getAprobada():
                                tieneLasPrerequisites = False
                if tieneLasPrerequisites:
                    CourseAvailable = DTCourse(Course=c)
                    CoursesAvailables.add(CourseAvailable)
            else:
                if len(CoursesInscriptos)==0: 
                    Prerequisites = c.getPrerequisites()
                    if len(Prerequisites) == 0:
                        CourseAvailable = DTCourse(course=c)
                        CoursesAvailables.add(CourseAvailable)
     
        return CoursesAvailables
    
    def  EnterCourseSeleccionado(self, NameCourse):
        self.__NameCourseRec = NameCourse
    
    def  FinalizarRegistrationACourse(self, nickname, Date = None, aprobado = False):
        mu = UserManager()
        mc = CourseManager()
        try:
           Student = mu.GetUser(nickname)
           Course = mc.GetCourse(self.__NameCourseRec);
           Student.inscribirseCourse(Course.getName(),Course, aprobado, Date)
           return True
        except:
           return False


    #Execute Exercise
    
    def  ExistsUser(nickname):
        pass
    
    def  RememberUser(nickname):
        pass
    def  GetCoursesInscriptoNoAprobado(self, nickname):
        mu = UserManager()
        Student = mu.GetUser(nickname)
        self.__StudentRemember = Student
        CoursesInscriptos= Student.MAPgetRegistrations()
        CoursesInscriptosNoApproved = set()
        for i in CoursesInscriptos.values():
            if i.getAprobada() == False :
                CoursesInscriptosNoApproved.add(DTRegistration(Registration=i))
        return CoursesInscriptosNoApproved


    
    def  GetExercisesNoApproved(self):
        mc = CourseManager()
        mu = UserManager()
        est = mu.GetUser(self.__nickNameRec)
        Registration = est.getRegistration(self.__NameCourseRec)
        ultimaLessonAprobada = Registration.getUltimaLessonAprobada()
        cur = mc.GetCourse(self.__NameCourseRec)
        self.__CourseRecordado = cur
        ExercisesNoApproved = set()
        if ultimaLessonAprobada is not None:
            Order = ultimaLessonAprobada.getOrder()
            nextLesson = cur.GetLesson(Order + 1)
            self.__LessonRecordada = nextLesson
            Exercises = nextLesson.MAPgetColExercises()
            for e in Exercises.values():
                if not e.esAprovado(self.__nickNameRec):
                    ExercisesNoApproved.add(DTExercise(Exercise=e))
            return ExercisesNoApproved
        else:
            nextLesson = cur.GetLesson(1)
            self.__LessonRecordada = nextLesson
            Exercises = nextLesson.MAPgetColExercises()
            for e in Exercises.values():
                if not e.esAprovado(self.__nickNameRec):
                    ExercisesNoApproved.add(DTExercise(Exercise=e))
            return ExercisesNoApproved
                


        
    
    def  RememberExercise(self, Id):
        self.__ExerciseRecordado = Id
    
    def  mostrarExercise(self):
        ej = self.__LessonRecordada.GetExercise(self.__ExerciseRecordado)
        if type(ej)== CompleteWord:
            self.__ExerciseDeCompleteWord=ej
            print("Complete: ")
            print(f"Sentence: {ej.getSentence()}")
            return True
        else:
            self.__ExerciseMultipleChoice = ej
            print("Elije la opción correcta: ")
            Options = ej.getOptions()
            print (f"Problema o Exercise:\n {ej.getOracion()}")
            for ok, ov in Options.items():
                print(f"Opción {ok}: {ov}")
            return False
        
         

    
    def  mostrarExerciseaux():
        pass
    
    def  ResolveCompleteWord(self, conjunto_Solution):
        if self.__ExerciseDeCompleteWord.EnterSolution(conjunto_Solution):
            Registration = self.__StudentRemember.getRegistration(self.__NameCourseRec)
            self.__ExerciseDeCompleteWord.addStudentAprobado(self.__nickNameRec, Registration)
            Exercises = self.__LessonRecordada.MAPgetColExercises()
            cantEjer = self.__LessonRecordada.getcountExercises()
            Order = self.__LessonRecordada.getOrder()
            cantApproved = 0
            for e in Exercises.values():
                if e.esAprovado(self.__nickNameRec):
                    cantApproved +=1
            if cantApproved == cantEjer:
                Registration.setNuevaLessonAprobada(self.__LessonRecordada)
            if self.__CourseRecordado.getcountLessons() == Order:
                Registration.setAprobada(True)
            return True
        else:
            return False


    def  ResolveMultipleChoice(self, Solution):
        if self.__ExerciseMultipleChoice.getCorrectOption() == Solution:
            Registration = self.__StudentRemember.getRegistration(self.__NameCourseRec)
            self.__ExerciseMultipleChoice.addStudentAprobado(self.__nickNameRec, Registration)
            Exercises = self.__LessonRecordada.MAPgetColExercises()
            cantEjer = self.__LessonRecordada.getcountExercises()
            Order = self.__LessonRecordada.getOrder()
            cantApproved = 0
            for e in Exercises.values():
                if e.esAprovado(self.__nickNameRec):
                    cantApproved +=1
            if cantApproved == cantEjer:
                Registration.setNuevaLessonAprobada(self.__LessonRecordada)
            if self.__CourseRecordado.getcountLessons() == Order:
                Registration.setAprobada(True)
            return True
        else: return False
        
    
    def cantidadWordsACompletar(self):
        return self.__ExerciseDeCompleteWord.getCantidadWords()

    #def __del__(): pass