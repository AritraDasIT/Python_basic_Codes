#Python Tuples: Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue","yellow")
print(tuple1)
print(tuple2)

print(type(tuple1))

#Tuple Indexes:

print(tuple1[0]);
print(tuple2[3]);
print(tuple2[-2]);

#Check for item:

if "Green" in tuple2:
    print("present")
else:
    print("absent");

#Range of Index:
#Syntax: Tuple[start : end : jumpIndex]

print(tuple1[0:5:2]);