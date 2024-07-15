#Default aarguments :
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Adi")

#Keyword arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
#Required arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

# Variable-length arguments:
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")