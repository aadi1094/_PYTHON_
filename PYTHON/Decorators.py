# def greet(fx):
#     def mfx():
#         print("Good morning")
#         fx()
#         print("Byee")
#     return mfx

# @greet


def greets(fx):
    print("good morning")
    return fx
def hello():
    print("Hello World")

greets(hello)()