from src.Exercise import Exercise
class CompleteWord(Exercise):
    def __init__(self, Id, Description, Sentence, WordsFaltantes):
        super().__init__(Id, Description)
        self.__Sentence = Sentence
        self.__MAPWordsFaltantes = WordsFaltantes
        

    def  getSentence(self):
        return self.__Sentence
    def getWordsFaltantes(self):
        return self.__MAPWordsFaltantes
    def getCantidadWords(self):
        return len(self.__MAPWordsFaltantes)
    def EnterSolution(self, MAPSolution):
        count = 0
        for i in self.__MAPWordsFaltantes:
            if self.__MAPWordsFaltantes[i] == MAPSolution[i]:
                count += 1
        return count == self.getCantidadWords()
        

    