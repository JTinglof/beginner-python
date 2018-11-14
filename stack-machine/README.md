## Synopsis
In this assignment we learned about python by creating a stack machine that 
could read instructions from a text file.

## Files Used
prog4_1.py is a program that, when given a text file through the command line,
can tokenize the contents by whitespace and return them separated by a ",".

StackMachine.py is a class that creates a StackMachine like data structure with 
methods for pushing and popping the stack as well as math functions that will add
or subtract the two top values on the stack.

prog4_2.py reads a text file like prog4_1 but will then check the contents for 
StackMachine commands. If it finds any it will create a StackMachine object and 
populate it acccording to the instructions on the text file.
