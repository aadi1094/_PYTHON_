#MAP:
def cube(x):
    return x*x*x

l= [1,2,3,4,5,6,7,8,9]
newl=list(map(cube,l))
print(newl)

#Filter:
newl2=list(filter(lambda a:a>4,l))
print(newl2)

#Reduce:
from functools import reduce

newl3=reduce(lambda x,y:x+y ,l)
print(newl3)