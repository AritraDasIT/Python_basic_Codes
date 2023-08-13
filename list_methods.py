list= [25, 7 , 12 ,19, 98, 11];

print(list);

#list.sort(): This method sorts the list in ascending order. The original list is updated

list.sort();
print(list);

list.sort(reverse=True);  #sort in decending order
print(list);

#reverse(): This method reverses the order of the list.

list1=[1,2,3,4,5,6,7]

list1.reverse()
print(list1)


# copy():Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

list2 = list1.copy();
print(list2)

#append(): This method appends items to the end of the existing list.

list2.append("Aritra")
list2.append(4);
print(list2);

#insert():
#This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

#extend(): This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

color1= ['yellow' , 'black', 'pink'];

colors.extend(color1);
print(colors)

# Concatenating two lists: You can simply concatenate two lists to join two lists.

print(colors+color1);

#count(): Returns the count of the number of items with the given value.

print(colors.count("black"))

#index(): This method returns the index of the first occurrence of the list item.

names= ['aritra', 'raya', 'arup', 'som'];

print(names.index('raya'))
print(names.index('arup'))
print(names.index('aritra'))
print(names.index('som'))



