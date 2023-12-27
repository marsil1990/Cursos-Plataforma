from src.CompleteWord import CompleteWord
from src.MultipleChoice import MultipleChoice
class Lesson:
    def __init__(self, Order, Topic, Goal, Exercises = None):
        self.__Order = Order
        self.__Topic = Topic
        self.__Goal = Goal
        if Exercises is None:
           self.__MAPExercise = dict()
        else:
           self.__MAPExercise =  Exercises
    
    def getOrder(self): 
        return self.__Order
    def getTopic(self):
        return self.__Topic
    def getGoal(self):
        return self.__Goal
    def añadirExerciseCompletar(self, Description, Sentence,  MAPrespuesta):
        n = len(self.__MAPExercise) + 1
        ej = CompleteWord(n , Description, Sentence, MAPrespuesta)
        self.__MAPExercise[n] = ej
        

    def añadirExerciseMultiple(self, Description, Question, Options, CorrectOption):
        n = len(self.__MAPExercise) + 1
        ej = MultipleChoice(n , Description,Question, Options, CorrectOption)
        self.__MAPExercise[n] = ej
    def contarExercises(tot, ap, nickStudent): pass
    def SETGetNoApproved(): pass
    def GetExercise(self, Id):
        return self.__MAPExercise[Id]
    def getcountExercises(self):
        return len(self.__MAPExercise)
    def setOrder(Order): pass
    def MAPgetColExercises(self):
        return self.__MAPExercise
    def eliminarExercises(self):
        for e in self.__MAPExercise.values():
            e.eliminarStudentsApproved()
        self.__MAPExercise.clear()
        del self.__MAPExercise