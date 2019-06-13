from abc import ABC, abstractmethod                                     #for abstract method
class Ogre:
    def __init__(self, name, surname, power):                           # constructor
        self.name = name
        self.surname = surname
        self.power = power
    def makeThemFear(self):                                             # method
        print(f"I am {self.name} {self.surname} and this is my swamp!")
    def crush(self):
        print(f"Now, {self.name} {self.surname} crushed peasants!")
    def attack(self):
        print(f"{self.name} {self.surname} is attacking!")
        return self.power
    def died(self):
        print(f"{self.name} {self.surname} died!")
    def survived(self):
        print(f"{self.name} {self.surname} killed the invaders and ate them!")

class OgreChild(Ogre):
    pass
class OgreCooker(Ogre):
    def __init__(self, name, surname, power, cookHat):
        super().__init__(self, name, surname)                             # constructor inheritence
        self.cookHat = cookHat
    def makeThemFear(self):
        super().makeThemFear()
        print("When I will finish you I will make soup from your bones!!! Grahr!!!")

class Orc(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod                                # there is forcing use of method in other classses
    def work(self):
        pass
 
class Peon(Ogre):                                  #It should be orc not ogre to be honest...
#class Peon(Orc):    
    def makeThemFear(self):                        # Methods without super inheritence
        print("Ready to work.")
    def attack(self):
        print("I'll try...")                       #and more texts from Warcraft 3... ^^
#    def work(self):
#        print("Work Work!")

class Peasant:
    groupOfPeasants = 0                            # static field
    peasantsDying = True                           # static field
    def __init__(self):                            # constructor
        Peasant.groupOfPeasants += 1               # reference to static field
        print(f"{self.groupOfPeasants} are ready to fight!")
    def __del__(self):                             # destructor
        if Peasant.peasantsDying:
            Peasant.groupOfPeasants -= 1
            print(f"{self.groupOfPeasants} still alive.")
        else:
            print(f"{self.groupOfPeasants} survived battle!")
    
    @staticmethod                                   #static method
    def tryToKillOgre():
        if Peasant.groupOfPeasants > 5:
            Peasant.peasantsDying = False
            return True
        elif Peasant.groupOfPeasants > 0:
            Peasant.peasantsDying = False
            print(f"{Peasant.groupOfPeasants} run away!")        
            return False
        else:
            return False

class Encapsulation:
    def __init__(self):
        self.public, self._protected, self.__private = 1, 2, 3

def main():
    print(f"Now it is time to fight against devil, group of peasants arrived to ogre`s swamp...")
    print(f"Ogre leaft his cave!")
    angryOgre = Ogre("Skull","Crusher", 5)
    angryOgre.makeThemFear()
    print(f"Oh no, lots of peasants run in fear! How many peasants still reamined?")
    amountofBravePeasants = int(input())
    peasants = []
    while amountofBravePeasants > 0:
        peasants.append(Peasant())
        amountofBravePeasants -= 1
    peasantsDied = angryOgre.attack()
    angryOgre.crush()

    if peasants.__len__() < peasantsDied:
        peasantsDied = peasants.__len__()
    for x in range(peasantsDied):
        peasants[x] = None

    if Peasant.tryToKillOgre():
        angryOgre.died()
    else:
        angryOgre.survived()
    #orc = Orc("Orc")
    #peon = Peon("Simple","Orc", 0)
    #peon = Peon("Simple Orc")
    ogreChild = OgreChild("Ogre","Child",0)
    print(isinstance(angryOgre, OgreChild))
    print(isinstance(angryOgre, Ogre))
    print(isinstance(ogreChild, OgreChild))
    print(isinstance(ogreChild, Ogre))
if __name__ == "__main__":
    main()
