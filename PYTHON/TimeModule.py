#Greetings to sir according to time .

import time
timenow=time.strftime('%H:%M:%S')
print(timenow)
if(timenow<time.strftime('12:00:00') and timenow>time.strftime('00:00:00')):
    print("Good Morning sir")
elif(timenow>time.strftime('12:00:00') and timenow<time.strftime('18:00:00')):
    print("Good Afternoon sir")
elif(timenow>time.strftime('18:00:00') and timenow<time.strftime('23:59:59')):
    print("Good Evening sir")
else:
    print("No salutation")



# timenow=int(time.strftime('%H'))
# print(timenow)
# timenow=time.strftime('%M')
# print(timenow)
# timenow=time.strftime('%S')
# print(timenow)

# import time
# print(time.time())
# # Output: 1602299933.233374

import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33