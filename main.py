from src.Factory import Factory
from src.DTDate import DTDate
from datetime import datetime

def registerSubject():
    a = Factory()
    ctrCourse = a.getICourse()
    enter_subject = input("Enter Subject: ")
    while enter_subject.strip() == "":
        enter_subject = input("It cannot be empty. Enter Subject: ")
    ctrCourse.EnterSubject(enter_subject)
    conf = ctrCourse.ConfirmSubject()
    if conf:
        print("The subject was entered correctly")
    else: print("The subject already exists")

def ConsultSubject():
    a = Factory()
    ctrCourse = a.getICourse()
    setSubjects = ctrCourse.ConsultSubject()
    for i in setSubjects:
        print(i[0].upper()+i[1:])


def registerUser():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    while ctrUser.NicknameAvailable(nickname) and nickname!= "":
        nickname = input("The entered nickname is not available. Please enter Yearther one: ")
    Password = input("Enter password (minimum 6 characters): ")
    while len(Password) < 6 :
        Password = input("The password must be at least 6 characters long. Please try again: ")
    Name = input("Enter name: ")
    Description = input("Enter description: ")
    TypeUser = input("Are you a professor or a student?(p/s): ")
    ctrUser.EnterDatasUser(nickname,Password,Description, Name)
    if (TypeUser.lower().strip()== "s" ):
        NameCountry = input("Enter the country where you live: ")
        print("Enter date of birth: ")
        Day = int(input("Day: "))
        Month = int(input("Month: "))
        Year = int(input("Year: "))
        DateBirth = DTDate(Day, Month, Year)
        ctrUser.EnterDataStudent(NameCountry,DateBirth)
        ctrUser.ConfirmRegisterStudent()
    elif (TypeUser.lower().strip() == "p"):
        Institute = input("Enter the institute where you work: ")
        ctrUser.EnterInstitute(Institute)
        setSubjectsAvailables = ctrUser.GetSubjectsAvailables()
        #mostrar los Subjects
        for i in setSubjectsAvailables:
            print(i)
        Continue = True
        while Continue:
            Specialization = input("Choose an available subject: ")
            if ctrUser.ExistsSubject(Specialization):
                ctrUser.AddSpecialization(Specialization)
            else:
                print("The entered subject is not correct, please try again: ")
            cont = input("Do you want to add Yearther subject? Yes/No: ")
            if cont.strip().lower() ==  "no":
                Continue = False
                    
        ctrUser.ConfirmRegisterProfessor()
    else:
        print("The entered user type is not correct.")


def ConsultUser():
    a = Factory()
    ctrUser = a.getIUser()
    SETnicknameUsers = ctrUser.GetNicknameUsers()
    if len(SETnicknameUsers) != 0:
        for u in SETnicknameUsers:
            print(u)
        nickname_User = input("Enter the user's nickname: ")
        if(ctrUser.NicknameAvailable(nickname_User)):
            ctrUser.SelectUser(nickname_User)
        else: 
            print("The entered nickname is not correct")
    else: 
        print ("There are no registered users.")
    

def registerCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessors = ctrCourse.GetNickname()
    for p in nicknameProfessors:
        print(p)
    nickname = input("Enter the professor's nickname: ")
    while(not (nickname in nicknameProfessors)):
        nickname = input("Incorrect nickname, please enter the professor's nickname: ")
    ctrCourse.SelectProfessor(nickname)
    NameCourse = input("Name Course: ")
    while (ctrCourse.ExistsCourse(NameCourse)):
        NameCourse = input("The course name already exists. Please enter another one: ")
    DescriptionCourse = input("Course description: ")
    LevelCourse = input("Course level (Beginner (B)/Intermediate (I)/Advanced (A)): ")
    while (LevelCourse.strip().lower() != "b" and LevelCourse.strip().lower() != "i" and 
            LevelCourse.strip().lower() != "a"):
        LevelCourse = input("Enter only b, i o a: ")
    ctrCourse.EnterDatasCourse(NameCourse, DescriptionCourse, LevelCourse)
    setSubjects =  ctrCourse.GetSubjectsSpecialization()
    for i in setSubjects:
        print(i)
    Subject = input("Enter subject: ")
    while (not(Subject in setSubjects)):
        Subject = input("Incorrect, please enter the subject again: ")
    ctrCourse.SelectSubject(Subject)
    Prerequisite = input("Requires previous approved courses? Yes/No: ")
    conf = False
    if Prerequisite.strip().lower() == "yes":
        conf = True
        ctrCourse.RequiresPrerequisite(conf) 
        colCoursesAvailable = ctrCourse.SETGetCoursesAvailable()
        print("Courses created by the same professor.")
        if len(colCoursesAvailable) != 0:
            for c in colCoursesAvailable:
                 print(c)
            Prerequisites = input("Enter, separated by commas, the courses that will be prerequisites: ")
            ctrCourse.SelectPrerequisites(Prerequisites)
        else: print("There are no available courses")
    ctrCourse.ConfirmregisterCourse()
    AddLessons = input("Do you want to add lessons? Yes/No: ")
    while AddLessons.strip().lower() =="yes":
        ctrCourse.SelectCourse(NameCourse)
        Topic = input("Enter the topic of the lesson: ")
        Goal = input("Enter the goal of the lesson: ")
        #ctrCourse.CreateDatasLesson(Topic, Goal)
        ctrCourse.CreateLesson(Topic, Goal, NameCourse)
        AddExercises = input("Do you want to add exercises? Yes/No: ")
        while AddExercises.strip().lower() == "yes":
            TypeExercise = input("Enter the exercise type (only the number): 1 - Fill in the Blank, 2 - Multiple Choice: ")
            if TypeExercise.strip() == "1":
                Description = input("Add description: ")
                Sentence = input("Enter the sentence; in the places where the words would go, write ---: ")
                CharacterCount = Sentence.count("---")
                Solutions = dict()
                Place = CharacterCount
                while Place > 0:
                    Word = input(f"Enter the word for the placeholder number {Place}: ")
                    Solutions[Place] = Word
                    Place -= 1
                ctrCourse.CreateExerciseCompleteWord(Description, Sentence, Solutions)
            elif TypeExercise.strip() == "2":
                Description = input("Add description: ")
                Question = input("Enter the question or problem: ")
                CorrectOption = input("Enter the correct option (number of the answer): ")
                Options = dict()
                ContinueAdding = True
                op = 1
                while ContinueAdding:
                    opc = input("Enter an option: ")
                    Options[op] = opc
                    op +=1
                    Continue_Adding = input("Do you want to continue adding options? Yes/No: ")
                    if Continue_Adding.strip().lower() == "no":
                        ContinueAdding = False
                        op = 1
                ctrCourse.CreateExerciseMultipleChoice(Description, Question, Options, CorrectOption)
            else: print("Incorrect option entry")
            AddExercises = input("Do you want to add another exercise? Yes/No: ")
        ctrCourse.DarDeregisterLesson()
        AddLessons = input("Do you want to add another lesson? Yes/No: ")
        

def MakeCourseAvailable():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessors = ctrCourse.GetNickname()
    nicknameProfessor = input("Enter the professor's nickname: ")
    while(not (nicknameProfessor in nicknameProfessors)):
        nicknameProfessor = input("Incorrect nickname, Enter the professor's nickname: ")
    colCoursesNoAvailable =  ctrCourse.SETGetCoursesNoAvailable(nicknameProfessor)
    for c in colCoursesNoAvailable:
        print (c)
    Course = input("Enter Course: ")
    while (not ctrCourse.ExistsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    ctrCourse.SelectCourse(Course)
    correcto = ctrCourse.MakeCourseAvailable()
    if correcto:
        ctrCourse.Notify(Course)
        print("It was successfully enabled")
    else:
        print("It was not enabled")

def AddLesson():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessor = input("Enter the professor's nickname: ")
    nicknameProfessors = ctrCourse.GetNickname()
    while(not (nicknameProfessor in nicknameProfessors)):
        nicknameProfessor = input("Incorrect nickname, Enter the professor's nickname: ")
    colCoursesNoAvailable =  ctrCourse.SETGetCoursesNoAvailable(nicknameProfessor)
    for c in colCoursesNoAvailable:
        print (c)
    Course = input("Enter Course: ")
    while (not ctrCourse.ExistsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    ctrCourse.SelectCourse(Course)
    Topic = input("Enter the topic of the lesson: ")
    Goal = input("Enter Goal of the lesson: ")
    #ctrCourse.CreateDatasLesson(Topic, Goal)
    ctrCourse.CreateLesson(Topic, Goal, Course)
    AddExercises = input("Do you want to add exercises? Yes/No: ")
    while AddExercises.strip().lower() == "yes":
        TypeExercise = input("Enter the exercise type (only the number): 1 - Fill in the Blank, 2 - Multiple Choice: ")
        if TypeExercise.strip() == "1":
            Description = input("Add description: ")
            Sentence = input("Enter the sentence; in the places where the words would go, write ---: ")
            CharacterCount = Sentence.count("---")
            Solutions = dict()
            Place = CharacterCount
            while Place > 0:
                Word = input(f"Enter the word for placeholder number {Place}: ")
                Solutions[Place] = Word
                Place -= 1
            ctrCourse.CreateExerciseCompleteWord(Description, Sentence, Solutions)
        elif TypeExercise.strip() == "2":
            Description = input("Add description: ")
            Question = input("Enter the question or problem: ")
            CorrectOption = input("Enter the correct option (number of the answer): ")
            Options = dict()
            ContinueAdding = True
            op = 1
            while ContinueAdding:
                opc = input("Enter an option: ")
                Options[op] = opc
                op +=1
                Continue_Adding = input("Do you want to continue adding options? Yes/No: ")
                if Continue_Adding.strip().lower() == "no":
                    ContinueAdding = False
                    op = 1
            ctrCourse.CreateExerciseMultipleChoice(Description, Question, Options, CorrectOption)
        else: print("Incorrect option entry")
        AddExercises = input("Do you want to add another exercise? Yes/No: ")
    ctrCourse.DarDeregisterLesson()

def AddExercise():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessor = input("Enter the professor's nickname: ")
    nicknameProfessors = ctrCourse.GetNickname()
    while(not (nicknameProfessor in nicknameProfessors)):
        nicknameProfessor = input("Incorrect nickname, Enter the professor's nickname: ")
    colCoursesNoAvailable =  ctrCourse.SETGetCoursesNoAvailable(nicknameProfessor)
    for c in colCoursesNoAvailable:
        print (c)
    Course = input("Enter Course: ")
    while (not ctrCourse.ExistsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    ctrCourse.SelectCourse(Course)
    Lessons = ctrCourse.MAPGetLessons()
    for lk, lv in Lessons.items():
        print(f"{lk}:{lv}")
    Order = int(input("Enter lesson (number): "))
    while not Order in Lessons.keys():
        Order = int(input("Incorrect, enter lesson (number): "))
    ctrCourse.SelectLesson(Order, Course)
    TypeExercise = input("Enter the exercise type (only the number): 1 - Fill in the Blank, 2 - Multiple Choice: ")
    ContinueAdding = True
    while ContinueAdding == True:
        if TypeExercise.strip() == "1":
            Description = input("Add description: ")
            Sentence = input("Enter the sentence; in the places where the words would go, write ---: ")
            CharacterCount = Sentence.count("---")
            Solutions = dict()
            Place = CharacterCount
            while Place > 0:
                Word = input(f"Enter the word for placeholder number {Place}")
                Solutions[Place] = Word
                Place -= 1
            ctrCourse.CreateExerciseCompleteWord(Description, Sentence, Solutions)
        elif TypeExercise.strip() == "2":
            Description = input("Add description: ")
            Question = input("Enter the word for placeholder number: ")
            CorrectOption = input("Enter the correct option (number of the answer): ")
            Options = dict()
            ContinueAdding = True
            op = 1
            while ContinueAdding:
                opc = input("Enter an option: ")
                Options[op] = opc
                op +=1
                Continue_Adding = input("Do you want to continue adding options? Yes/No: ")
                if Continue_Adding.strip().lower() == "no":
                    ContinueAdding = False
                    op = 1
            ctrCourse.CreateExerciseMultipleChoice(Description, Question, Options, CorrectOption)
        else: 
            TypeExercise = input("Enter the exercise type (only the number): 1 - Fill in the Blank, 2 - Multiple Choice: ")
        s = input("Do you want to continue adding exercises? Yes/No: ")
        if s.strip().lower() == "no":
            ContinueAdding = False

def RegistrationCourse():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.NicknameAvailable(nickname):
        ctrUser.EnterNickname(nickname)
        CoursesAvailable = ctrUser.GetCoursesAvailableforRegistration(nickname)
        if not CoursesAvailable:
            print("The student does not have available courses.")
        else:
            i = 1
            print("---Courses Availables---")
            for c in CoursesAvailable:
                print(f"{1}) Course: {c.getName()}")
                print(f"- Description: {c.getDesc()}")
                print(f"- Number of lessons: {c.getcountLessons()}")
                print(f"- Number of Exercises: {c.getcountExercises()}")

            nameCourse = input("Write the name of the course: ")
            
            ctrUser.EnterCourseSeleccionado(nameCourse)
            Date_actual = datetime.now()
            f = DTDate(Date_actual.year, Date_actual.month, Date_actual.day)
            RegistrationCorrecta = ctrUser.FinalizarRegistrationACourse(nickname, f)
            if RegistrationCorrecta:
                print( "The registration was completed successfully.")
            
            else:
               print("There was an issue during the registration. Please try again.")
            
    else: print("No user exists with that nickname.")

def ConsultCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    Courses = ctrCourse.SETGetCourses()
    for c in Courses:
        print(c.getName())
    Course  =  input("Write the name of the course: ")
    while (not ctrCourse.ExistsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    CourseDt = ctrCourse.GetCourse(Course)
    print(f"Name of the Course: {CourseDt.getName()}")
    print(f"Difficulty of the course: {CourseDt.getDificultad()}")
    print(f"Subject: {CourseDt.getNaMonthubject()}")
    print(f"Enabled: {CourseDt.getHabilitado()}")
    if CourseDt.getcountLessons()!= 0:
        Lessons = CourseDt.getLessons()
        for lv in Lessons.values():
            print(f"Number lesson {lv.getOrder()} \n Topic: {lv.getTopic()} \n Goal: {lv.getGoal()}")
            Exercises =  lv.getExercises()
            if len(Exercises) != 0:
                for ej in Exercises.values():
                    print(f"Exercise description: {ej.getDescription()}")
            else: print("It doesn't have exercises.")
    else: print("It doesn't have Lessons.")
    StudentsInscriptos = CourseDt.MAPgetStudentsInscription()
    if len(StudentsInscriptos) !=0:
        for e in StudentsInscriptos.values():
            ins = e.getRegistration(Course)
            dateIns = ins.getDateDeRegistration()
            print(f"Name Student: {e.getName()} \n Date of inscription: {dateIns.getDay()}/{dateIns.getMonth()}/{dateIns.getYear()}")
    else: 
        print("It doesn't have students inscriptos")

def cargarDatas():
    f = Factory()
    ctrCourse = f.getICourse()
    ctrUser = f.getIUser()
    #Subject DAR register
    ctrCourse.EnterSubject("Math")
    ctrCourse.ConfirmSubject()
    #User DAR register (Professor)
    ctrUser.EnterDatasUser("prof","123456","Math Teacher","Prof")
    ctrUser.EnterInstitute("IFD")
    ctrUser.AddSpecialization("Math")
    ctrUser.ConfirmRegisterProfessor()
    #User DAR register Student
    ctrUser.EnterDatasUser("Marcos","123456","I am Student","Marcos")
    Day = 15
    Month = 12
    Year = 1990
    DateBirth = DTDate(Year, Month, Day)
    ctrUser.EnterDataStudent("Uruguay",DateBirth)
    ctrUser.ConfirmRegisterStudent()
    #register Course (maTopictica1)
    ctrCourse.SelectProfessor("prof")
    ctrCourse.EnterDatasCourse("math1", "Ecuaciones", "b")
    ctrCourse.SelectSubject("Math")
    ctrCourse.RequiresPrerequisite(False)
    ctrCourse.ConfirmRegisterCourse()
    #Add Lesson Y ExerciseS A maTopictica1 (una 2 Lessons y 2 Exercises en solo la lección 1)
    #Lesson 1
    #Exercise 1 - completar
    ctrCourse.SelectCourse("math1")
    ctrCourse.CreateLesson("Equations","Solve first-degree equations", "math1")
    Solutions = dict()
    Solutions[1]="10"
    ctrCourse.CreateExerciseCompleteWord("Equations first-degree", "x + 10 = 20, then x = ---", Solutions)
    #Exercise 2 - Multiple Choice    
    CorrectOption = "1"
    Options = dict()
    Options[1] = "-30"
    Options[2] = "30"
    ctrCourse.CreateExerciseMultipleChoice("Choice the correct option", "x + 30 = 0, then x = ", Options, CorrectOption)
    ctrCourse.DarDeRegisterLesson()
    #Lesson2
    ctrCourse.SelectCourse("math1")
    ctrCourse.CreateLesson("Function","Imagen", "math1")
    CorrectOption = "2"
    Options = dict()
    Options[1] = "10"
    Options[2] = "-10"
    ctrCourse.CreateExerciseMultipleChoice("Choice the correct option", "f(x) = -10, then f(5)= ", Options, CorrectOption)
    ctrCourse.DarDeRegisterLesson()
    ctrCourse.SelectCourse("math1")
    #ctrCourse.MakeCourseAvailable()

    #register Course (maTopictica2)
    ctrCourse.SelectProfessor("prof")
    ctrCourse.EnterDatasCourse("math2", "Equations", "i")
    ctrCourse.SelectSubject("Math")
    ctrCourse.RequiresPrerequisite(True)
    ctrCourse.SelectPrerequisites("math1")
    ctrCourse.ConfirmRegisterCourse()
    #Lesson 1 Course math2
    ctrCourse.SelectCourse("math2")
    ctrCourse.CreateLesson("Equations second-degree","Solve second-degree Equations", "math2")
    #Exercise 1 de la Lesson 1
    Solutions = dict()
    Solutions[1]="2"
    Solutions[2]="-2"
    ctrCourse.CreateExerciseCompleteWord("Equations second-degree", "x^2 - 4 = 0, then x = --- y ---", Solutions)
    ctrCourse.DarDeRegisterLesson()
    ctrCourse.SelectCourse("math2")
    ctrCourse.MakeCourseAvailable()




def ExecuteExercise():
    a = Factory()
    ctrUser = a.getIUser()
    ctrCourse = a.getICourse()
    nickname = input("Enter nickname: ")
    if ctrUser.NicknameAvailable(nickname):
        ctrUser.EnterNickname(nickname)
        CoursesInscriptosNoApproved = ctrUser.GetCoursesInscriptoNoAprobado(nickname)
        print("Courses not yet approved: ")
        if len(CoursesInscriptosNoApproved) != 0:
            for i in CoursesInscriptosNoApproved:
                print(f"- {i.getCourseInscripto()} ")
            Course  =  input("Enter name of the Course: ")
            while (not ctrCourse.ExistsCourse(Course)):
                Course = input("Incorrect course name, please enter it again: ")
            ctrUser.EnterCourseSeleccionado(Course)
            ExercisesNoApproved = ctrUser.GetExercisesNoApproved()
            print("Exercises no Approved:")
            for e in ExercisesNoApproved:
                print(f"Exercise id: {e.getId()}, Description: {e.getDescription()}")
            
            ExerciseSelect = int(input("Enter the identifier of the exercise you want to execute: "))
            ctrUser.RememberExercise(ExerciseSelect)
            ej = ctrUser.mostrarExercise()
            if ej:
                r = (input("Enter the words separated by commas: ")).replace(" ", "").split(",")
                c = ctrUser.cantidadWordsACompletar()
                reSolution = dict()
                count = 1
                while c >= count:
                    reSolution[count] = r[count-1]
                    count+=1
                if ctrUser.ResolveCompleteWord(reSolution):
                    print("Congratulations, the entered words are correct.")
                else: print("the entered words are incorrect")
            else:
                opcion = input("Enter one of the options (number): ")
                if ctrUser.ResolveMultipleChoice(opcion):
                    print("Felicitaciones, la opción ingresada es la correcta.")
                    
                else: print("You entered the incorrect option: ")
        else: print("All the courses have been approved.")
        
    else: print("Nickname incorrecto")


def ConsultStatistics():
    a = Factory()
    ctrUser = a.getIUser()
    ctrCourse = a.getICourse()
    e = input("""Choose one of the following options: \n
              Statistics Student (e)\n
              Statistics Professor (p) \n
              Statistics Course (c)\n
              Enter the option: """)
    if e.lower().strip() == "e":
        Students = ctrCourse.GetStudents()
        for e in Students:
            print(e)
        nickname = input("Enter nickname: ")
        if ctrUser.NicknameAvailable(nickname):
           ctrCourse.MAPGetAdvancedCourses(nicknaMonthtudent=nickname)

        else: print("Incorrect nickname ")
        
    elif  e.lower().strip() == "p":
        nicknameProfessors = ctrCourse.GetNickname()
        for p in nicknameProfessors:
            print(p)
        nickname = input("Enter the professor's nickname: ")
        if ctrUser.NicknameAvailable(nickname):
           ctrCourse.MAPGetAdvancedCourses(nicknameProfessor=nickname)

        else: print("Incorrect nickname ")
    elif  e.lower().strip() == "c":
        Courses = ctrCourse.SETGetCourses()
        for c in Courses:
            print(c.getName())
        Course  =  input("Enter the course's name: ")
        if ctrCourse.ExistsCourse(Course):
            ctrCourse.MAPGetAdvancedCourses(Course=Course)
    else: 
        print("Incorrect choice")


def deleteCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    Courses = ctrCourse.SETGetCourses()
    for c in Courses:
        print(c.getName())
    Course  =  input("Enter the course's name: ")
    if ctrCourse.ExistsCourse(Course):
        ctrCourse.deleteCourse(Course)
    else: 
        print("Name incorrect")

def suscribirseNorificaciones():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.NicknameAvailable(nickname=nickname):
        subjects = ctrUser.GetSubjectUnsubscribed (nickname)
        for a in subjects:
            print(a)
        number_of_subscriptions = 0
        for a in subjects:
            selectSubject = input("Enter the subject you wish to subscribe to: ")
            if selectSubject in subjects:
                ctrUser.AgreagarSuscripcion(nickname, selectSubject)
                number_of_subscriptions +=1
                if number_of_subscriptions < len(subjects):
                    Continue = input("Do you want tu subscribe to another subject? Yes/No: ")
                    if Continue.lower().strip() == "no":
                        break
                else: print("You are subscribe to all subjects") 
            else:
                print(" ERROR ")
            
    else:
        print(" ERROR ")
            
def consultNotify():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.NicknameAvailable(nickname=nickname):
        Notifications = ctrUser.GetNotifications(nickname)
        for n in Notifications:
            print(n)
        ctrUser.DeleteNotifiaciones(nickname)

def DeleteSubscriptions():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.NicknameAvailable(nickname=nickname):
        subjectSubscribers = ctrUser.GetSubscriptions(nickname)
        for s in subjectSubscribers:
            print(s)
        number_of_subscriptions = 0
        for s in subjectSubscribers:
            selectSubject = input("Enter the subject you wish to unsubscribe : ")
            if selectSubject in subjectSubscribers:
                ctrUser.DeleteSubscriptions(nickname, selectSubject)
                number_of_subscriptions +=1
                if number_of_subscriptions < len(subjectSubscribers):
                    Continue = input("Do you want tu unsubscribe to another subject? Yes/No: ")
                    if Continue.lower().strip() == "no":
                        break
                else: print("You unsubscribed from all subjects") 
            else:
                print(" ERROR ")

    else: 
        print("Nickname incorrecto")
    
    


def main():
    Continue = True
    while Continue == True:
        print('''Choose the following use cases:
              1- Load data
              2- Register from Subject
              3- Consult Subject
              4- Register user
              5- Consult Users
              6- Register of course
              7- Course enable
              8- Add lesson
              9- Add exercise
              10- Register for a Course
              11- Consult Course
              12- Execute exercise
              13- Consult Statistics
              14- Delete Course
              15- Subscribe a Subject
              16- Check Notifications
              17- Delete subscription
              18- EXIT''')
        
        choice = input("Choice: ").strip()
    
        if choice == "1":
            cargarDatas()
    #register Subject
        if choice == "2":
            registerSubject()
    #Consult Subject
        elif choice == "3":
            ConsultSubject()
    #register DE User:
        elif choice == "4":
            registerUser()
    #Consult User:
        elif choice == "5":
            ConsultUser()
    
        elif choice == "6":
            registerCourse()
            
        elif choice == "7":
            MakeCourseAvailable()
        
        elif choice == "8":
            AddLesson()
            
        elif choice == "9":
            AddExercise()

        elif choice == "10":
            RegistrationCourse()

        elif choice == "11":
            ConsultCourse()

        elif choice == "12":
            ExecuteExercise()
        
        elif choice == "13":
            ConsultStatistics()

        elif choice == "14":
            deleteCourse()

        elif choice == "15":
            suscribirseNorificaciones()

        elif choice == "16":
            consultNotify()

        elif choice == "17":
            DeleteSubscriptions()

        elif choice == "18":
            Continue = False

if __name__ == "__main__":
    main()
