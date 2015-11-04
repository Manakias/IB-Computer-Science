class Pet:
    #function that constructs an object VVVV
    def __init__(self,petname,petspecies):
        self.name=petname
        self.species=petspecies

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species
#speak is a null method - just does something
    def speak(self):
        if self.species=="Dog":
            print "Woof!"
        else:
            if self.species=="Cat":
                print "Meow!~"
            else:
                print "Insert animal sound here"
    def intro(self,pet):
        print "Hello "+pet.getName()+" I am a "+self.species+" named "+self.name
        
p1=Pet("Ruff", "Dog")
p2=Pet("Kara", "Cat")
#print p1.getName()+" is a "+p1.getSpecies()
#print p1
#p1 is an instance of the Pet class
#we say p1 is an object
#the first O in OOP
p1.intro(p2)
p2.speak()
