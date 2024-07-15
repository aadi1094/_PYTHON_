#StringFormatting

#f-Strings:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
name="Aditya"
country="India"
print(f"Hi, My name is {name} and I am from {country}")

#DocStrings:
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)
