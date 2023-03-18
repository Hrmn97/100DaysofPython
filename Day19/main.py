# break statement
# The break statement enables a program to skip over a part of the code.
#  A break statement terminates the very loop it lies within.


for i in range(1,100, 5):
    print("5 X ", i,  " = ", 5*i )
    if( i == 16):
        break

i=0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break

# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.


for i in [2,3,4,6,8,0]:
    if ( i%2 != 0):
        continue
    print(i)