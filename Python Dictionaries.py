#Python Dictionaries:
#Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

info={
    'Name': 'Aritra' ,
    'roll': 10,
    'class': 8,
    'age': 15,
    # key: value
}

print(info)           
print(info['age'])       #access particular key value

print(info.values())     #access values
print(info.keys())       #access keys

print(info.items())    #Accessing key-value pairs


#update()
#The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

#SYNTAX: dictionary_name.update({'key':value})

info.update({'age':23})
print(info['age'])

#Removing items from dictionary- 
# 1) clear():The clear() method removes all the items from the list.

#SYNTAX: dictionary_name.clear()

info.clear()
print(info)

#2) pop(): The pop() method removes the key-value pair whose key is passed as a parameter.

#SYNTAX: dictionary_name.pop('key')

info1 = {'name':'Karan', 'age':19, 'eligible':True , 'roll':50}
info1.pop('eligible')
print(info1)

#3) popitem():The popitem() method removes the last key-value pair from the dictionary.

##SYNTAX: dictionary_name.popitem()

info1.popitem()

print(info1)

#4)del()
# i) : we can also use the del keyword to remove a dictionary item.

#SYNTAX: del.dictionary_name['key']

info3 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info3['age']
print(info3)

# ii) If key is not provided, then the del keyword will delete the dictionary entirely.

#del.info3
#print(info3)  output: NameError: name 'info' is not defined











