# def apply(fx,value):
#     return 10+fx(value)
cube=lambda x:x**2
# print(apply(cube,2))

print(cube(3))


def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x*x , 2))