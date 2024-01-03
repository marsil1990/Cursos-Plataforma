from src.CompleteWord import CompleteWord
from src.MultipleChoice import MultipleChoice
class Lesson:
    def __init__(self, order, topic, goal, exercises = None):
        self.__order = order
        self.__topic = topic
        self.__goal = goal
        if exercises is None:
           self.__MAPExercise = dict()
        else:
           self.__MAPExercise =  exercises
    
    def getOrder(self): 
        return self.__order
    def getTopic(self):
        return self.__topic
    def getGoal(self):
        return self.__goal
    def addCompletionExercise(self, description, sentence,  MAPrespuesta):
        n = len(self.__MAPExercise) + 1
        ej = CompleteWord(n , description, sentence, MAPrespuesta)
        self.__MAPExercise[n] = ej
        

    def addExerciseMultiple(self, description, question, options, correctOption):
        n = len(self.__MAPExercise) + 1
        ej = MultipleChoice(n , description,question, options, correctOption)
        self.__MAPExercise[n] = ej

        
    def numberOfExercises(tot, ap, nickStudent): pass
   
    def getExercise(self, Id):
        return self.__MAPExercise[Id]
    def getcountExercises(self):
        return len(self.__MAPExercise)
    def setOrder(Order): pass
    def MAPgetColExercises(self):
        return self.__MAPExercise
    def removeExercises(self):
        for e in self.__MAPExercise.values():
            e.removeStudentsApproved()
        self.__MAPExercise.clear()
        del self.__MAPExercise