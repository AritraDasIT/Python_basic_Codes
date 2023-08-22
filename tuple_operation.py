# Manipulating Tuples:

tup1=(2,25,7,8,11,22,23)
print(type(tup1));

temp= list(tup1);         # tuple to list 
print(type(temp));
temp.append(100);
print(temp);
temp.pop(5);
print(temp);

#concatinate:
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count() Method: The count() method of Tuple returns the number of times the given element appears in the tuple.
#syntax: tuple.count(element)

tup2=(2,4,6,12,2,6,7,8,9,2,6,12,12,2)
print(tup2.count(12))
print(tup2.count(2))

#index() method: The Index() method returns the first occurrence of the given element from the tuple.
#Syntax: tuple.index(element, start, end)

print(tup2.index(6))
print(tup2.index(8))
print(tup2.index(6,8,12)) #tuple sclice between 8 and 12


