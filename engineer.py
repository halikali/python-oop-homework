import staff
class Engineer(staff.Staff):
    def __init__(self):
        super().__init__()
        self.__abilities=[]
    
    @property
    def Abilities(self):
        return self.__abilities
    @Abilities.setter
    def Abilities(self,value):
        self.__abilities=value
    
    def showProfile(self):
        super().showProfile()
        print("Yetenkler : ")
        for ability in self.Abilities:
            print(ability)
    