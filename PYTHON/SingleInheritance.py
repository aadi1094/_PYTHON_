class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species 

    def make_sound(self):
        print("animal sound")

class Dog(Animal):
    def __init__(self,name,breed) -> None:
        Animal.__init__(self,name,species="dog")
        self.breed=breed

    def make_sound(self):
        print("barkk")

a=Animal("Tiger","Tiger")
a.make_sound()

d=Dog("LabraDog","Dogerman")
d.make_sound()