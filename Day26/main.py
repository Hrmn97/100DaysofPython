import time
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime



hour = int(time.strftime('%H'))
print(hour)

if(hour>0 and hour<12):
    print("Good morning sir")
elif(hour>12 and hour<17):
    print("Good after noon sir")
elif(hour>=17 and hour<0):
    print("Good night sir")


    