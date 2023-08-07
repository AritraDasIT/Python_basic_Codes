# STRING METHODS

#STRINGS ARE IMMUTABLE

#upper() method       [ Change a string into a uppercase letters]

Name="Aritra";
print(Name);
print(Name.upper());

#lower() method       [ Change a string into a lowercase letters]

name="RAYA";
print(name);
print(name.lower());

#rstrip() method             [Eleminate the spacial character afer string ]

NAME= "***ARITRA***";    
print(NAME.rstrip("*"));

#replace() method          [Replace a String with other string]

print(NAME.replace("ARITRA","Arup"));



# split() method  [Split a string into a list where each word is a list item]

Name = "I am Aritra Das";

print(Name.split(" "));   # output : ['I', 'am', 'Aritra', 'Das']

# capitalize() Method [Upper case the first letter and the rest is lower case in this sentence]

Heading = 'this is My 1st code';

print(Heading.capitalize());

#The center() method will center align the string, using a specified character (space is default) as the fill character

print(Name.center(20,"."));

#count() : The count() method returns the number of times the given value has occurred within the given string.

str1= 'hei bibek , bibek is mad , love u bibek ***';

print(str1.count("bibek"));

# endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

print(str1.endswith("**"));





