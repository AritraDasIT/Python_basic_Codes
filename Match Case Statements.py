# Match Case Statements 
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# Syntax: match variable_name:
        #    case ‘pattern1’ : //statement1
        #    case ‘pattern2’ : //statement2
        #   …            
        #    case ‘pattern n’ : //statement n 
        
    
x=int(input("Enter a number: "));
 
match x:
    case 0 :
         print(x , " is zero");
    case 1:
         print(x, "is one");
         
    case _ if x!=90 :
        print(x, "is not 90");    # case with if-condition
    case _ if x!=80 :
        print(x , "is not 80");
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)