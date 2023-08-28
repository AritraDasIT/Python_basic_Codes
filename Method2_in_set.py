#isdisjoint():
#The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

c1={2,7,12,4,25}
c2={5,8,78,2,58}
print(c1.isdisjoint(c2))      # return false

C1={'mrinal','ray','ghatak'}
C2={'raj', 'haranath','rabi'}
C3={'mrinal','ray','ghatak'}
print(C1.isdisjoint(C2))           #return true

#issuperset():
#The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

print(C1.issuperset(C2))     # return false
print(C1.issuperset(C3))     # return true

#issubset():
#The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

s={'Dev','jeet','Ankush'}
s1={'jissu','abir','param'}
s2={'Dev','abir','anirban'}
s3={'jeet','Ankush'}

print(s1.issubset(s))
print(s2.issubset(s))
print(s3.issubset(s))

#add():
# If you want to add a single item to the set use the add() method.

s1.add('sohom')
print(s1)

#update():
#If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

s1.update(s2);
print(s1)

#remove()/discard(): We can use remove() and discard() methods to remove items form list.

s1.remove('abir')
print(s1)

#pop():
#This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del:
#del is not a method, rather it is a keyword which deletes the set entirely.

del cities
print(cities)

#clear(): This method clears all items in the set and prints an empty set.

s3.clear()
print(s3)          #return empty set .... output : set()