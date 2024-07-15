class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

a=Employee("adi",1243)
b=Programmer("Adiiii",233,"python")
print(b.name)
print(a.name)
print(b.id)
print(a.id)
print(b.lang)