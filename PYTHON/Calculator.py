#Calculator..
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y!=0:
        return x/y
    else :
        return "Error .! Division by zero"

def main():
    print("Welcome to the Calculator")
    num1=float(input("Enter the 1st number: "))
    num2=float(input("Enter the 2nd number: "))

    print("Select Operators")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")

    choice=input("Enter the choice 1/2/3/4 : ")

    if choice=='1':
        print(f"The result of {num1} + {num2} is: {add(num1,num2)}")
    elif choice=='2':
        print(f"The result of {num1} - {num2} is: {substract(num1,num2)}")
    elif choice=='3':
        print(f"The result of {num1} * {num2} is: {multiplication(num1,num2)}")
    elif choice=='4':
        print(f"The result of {num1} / {num2} is: {division(num1,num2)}")
    else:
        print("Invalid input")

    while True:
        cont=input("You want to perform another Calulation ?(Yes or No)").strip().lower()
        if cont=="yes":
            main()
        elif cont=="no":
            print("Exiting the calculation..Goodbyee..")
            break
        else:
            ("Please enter \"Yes/No\"")
if __name__=="__main__":
    main()