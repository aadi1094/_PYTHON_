class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The employee id {self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("Heyy My language is python")


e1=Employee("Aditya",400)
e1.showdetails()
e2=Programmer("Pratu",420)
e2.showlanguage()
e2.showdetails()