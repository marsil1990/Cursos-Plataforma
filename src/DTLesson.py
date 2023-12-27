from src.DTExercise import DTExercise
class DTLesson:
    def __init__(self, Order = None, Topic = None, Goal=None, lesson = None):
        if lesson is None:
            self.__Order = Order
            self.__Topic =  Topic
            self.__Goal = Goal
        else:
            from src.Lesson import Lesson
            self.__Order = lesson.getOrder()
            self.__Topic =  lesson.getTopic()
            self.__Goal = lesson.getGoal()
            self.__Exercises = dict()
            Exercises = lesson.MAPgetColExercises()
            for ek, ev in Exercises.items():
                self.__Exercises[ek] = DTExercise(Exercise=ev)


    def getOrder(self):
        return self.__Order
    def getTopic(self):
        return self.__Topic
    def getGoal(self):
        return self.__Goal
    def getExercises(self):
        return self.__Exercises
    