class DTUser:
    def __init__(self, nickname, password, name, description):
        self.__nickname = nickname
        self.__password = password
        self.__name = name
        self.__description = description
    def getNickname(self):
        return self.__nickname
    def getPassword(self):
        return self.__password
    def getDescription(self):
        return self.__description
    def getName(self):
        return self.__name
   