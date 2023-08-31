#These 3 lines ask the user to enter someting. The specifc info is asked tbrough adding (). Var stores info to be used later
age = input ("How old are you? ")
height = input ("How tall are you? ")
weight = input ("How much do you weigh? ")

#This is an F string and formats all the inputs defined from previous Var onto a single line allowing them to print as an output
print (f"So, you're {age} old, {height} tall and {weight} heavy.")