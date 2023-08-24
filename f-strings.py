# String formatting in python / f-strings in python :

#exm1:
name="Aritra";
country="INDIA"
txt= (f"my name is {name} and i am form {country}");
print(txt)

#exm2:

txt1= "For only {price:.2f} dollars!"
print(txt1.format(price = 49.00201))

#exm3:

print(f"{20*5}");
print(type(f"{20*5}"));