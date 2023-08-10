#LIST:
#Lists are ordered collection of data items.
#They store multiple items in a single variable.
#List items are separated by commas and enclosed within square brackets [].
#Lists are changeable meaning we can alter them after creation.

lst1=[1, 200 , True , 'Aritra' , 22.5 ];

print(lst1)
print(type(lst1));

#List Index:

print(lst1[0]);
print(lst1[1]);
print(lst1[2]);
print(lst1[3]);
print(lst1[4]);

print(lst1[-3]);     # eqivalent to print(lst1[len(lst1)-3]);

if 'Aritra' in lst1 :
    print("Yes")

else:
    print("NO");

# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
# Syntax : listName[start : end : jumpIndex]

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
print(animals[1:9:3])

#List Comprehension
#List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

#Syntax: List = [Expression(item) for item in iterable if Condition]

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

namesWith_O = [item for item in names if "o" in item]

print(namesWith_O)