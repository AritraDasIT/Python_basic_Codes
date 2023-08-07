# find(): The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

str1= 'i am the best actor in the world';
STR2= 'iamthebestactorintheworld';
print(str1.find("the"));
print(str1.find("raya"));


# index() : The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

print(str1.index("best"));
# print(str1.index("raya"));  shows error

#isalnum() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

print(str1.isalnum());   #space also not allowed
print(STR2.isalnum());

#The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str3= 'myrollis15';      

print(str3.isalpha());

# isspace() : The isspace() method returns True only and only if the string contains white spaces, else returns False.

print(str3.isspace());
str4="  ";
print(str4.isspace());

# istitle() : The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str5= " I Am Aritra ";
print(str5.istitle());

# isupper() : The isupper() method returns True if all the characters in the string are upper case, else it returns False.

str6= 'HEY BOYS';
print(str6.isupper());

#startswith() : The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

print(str6.startswith("HEY"));

# swapcase() : The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

print(str5.swapcase());

# title() : The title() method capitalizes each letter of the word within the string.

print(str1.title());