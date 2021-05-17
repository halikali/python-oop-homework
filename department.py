class Department():
    def __init__(self,cName,cPhoneNumber):
        self.__name=cName
        self.__phone=cPhoneNumber

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name=value

    @property
    def Phone(self):
        return self.__phone
    @Phone.setter
    def Phone(self,value):
        self.__phone=value

    def __str__(self):
        return "Bölüm Adı: " + self.Name+"\n Telefon Numarası:"+self.Phone
    