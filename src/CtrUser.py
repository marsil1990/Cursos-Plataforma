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
    __instance = None
    __nickNameRec = None
    __nameCourseRec = None
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
        if CtrUser.__instance is None:
           CtrUser.__instance = object.__new__(cls)
        return CtrUser.__instance
    
    
    
    
    #public
    #Register User
    def enterDatasUser(self, nickname, password, description, Name): 
        self.__nuevoUserNicknameRec = nickname
        self.__nuevoUserContrasenia = password
        self.__nuevoUserDescription = description
        self.__nuevoUserNameRec = Name
    
    def  enterDataStudent(self, nameCountry,dateBirth):
        self.__nuevoUserNameCountryRec = nameCountry
        self.__nuevoUserDateBirthRec = dateBirth

    #Devuelve true si el nickname ya esta
    def  nicknameAvailable(self, nickname):
        mu = UserManager()
        if mu.existsUser(nickname):
           return True
        else:
            return False

    def  registerStudent(self):
        mu = UserManager()
        nuevoStudent = Student(self.__nuevoUserNicknameRec, self.__nuevoUserContrasenia,
                                     self.__nuevoUserNameRec, self.__nuevoUserDescription,
                                     self.__nuevoUserNameCountryRec, self.__nuevoUserDateBirthRec)
        mu.AddUser(nuevoStudent)
    
    def  confirmRegisterStudent(self):
        if not self.nicknameAvailable(self.__nuevoUserNicknameRec):
            self.registerStudent()

    
    def  enterInstitute(self, nameInstitute):
        self.__nuevoUserInstituteRec= nameInstitute
    
    def GetSubjectsAvailables(self):
        mi = SubjectManager()
        Subjects = mi.SETSubjectsAvailables()
        return Subjects
    
    def  addSpecialization(self, nameSubject):
        self.__SETSubjectRecordados.add(nameSubject)
    
    def  confirmregisterProfessor(self):
        mu = UserManager()
        prof = Professor(self.__nuevoUserNicknameRec, self.__nuevoUserContrasenia, self.__nuevoUserNameRec,
                        self.__nuevoUserDescription, self.__nuevoUserInstituteRec)
        for i in self.__SETSubjectRecordados:
           prof.AddSpecialization(i)
        mu.AddUser(prof)
    
    def  registerProfessor():
        pass
    
     #Consutl User
    
    def GetNicknameUsers(self):
        mu = UserManager()
        SETnicknameUsers = mu.GetNickname()
        return SETnicknameUsers
    
    def  selectUser(self, nickname):
        mu = UserManager()
        user = mu.GetUser(nickname)
        if type(user)== Professor :
            prof = self.selectProfessor(nickname)
            print(f"Name: {prof.getName()}")
            print(f"Descripción: {prof.getDescription()}")
            print(f"Institute: {prof.getInstitute()}")
            Subject = user.SETGetSpecializationes()
            for i in Subject:
                print(f"Subject: {i}")
        elif type(user)== Student: 
            es = self.selectStudent(nickname)
            print(f"Name: {es.getName()}")
            print(f"Descripción: {es.getDescription()}")
            print(f"Country: {es.getCountry()}")
            print(f"Date de Birth: {es.getDate().getDay()} /{es.getDate().getMonth()}/{es.getDate().getYear()} ")



    
    def  selectStudent(self, nickname):
        mu = UserManager()
        Student = mu.GetUser(nickname)
        es = DTStudent(Student.getNickname(), Student.getPassword(),
                          Student.getName(), Student.getDescription(), 
                          Student.getCountry(), Student.getDateNac())
        return es

    
    def selectProfessor(self, nickname):
        mu = UserManager()
        professor = mu.GetUser(nickname)
        prof = DTProfessor(professor.getNickname(), professor.getPassword(),
                          professor.getName(), professor.getDescription(), 
                          professor.getInstitute())
        return prof
     #Consutl Notifications
    
    def  enterNickname(self, nickname):
        self.__nickNameRec = nickname
    
    def  GetNotifications(self, nickname):
        mu = UserManager()
        ususario = mu.GetUser(nickname=nickname)
        notifications =  ususario.getNotifications()
        return notifications
    
    def  deleteNotifiaciones(self, nickname):
        mu = UserManager()
        user = mu.GetUser(nickname=nickname)
        user.removeNotifications()
     #SUSCRIBIRSE A NOTIFIACIONES
    
    def GetSubjectUnsubscribed (self, nickname):
        mu = UserManager()
        ma = SubjectManager()
        User = mu.GetUser(nickname=nickname)
        subjectuscrito = User.SETGetNomSubjectuscrito()
        subjectDiponible = ma.SETSubjectsAvailables()
        subjectSubscriptions = set()
        for a in subjectDiponible:
            if not a in subjectuscrito:
                subjectSubscriptions.add(a)
        return subjectSubscriptions



    
    def  addSuscription(self, nickname, nomSubject):
        mu = UserManager()
        ma = SubjectManager()
        user = mu.GetUser(nickname=nickname)
        subject = ma.GetSubject(NameSubject=nomSubject)
        user.addSuscription(subject)
        subject.AddSuscriptor(user)
    
    def existsSubject(self, subject):
        mi = SubjectManager()
        return mi.ExistsSubject(subject)
    
     #ElIMIAR SUSCRIPCIÓN
    
    def GetSubscriptions(self, nickname):
        mu = UserManager()
        user = mu.GetUser(nickname=nickname)
        subscriptions = user.SETGetNomSubjectuscrito()
        return subscriptions
    
    def  deleteSubscriptions(self, nickname, choiceSubject):
        ma = SubjectManager()
        mu = UserManager()
        subject = ma.GetSubject(choiceSubject)
        user = mu.GetUser(nickname = nickname)
        user.removeSubscription(choiceSubject)
        subject.eliminar(nickname)
    

        
     #INSCRIBIRSE A Course
    
    def  getCoursesAvailableforRegistration(self, nickname):
        mc = CourseManager()
        mu = UserManager()
        student = mu.GetUser(nickname)
        coursesInscriptos = Student.MAPgetCoursesInscriptos()
        nameCourses = mc.getCoursesAvailables()
        listnameCourses = []
        for curDis in nameCourses:
            listnameCourses.append(curDis)
        courses = mc.SETgetCourses(listnameCourses)
        coursesAvailable = set()
        coursesAvailables = set()
        for c in courses:
            if c.getEnabled():
                coursesAvailable.add(c)
        #//Si no Exists Courses Habilitado con el null indicamos que no Exists Courses para inscribirse.
        if len(coursesAvailable)==0:
            return coursesAvailable
        
        #itero en todos los Courses Available
        for c in coursesAvailable:
            #si tengo Courses inscriptos
            if len(coursesInscriptos) != 0 and not (c.getName() in coursesInscriptos):
                MAPPrerequisites = c.getPrerequisites()
                tieneLasPrerequisites = True
                if len(MAPPrerequisites) != 0:
                    for p in MAPPrerequisites:
                        if not p in coursesInscriptos:
                            tieneLasPrerequisites = False
                        else:
                            if not student.getRegistration(p).getAprobada():
                                tieneLasPrerequisites = False
                if tieneLasPrerequisites:
                    courseAvailable = DTCourse(Course=c)
                    coursesAvailables.add(courseAvailable)
            else:
                if len(coursesInscriptos)==0: 
                    prerequisites = c.getPrerequisites()
                    if len(prerequisites) == 0:
                        courseAvailable = DTCourse(course=c)
                        coursesAvailables.add(courseAvailable)
     
        return coursesAvailables
    
    def  enterCourseSeleccionado(self, nameCourse):
        self.__nameCourseRec = nameCourse
    
    def  finalizarRegistrationACourse(self, nickname, Date = None, aprobado = False):
        mu = UserManager()
        mc = CourseManager()
        try:
           student = mu.GetUser(nickname)
           course = mc.getCourse(self.__nameCourseRec);
           student.inscribirseCourse(course.getName(),course, aprobado, Date)
           return True
        except:
           return False


    #Execute Exercise
    
    def  existsUser(nickname):
        pass
    
    def  rememberUser(nickname):
        pass
    def  getCoursesInscriptoNoAprobado(self, nickname):
        mu = UserManager()
        student = mu.GetUser(nickname)
        self.__StudentRemember = Student
        coursesInscriptos= Student.MAPgetRegistrations()
        coursesInscriptosNoApproved = set()
        for i in coursesInscriptos.values():
            if i.getAprobada() == False :
                coursesInscriptosNoApproved.add(DTRegistration(Registration=i))
        return coursesInscriptosNoApproved


    
    def  getExercisesNoApproved(self):
        mc = CourseManager()
        mu = UserManager()
        est = mu.GetUser(self.__nickNameRec)
        registration = est.getRegistration(self.__nameCourseRec)
        ultimaLessonAprobada = registration.getUltimaLessonAprobada()
        cur = mc.getCourse(self.__nameCourseRec)
        self.__CourseRecordado = cur
        exercisesNoApproved = set()
        if ultimaLessonAprobada is not None:
            Order = ultimaLessonAprobada.getOrder()
            nextLesson = cur.getLesson(Order + 1)
            self.__LessonRecordada = nextLesson
            exercises = nextLesson.MAPgetColExercises()
            for e in exercises.values():
                if not e.esAprovado(self.__nickNameRec):
                    exercisesNoApproved.add(DTExercise(Exercise=e))
            return exercisesNoApproved
        else:
            nextLesson = cur.getLesson(1)
            self.__LessonRecordada = nextLesson
            exercises = nextLesson.MAPgetColExercises()
            for e in exercises.values():
                if not e.esAprovado(self.__nickNameRec):
                    exercisesNoApproved.add(DTExercise(Exercise=e))
            return exercisesNoApproved
                


        
    
    def  rememberExercise(self, Id):
        self.__ExerciseRecordado = Id
    
    def  mostrarExercise(self):
        ej = self.__LessonRecordada.getExercise(self.__ExerciseRecordado)
        if type(ej)== CompleteWord:
            self.__ExerciseDeCompleteWord=ej
            print("Complete: ")
            print(f"Sentence: {ej.getSentence()}")
            return True
        else:
            self.__ExerciseMultipleChoice = ej
            print("Elije la opción correcta: ")
            options = ej.getOptions()
            print (f"Problema o Exercise:\n {ej.getOracion()}")
            for ok, ov in options.items():
                print(f"Opción {ok}: {ov}")
            return False
        
         

    
    def  mostrarExerciseaux():
        pass
    
    def  resolveCompleteWord(self, conjunto_Solution):
        if self.__ExerciseDeCompleteWord.EnterSolution(conjunto_Solution):
            registration = self.__StudentRemember.getRegistration(self.__nameCourseRec)
            self.__ExerciseDeCompleteWord.addApprovedStudent(self.__nickNameRec, registration)
            exercises = self.__LessonRecordada.MAPgetColExercises()
            cantEjer = self.__LessonRecordada.getcountExercises()
            order = self.__LessonRecordada.getOrder()
            cantApproved = 0
            for e in exercises.values():
                if e.esAprovado(self.__nickNameRec):
                    cantApproved +=1
            if cantApproved == cantEjer:
                registration.setNuevaLessonAprobada(self.__LessonRecordada)
            if self.__CourseRecordado.getcountLessons() == order:
                registration.setAprobada(True)
            return True
        else:
            return False


    def  resolveMultipleChoice(self, solution):
        if self.__ExerciseMultipleChoice.getCorrectOption() == solution:
            registration = self.__StudentRemember.getRegistration(self.__nameCourseRec)
            self.__ExerciseMultipleChoice.addApprovedStudent(self.__nickNameRec, registration)
            exercises = self.__LessonRecordada.MAPgetColExercises()
            cantEjer = self.__LessonRecordada.getcountExercises()
            order = self.__LessonRecordada.getOrder()
            cantApproved = 0
            for e in exercises.values():
                if e.esAprovado(self.__nickNameRec):
                    cantApproved +=1
            if cantApproved == cantEjer:
                registration.setNuevaLessonAprobada(self.__LessonRecordada)
            if self.__CourseRecordado.getcountLessons() == order:
                registration.setAprobada(True)
            return True
        else: return False
        
    
    def cantidadWordsACompletar(self):
        return self.__ExerciseDeCompleteWord.getWordCount()

    #def __del__(): pass