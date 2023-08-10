# Function Arguments and return statement

#Default arguments:
#We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy");

def avarage(a=10,b=16):
    
    print("The avarage is :" , ((a+b)/2));
     
avarage();     #output: The avarage is : 13.0
avarage(2);    #output: The avarage is : 9.0
avarage(6,8);  #output: The avarage is : 7.0
avarage(b=12);  #output: The avarage is: 11.0

#Keyword arguments:
#We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

#Required arguments:
#In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

def avg(a,b,c):
    print((a+b+c)/2);
    
avg(1,2,3);
# avg(1,2) shows error



#Variable-length arguments:
#Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
#There are two ways to achieve this:

#1) Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

def avag(*numbers):
    sum=0;
    
    for i in numbers:
        sum=sum+i;
        
    print("Average is : ", (sum/len(numbers)));

avag(4,8)
avag(5,15,25,65)

#2)Keyword Arbitrary Arguments:
  #While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.


def name(**name):
    
    print("Hello,", name["fname"], name["mname"], name["lname"])
    print(type(name))
       
      

name(mname = "Buchanan", lname = "Barnes", fname = "James")     
















