class Staff():
    def __init__(self):
        self.__name=None
        self.__adress=None
        self.__price=None
        self.__department=None

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,value):
        self.__name = value
    
    @property
    def Adress(self):
        return self.__adress
    
    @Adress.setter
    def Adress(self,value):
        self.__adress = value
    
    
    @property
    def Price(self):
        return self.__price
    
    @Price.setter
    def Price(self,value):
        self.__price = value
    
    
    @property
    def Department(self):
        return self.__department
    
    @Department.setter
    def Department(self,value):
        self.__department = value
    
    def __str__(self):
        return self.Name+"\n"+self.Adress+"\n"+str(self.Price)+"\n"+str(self.Department)

    def showProfile(self):
        print(self.Name,"\n",self.Adress,"\n Maaş : ",str(self.Price),"\n",str(self.Department))
    