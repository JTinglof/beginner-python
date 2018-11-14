import sys
from StackMachine import StackMachine               #Inports custom StackMachine class

print("Assignment #4-1, Joseph Tinglof, jbtinglof@gmail.com")
theThing = StackMachine()                           #Creates StackMachine object

file_name = sys.argv[1]                             #Stores name of text file to be used
tokenedList = []                                    #Creates list for the tokenized commands
for x in open(file_name).readlines():               #Tokenizes the contents of the text file
    if len(x.split()) > 0:
        tokenedList.append(x.split())

for line in tokenedList:                           #Checks each token for proper syntax, if correct
    if line[0] == "push" and line[1].isdigit():    #the appropriate command is carried out
        theThing.push(int(line[1]))
    elif line[0] == "pop":
        print(theThing.pop())
    elif line[0] == "add":
        theThing.add()
    elif line[0] == "sub":
        theThing.sub()
    elif line[0] == "mul":
        theThing.mul()
    elif line[0] == "div":
        theThing.div()
    elif line[0] == "mod":
        theThing.mod()
    else: 
        print("Your input was ignored.")

