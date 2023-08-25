#Recursion in python: Recursion is the process of defining something in terms of itself.

#Python Recursive Function:
#In Python, we know that a function can call other functions. It is even possible for the function to call #itself. These types of construct are termed as recursive functions.

def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num* factorial(num-1)
    
Factorial=factorial(5);
print(Factorial) 