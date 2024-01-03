from src.Exercise import Exercise
class CompleteWord(Exercise):
    def __init__(self, Id, Description, Sentence, WordsFaltantes):
        super().__init__(Id, Description)
        self.__Sentence = Sentence
        self.__getMissingWords = WordsFaltantes
        

    def  getSentence(self):
        return self.__Sentence
    def getMissingWords(self):
        return self.__getMissingWords
    def getWordCount(self):
        return len(self.__getMissingWords)
    def EnterSolution(self, MAPSolution):
        count = 0
        for i in self.__getMissingWords:
            if self.__getMissingWords[i] == MAPSolution[i]:
                count += 1
        return count == self.getWordCount()
        

    