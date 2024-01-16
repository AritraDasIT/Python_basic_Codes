
#Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop.
#The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

#1
for i in range (5):
    print(i)

else:
    print("sorry no i ")

#2
    
for i in  []:
    print(i)

else:
    print("sorry no i ")

#3

for i in range (6):
    print(i)

    if (i==4):
        break

else:
    print("sorry no i ")
