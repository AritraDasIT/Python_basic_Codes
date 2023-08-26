# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

set1={1,2,3,4,5,4,2}

print(set1)
print(type(set1))

s= {}
print(type(s))         #it print <class 'dict'>  [it is a syntax of empty dictionary]

s1= set()
print(type(s1))        #it print <class 'set'>   [it is a syntax of empty set]

#Accessing set items:

#Using a For loop : You can access items of set using a for loop.

for value in set1:
    print(value)

#or

s3={'arira', False, 5 , 8 ,2.2, 5 , "red"}

for item in s3:
    print(item)           #IN python set does not maintain order