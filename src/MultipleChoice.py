from src.Exercise import Exercise
class MultipleChoice(Exercise):
    def __init__(self, Id, Description, Question, Options, CorrectOption):
        super().__init__(Id, Description)
        self.__oracion = Question
        self.__MAPOptions = Options
        self.__CorrectOption = CorrectOption

    def getOracion(self):
        return self.__oracion
    def getOptions(self):
        return self.__MAPOptions
    def getCorrectOption(self):
        return self.__CorrectOption