# For loop

Namne= 'Aritraya';

for i in Namne:        #for string
    print(i);
    
colors=['red', 'green', 'blue','yellow','pink'];

for r in colors:      #for list
    print(r);
    
    for color in r :
        print(color);
        
# range():
#What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
#Here, we can use the range() function.

for k in range(0,10):
     print(k);
     
for s in range (200):
    print(s);
    
for b in range (1, 20 , 2):
    print(b);