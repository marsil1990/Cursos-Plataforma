class DTExercise:
    def __init__(self, Id = None, Description=None, Exercise = None):
        if Exercise is None:
            self.__Id = Id
            self.__Description = Description
        else:
            self.__Id = Exercise.getId()
            self.__Description = Exercise.getDescription()
       
    def getDescription(self):
        return self.__Description
    def getId(self):
        return self.__Id
    
    