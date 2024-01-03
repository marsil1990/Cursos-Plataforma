from src.DTExercise import DTExercise
class DTLesson:
    def __init__(self, order = None, topic = None, goal=None, lesson = None):
        if lesson is None:
            self.__order = order
            self.__topic =  topic
            self.__goal = goal
        else:
            from src.Lesson import Lesson
            self.__order = lesson.getOrder()
            self.__topic =  lesson.getTopic()
            self.__goal = lesson.getGoal()
            self.__exercises = dict()
            exercises = lesson.MAPgetColExercises()
            for ek, ev in exercises.items():
                self.__exercises[ek] = DTExercise(exercise=ev)


    def getOrder(self):
        return self.__order
    def getTopic(self):
        return self.__topic
    def getGoal(self):
        return self.__goal
    def getExercises(self):
        return self.__exercises
    