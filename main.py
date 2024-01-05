from src.Factory import Factory
from src.DTDate import DTDate
from datetime import datetime

def registerSubject():
    a = Factory()
    ctrCourse = a.getICourse()
    enter_subject = input("Enter Subject: ")
    while enter_subject.strip() == "":
        enter_subject = input("It cannot be empty. Enter Subject: ")
    ctrCourse.enterSubject(enter_subject)
    conf = ctrCourse.confirmSubject()
    if conf:
        print("The subject was entered correctly")
    else: print("The subject already exists")

def consultSubject():
    a = Factory()
    ctrCourse = a.getICourse()
    setSubjects = ctrCourse.consultSubject()
    for i in setSubjects:
        print(i[0].upper()+i[1:])


def registerUser():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    while ctrUser.nicknameAvailable(nickname) and nickname!= "":
        nickname = input("The entered nickname is not available. Please enter Yearther one: ")
    Password = input("Enter password (minimum 6 characters): ")
    while len(Password) < 6 :
        Password = input("The password must be at least 6 characters long. Please try again: ")
    Name = input("Enter name: ")
    Description = input("Enter description: ")
    TypeUser = input("Are you a professor or a student?(p/s): ")
    ctrUser.enterDatasUser(nickname,Password,Description, Name)
    if (TypeUser.lower().strip()== "s" ):
        nameCountry = input("Enter the country where you live: ")
        print("Enter date of birth: ")
        Day = int(input("Day: "))
        Month = int(input("Month: "))
        Year = int(input("Year: "))
        dateBirth = DTDate(Day, Month, Year)
        ctrUser.enterDataStudent(nameCountry,dateBirth)
        ctrUser.confirmRegisterStudent()
    elif (TypeUser.lower().strip() == "p"):
        Institute = input("Enter the institute where you work: ")
        ctrUser.enterInstitute(Institute)
        setSubjectsAvailables = ctrUser.getSubjectsAvailables()
        #mostrar los Subjects
        for i in setSubjectsAvailables:
            print(i)
        Continue = True
        while Continue:
            Specialization = input("Choose an available subject: ")
            if ctrUser.existsSubject(Specialization):
                ctrUser.addSpecialization(Specialization)
            else:
                print("The entered subject is not correct, please try again: ")
            cont = input("Do you want to add another subject? Yes/No: ")
            if cont.strip().lower() ==  "no":
                Continue = False
                    
        ctrUser.confirmregisterProfessor()
    else:
        print("The entered user type is not correct.")


def ConsultUser():
    a = Factory()
    ctrUser = a.getIUser()
    SETnicknameUsers = ctrUser.getNicknameUsers()
    if len(SETnicknameUsers) != 0:
        for u in SETnicknameUsers:
            print(u)
        nickname_User = input("Enter the user's nickname: ")
        if(ctrUser.nicknameAvailable(nickname_User)):
            ctrUser.selectUser(nickname_User)
        else: 
            print("The entered nickname is not correct")
    else: 
        print ("There are no registered users.")
    

def registerCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessors = ctrCourse.getNickname()
    for p in nicknameProfessors:
        print(p)
    nickname = input("Enter the professor's nickname: ")
    if nickname in nicknameProfessors:
        ctrCourse.selectProfessor(nickname)
        nameCourse = input("Name Course: ")
        while (ctrCourse.existsCourse(nameCourse)):
            nameCourse = input("The course name already exists. Please enter another one: ")
        DescriptionCourse = input("Course description: ")
        LevelCourse = input("Course level (Beginner (B)/Intermediate (I)/Advanced (A)): ")
        while (LevelCourse.strip().lower() != "b" and LevelCourse.strip().lower() != "i" and 
                LevelCourse.strip().lower() != "a"):
            LevelCourse = input("Enter only b, i o a: ")
        ctrCourse.enterDatasCourse(nameCourse, DescriptionCourse, LevelCourse)
        setSubjects =  ctrCourse.getSubjectsSpecialization()
        for i in setSubjects:
            print(i)
        Subject = input("Enter subject: ")
        while (not(Subject in setSubjects)):
            Subject = input("Incorrect, please enter the subject again: ")
        ctrCourse.selectSubject(Subject)
        Prerequisite = input("Requires previous approved courses? Yes/No: ")
        conf = False
        if Prerequisite.strip().lower() == "yes":
            conf = True
            ctrCourse.requirisPrerequisite(conf) 
            colCoursesAvailable = ctrCourse.SETgetCoursesAvailable()
            print("Courses created by the same professor.")
            if len(colCoursesAvailable) != 0:
                for c in colCoursesAvailable:
                    print(c)
                Prerequisites = input("Enter, separated by commas, the courses that will be prerequisites: ")
                ctrCourse.selectPrerequisites(Prerequisites)
            else: print("There are no available courses")
        ctrCourse.confirmRegisterCourse()
        AddLessons = input("Do you want to add lessons? Yes/No: ")
        while AddLessons.strip().lower() =="yes":
            ctrCourse.selectCourse(nameCourse)
            Topic = input("Enter the topic of the lesson: ")
            Goal = input("Enter the goal of the lesson: ")
            #ctrCourse.createDatasLesson(Topic, Goal)
            ctrCourse.createLesson(Topic, Goal, nameCourse)
            addExercises = input("Do you want to add exercises? Yes/No: ")
            while addExercises.strip().lower() == "yes":
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
                    ctrCourse.createExerciseCompleteWord(Description, Sentence, Solutions)
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
                    ctrCourse.createExerciseMultipleChoice(Description, Question, Options, CorrectOption)
                else: print("Incorrect option entry")
                addExercises = input("Do you want to add another exercise? Yes/No: ")
            ctrCourse.confirmLesson()
            AddLessons = input("Do you want to add another lesson? Yes/No: ")
    else: print("Inconrrect nickName")
        

def makeCourseAvailable():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessors = ctrCourse.getNickname()
    nicknameProfessor = input("Enter the professor's nickname: ")
    if nicknameProfessor in nicknameProfessors:
        colCoursesNoAvailable =  ctrCourse.getCoursesNoAvailable(nicknameProfessor)
        for c in colCoursesNoAvailable:
            print (c)
        course = input("Enter Course: ")
        while (not ctrCourse.existsCourse(course)):
            course = input("Incorrect course name, please enter it again: ")
        ctrCourse.selectCourse(course)
        correcto = ctrCourse.makeCourseAvailable()
        if correcto:
            ctrCourse.notify(course)
            print("It was successfully enabled")
        else:
            print("It was not enabled")

def AddLesson():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessor = input("Enter the professor's nickname: ")
    nicknameProfessors = ctrCourse.getNickname()
    while(not (nicknameProfessor in nicknameProfessors)):
        nicknameProfessor = input("Incorrect nickname, Enter the professor's nickname: ")
    colCoursesNoAvailable =  ctrCourse.getCoursesNoAvailable(nicknameProfessor)
    for c in colCoursesNoAvailable:
        print (c)
    Course = input("Enter Course: ")
    while (not ctrCourse.existsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    ctrCourse.selectCourse(Course)
    Topic = input("Enter the topic of the lesson: ")
    Goal = input("Enter Goal of the lesson: ")
    #ctrCourse.createDatasLesson(Topic, Goal)
    ctrCourse.createLesson(Topic, Goal, Course)
    addExercises = input("Do you want to add exercises? Yes/No: ")
    while addExercises.strip().lower() == "yes":
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
            ctrCourse.createExerciseCompleteWord(Description, Sentence, Solutions)
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
            ctrCourse.createExerciseMultipleChoice(Description, Question, Options, CorrectOption)
        else: print("Incorrect option entry")
        addExercises = input("Do you want to add another exercise? Yes/No: ")
    ctrCourse.confirmLesson()

def addExercise():
    a = Factory()
    ctrCourse = a.getICourse()
    nicknameProfessor = input("Enter the professor's nickname: ")
    nicknameProfessors = ctrCourse.getNickname()
    while(not (nicknameProfessor in nicknameProfessors)):
        nicknameProfessor = input("Incorrect nickname, Enter the professor's nickname: ")
    colCoursesNoAvailable =  ctrCourse.getCoursesNoAvailable(nicknameProfessor)
    for c in colCoursesNoAvailable:
        print (c)
    Course = input("Enter Course: ")
    while (not ctrCourse.existsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    ctrCourse.selectCourse(Course)
    Lessons = ctrCourse.MAPgetLessons()
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
            ctrCourse.createExerciseCompleteWord(Description, Sentence, Solutions)
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
            ctrCourse.createExerciseMultipleChoice(Description, Question, Options, CorrectOption)
        else: 
            TypeExercise = input("Enter the exercise type (only the number): 1 - Fill in the Blank, 2 - Multiple Choice: ")
        s = input("Do you want to continue adding exercises? Yes/No: ")
        if s.strip().lower() == "no":
            ContinueAdding = False

def RegistrationCourse():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.nicknameAvailable(nickname):
        ctrUser.enterNickname(nickname)
        CoursesAvailable = ctrUser.getCoursesAvailableforRegistration(nickname)
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
            
            ctrUser.enterCourseSeleccionado(nameCourse)
            Date_actual = datetime.now()
            f = DTDate(Date_actual.year, Date_actual.month, Date_actual.day)
            RegistrationCorrecta = ctrUser.finalizarRegistrationACourse(nickname, f)
            if RegistrationCorrecta:
                print( "The registration was completed successfully.")
            
            else:
               print("There was an issue during the registration. Please try again.")
            
    else: print("No user exists with that nickname.")

def ConsultCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    Courses = ctrCourse.SETgetCourses()
    for c in Courses:
        print(c.getName())
    Course  =  input("Write the name of the course: ")
    while (not ctrCourse.existsCourse(Course)):
        Course = input("Incorrect course name, please enter it again: ")
    CourseDt = ctrCourse.getCourse(Course)
    print(f"Name of the Course: {CourseDt.getName()}")
    print(f"Difficulty of the course: {CourseDt.getDifficulty()}")
    print(f"Subject: {CourseDt.getNameSubject()}")
    print(f"Enabled: {CourseDt.getEnabled()}")
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
    ctrCourse.enterSubject("Math")
    ctrCourse.confirmSubject()
    #User DAR register (Professor)
    ctrUser.enterDatasUser("prof","123456","Math Teacher","Prof")
    ctrUser.enterInstitute("IFD")
    ctrUser.addSpecialization("Math")
    ctrUser.confirmregisterProfessor()
    #User DAR register Student
    ctrUser.enterDatasUser("Marcos","123456","I am Student","Marcos")
    Day = 15
    Month = 12
    Year = 1990
    dateBirth = DTDate(Year, Month, Day)
    ctrUser.enterDataStudent("Uruguay",dateBirth)
    ctrUser.confirmRegisterStudent()
    #register Course (maTopictica1)
    ctrCourse.selectProfessor("prof")
    ctrCourse.enterDatasCourse("math1", "Ecuaciones", "b")
    ctrCourse.selectSubject("Math")
    ctrCourse.requirisPrerequisite(False)
    ctrCourse.confirmRegisterCourse()
    #Add Lesson Y ExerciseS A maTopictica1 (una 2 Lessons y 2 Exercises en solo la lección 1)
    #Lesson 1
    #Exercise 1 - completar
    ctrCourse.selectCourse("math1")
    ctrCourse.createLesson("Equations","Solve first-degree equations", "math1")
    Solutions = dict()
    Solutions[1]="10"
    ctrCourse.createExerciseCompleteWord("Equations first-degree", "x + 10 = 20, then x = ---", Solutions)
    #Exercise 2 - Multiple Choice    
    CorrectOption = "1"
    Options = dict()
    Options[1] = "-30"
    Options[2] = "30"
    ctrCourse.createExerciseMultipleChoice("Choice the correct option", "x + 30 = 0, then x = ", Options, CorrectOption)
    ctrCourse.confirmLesson()
    #Lesson2
    ctrCourse.selectCourse("math1")
    ctrCourse.createLesson("Function","Imagen", "math1")
    CorrectOption = "2"
    Options = dict()
    Options[1] = "10"
    Options[2] = "-10"
    ctrCourse.createExerciseMultipleChoice("Choice the correct option", "f(x) = -10, then f(5)= ", Options, CorrectOption)
    ctrCourse.confirmLesson()
    ctrCourse.selectCourse("math1")
    #ctrCourse.makeCourseAvailable()

    #register Course (maTopictica2)
    ctrCourse.selectProfessor("prof")
    ctrCourse.enterDatasCourse("math2", "Equations", "i")
    ctrCourse.selectSubject("Math")
    ctrCourse.requirisPrerequisite(True)
    ctrCourse.selectPrerequisites("math1")
    ctrCourse.confirmRegisterCourse()
    #Lesson 1 Course math2
    ctrCourse.selectCourse("math2")
    ctrCourse.createLesson("Equations second-degree","Solve second-degree Equations", "math2")
    #Exercise 1 de la Lesson 1
    Solutions = dict()
    Solutions[1]="2"
    Solutions[2]="-2"
    ctrCourse.createExerciseCompleteWord("Equations second-degree", "x^2 - 4 = 0, then x = --- y ---", Solutions)
    ctrCourse.confirmLesson()
    ctrCourse.selectCourse("math2")
    ctrCourse.makeCourseAvailable()




def ExecuteExercise():
    a = Factory()
    ctrUser = a.getIUser()
    ctrCourse = a.getICourse()
    nickname = input("Enter nickname: ")
    if ctrUser.nicknameAvailable(nickname):
        ctrUser.enterNickname(nickname)
        CoursesInscriptosNoApproved = ctrUser.getCoursesInscriptoNoAprobado(nickname)
        print("Courses not yet approved: ")
        if len(CoursesInscriptosNoApproved) != 0:
            for i in CoursesInscriptosNoApproved:
                print(f"- {i.getEnrolledCourse()} ")
            Course  =  input("Enter name of the Course: ")
            while (not ctrCourse.existsCourse(Course)):
                Course = input("Incorrect course name, please enter it again: ")
            ctrUser.enterCourseSeleccionado(Course)
            exercisesNoApproved = ctrUser.getExercisesNoApproved()
            print("Exercises no Approved:")
            for e in exercisesNoApproved:
                print(f"Exercise id: {e.getId()}, Description: {e.getDescription()}")
            try:
                exerciseSelect = int(input("Enter the identifier of the exercise you want to execute: "))
            except:
                print("Debe ingresar un número")
            ctrUser.rememberExercise(exerciseSelect)
            ej = ctrUser.mostrarExercise()
            if ej:
                r = (input("Enter the words separated by commas: ")).replace(" ", "").split(",")
                c = ctrUser.cantidadWordsACompletar()
                reSolution = dict()
                count = 1
                while c >= count:
                    reSolution[count] = r[count-1]
                    count+=1
                if ctrUser.resolveCompleteWord(reSolution):
                    print("Congratulations, the entered words are correct.")
                else: print("the entered words are incorrect")
            else:
                opcion = input("Enter one of the options (number): ")
                if ctrUser.resolveMultipleChoice(opcion):
                    print("Congratulations, the entered option is correct.")
                    
                else: print("You entered the incorrect option: ")
        else: print("All the courses have been approved.")
        
    else: print("Nickname incorrecto")


def ConsultStatistics():
    a = Factory()
    ctrUser = a.getIUser()
    ctrCourse = a.getICourse()
    e = input("""Choose one of the following options: \n
              Statistics Student (s)\n
              Statistics Professor (p) \n
              Statistics Course (c)\n
              Enter the option: """)
    if e.lower().strip() == "s":
        Students = ctrCourse.GetStudents()
        for e in Students:
            print(e)
        nickname = input("Enter nickname: ")
        if ctrUser.nicknameAvailable(nickname):
           ctrCourse.MAPGetAdvancedCourses(nicknaMonthtudent=nickname)

        else: print("Incorrect nickname ")
        
    elif  e.lower().strip() == "p":
        nicknameProfessors = ctrCourse.getNickname()
        for p in nicknameProfessors:
            print(p)
        nickname = input("Enter the professor's nickname: ")
        if ctrUser.nicknameAvailable(nickname):
           ctrCourse.MAPGetAdvancedCourses(nicknameProfessor=nickname)

        else: print("Incorrect nickname ")
    elif  e.lower().strip() == "c":
        Courses = ctrCourse.SETgetCourses()
        for c in Courses:
            print(c.getName())
        Course  =  input("Enter the course's name: ")
        if ctrCourse.existsCourse(Course):
            ctrCourse.MAPGetAdvancedCourses(Course=Course)
    else: 
        print("Incorrect choice")


def deleteCourse():
    a = Factory()
    ctrCourse = a.getICourse()
    Courses = ctrCourse.SETgetCourses()
    for c in Courses:
        print(c.getName())
    Course  =  input("Enter the course's name: ")
    if ctrCourse.existsCourse(Course):
        ctrCourse.deleteCourse(Course)
    else: 
        print("Name incorrect")

def suscribirseNorificaciones():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.nicknameAvailable(nickname=nickname):
        subjects = ctrUser.getSubjectUnsubscribed (nickname)
        for a in subjects:
            print(a)
        number_of_subscriptions = 0
        for a in subjects:
            selectSubject = input("Enter the subject you wish to subscribe to: ")
            if selectSubject in subjects:
                ctrUser.addSuscription(nickname, selectSubject)
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
            
def consultnotify():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.nicknameAvailable(nickname=nickname):
        Notifications = ctrUser.GetNotifications(nickname)
        for n in Notifications:
            print(n)
        ctrUser.deleteNotifiaciones(nickname)

def deleteSubscriptions():
    a = Factory()
    ctrUser = a.getIUser()
    nickname = input("Enter nickname: ")
    if ctrUser.nicknameAvailable(nickname=nickname):
        subjectSubscribers = ctrUser.GetSubscriptions(nickname)
        for s in subjectSubscribers:
            print(s)
        number_of_subscriptions = 0
        for s in subjectSubscribers:
            selectSubject = input("Enter the subject you wish to unsubscribe : ")
            if selectSubject in subjectSubscribers:
                ctrUser.deleteSubscriptions(nickname, selectSubject)
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
              2- Register Subject
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
            consultSubject()
    #register DE User:
        elif choice == "4":
            registerUser()
    #Consult User:
        elif choice == "5":
            ConsultUser()
    
        elif choice == "6":
            registerCourse()
            
        elif choice == "7":
            makeCourseAvailable()
        
        elif choice == "8":
            AddLesson()
            
        elif choice == "9":
            addExercise()

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
            consultnotify()

        elif choice == "17":
            deleteSubscriptions()

        elif choice == "18":
            Continue = False

if __name__ == "__main__":
    main()
