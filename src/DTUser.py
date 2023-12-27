class DTUser:
    def __init__(self, Nickname, Password, Name, Description):
        self.__Nickname = Nickname
        self.__Password = Password
        self.__Name = Name
        self.__Description = Description
    def getNickname(self):
        return self.__Nickname
    def getPassword(self):
        return self.__Password
    def getDescription(self):
        return self.__Description
    def getName(self):
        return self.__Name
   