class person:
    name="Aditya"
    age=19
    occupation="Software Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
a.info()

c=person()
c.name="Mayank"
c.occupation="Hardworking boy"
c.info()