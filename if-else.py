a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")

#elif

num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")



#nested if-else

num=int(input("Enter a number: "));

if(num<0):
    print("Negative");
    
elif(num>0):
    if(num<=10):
        print("The number stay between 1-10");
    elif(num>10 and num<=20):
        print("The  number between 11-20");
    else:
        print("The number is greater than 20");
        
else:
    print("The number is zero");
         
