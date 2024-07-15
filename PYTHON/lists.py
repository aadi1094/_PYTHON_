# lst1 = [1,2,2,3,5,4,6]
# lst2 = ["Red", "Green", "Blue"]
# print(lst1)
# print(lst2)

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]  #Positive index
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]   #Negative index
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Orange" in colors:
#     print("Orange is present.")
# else:
#     print("Orange is absent.")

#Range of index:
# n=[3,4,5,6,7,8,9,10]
# print(n[3:7])
# print(n[-7:-2])

#Printing alternative:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes