from src.Exercise import Exercise
class MultipleChoice(Exercise):
    def __init__(self, Id, description, question, options, correctOption):
        super().__init__(Id, description)
        self.__question= question
        self.__MAPOptions = options
        self.__correctOption = correctOption

    def getOracion(self):
        return self.__question
    def getOptions(self):
        return self.__MAPOptions
    def getCorrectOption(self):
        return self.__correctOption