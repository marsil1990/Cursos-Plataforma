class DTExercise:
    def __init__(self, Id = None, description=None, exercise = None):
        if exercise is None:
            self.__Id = Id
            self.__description = description
        else:
            self.__Id = exercise.getId()
            self.__description = exercise.getDescription()
       
    def getDescription(self):
        return self.__description
    def getId(self):
        return self.__Id
    
    