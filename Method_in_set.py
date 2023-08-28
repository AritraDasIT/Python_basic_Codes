# union() and update() :

#The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

color1= {'red','green','blue','yellow','black'}
color2= {'pink','white','red','violate'}

print(color1.union(color2))         #The union() method returns a new set

color1.update(color2);              #update() method adds item into the existing set from another set.
print(color1)

#  intersection and intersection_update():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)          #The intersection() method returns a new set 
print(cities3)            

cities.intersection_update(cities2)        #intersection_update() method updates into the existing set from another set
print(cities)


#symmetric_difference and symmetric_difference_update():

s1={2,3,4,5,6}
s2={5,6,7,8,9}

s3=s1.symmetric_difference(s2)
print(s3)

#difference() and difference_update():
#The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

n1={2,3,4,1,10}
n2={6,2,5,4,25}

n3=n1.difference(n2)
print(n3)

#Check if item exists
# You can also check if an item exists in the set or not.

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")