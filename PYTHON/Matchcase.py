x = int(input("Enter the value: "))
# x is the variable to match
match x:
    # # if x is 0
    # case 0:
    #     print("x is zero")
    # # case with if-condition
    # case _ if x % 2 == 0:
    #     print("x % 2 == 0 and case is 4")
    # # Empty case with if-condition
    # case _ if x < 10:
    #     print("x is < 10")
    # # default case(will only be matched if the above cases were not matched)
    # # so it is basically just an else:
    # case _:
    #     print(x)
    case 0:
        print("x is zero")
    case 1 if x%2==0:
        print("x is module")
    case 2 if x%3==0:
        print("x%3==0")
    case _ if(x>2):
        print("nothing")