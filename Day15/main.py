'''Exercise 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
Your program should use time module to get the current hour. 
Here is a sample program and documentation link for you:'''


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minute = int(time.strftime('%M'))
print(minute)
seconds = int(time.strftime('%S'))
print(seconds)
# https://docs.python.org/3/library/time.html#time.strftime

if(hour < 23 and minute < 59 and seconds < 59 ):
    print('Good evening')
elif(hour < 11 and minute < 59 and seconds < 59):
    print("Good morning")
elif(hour < 15 and minute< 59 and seconds < 59):
    print("Good afternoon")
else:
    print("Invalid timezone")