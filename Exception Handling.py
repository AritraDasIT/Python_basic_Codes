#Exception Handling
#Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals
#with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

#syntax:
# try:
     #statements which could generate 
     #exception
# except:
     #Soloution of generated exception

n=input("Enter a number: ")

print(f"Multiplication table of {n} is = ")

try:
    for i in range (1,11):
        print(f"{int(n)}x{i}=h{int(n)*i}")
except:
    print("Invalid")

