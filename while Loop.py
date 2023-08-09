# Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

#example1

i=0;
while(i<=3):
    print(i);
    i=i+1;
    
#example2
    
k= int(input('Enter the value of k :  '));
while(k<=50):
    k= int(input('Enter the value of k :  '));
    print(k);
    k=k+1;

#example3
count=10;
while (count>0):
    print(count);
    count=count-1;
else:
    print("I am in else");
    