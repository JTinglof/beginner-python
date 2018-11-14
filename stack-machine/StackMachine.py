class StackMachine(object):
    def __init__(self):                 #Constructor for the class
        self.theStack = []
    def push(self,newItem):             #Adds a new value to the top of the stack
        self.theStack.append(newItem) 
    def pop(self):                      #Removes and returns the top value on the stack 
        return self.theStack.pop()      
    def add(self):                      #Pops two values, adds them, pushes them to the stack
        num1 = self.pop()
        num2 = self.pop()
        newnum = num1 + num2
        self.push(newnum)
    def sub(self):                      #Pops two values, subtracts them, pushes the result to the stack
        num1 = self.pop()
        num2 = self.pop()
        newnum = num1 - num2
        self.push(newnum)
    def mul(self):                      #Pops two values, multiplies them, pushes result to the stack
        num1 = self.pop()
        num2 = self.pop()
        newnum = num1 * num2
        self.push(newnum)
    def div(self):                      #Pops two values, divides them, pushes result to the stack
        num1 = self.pop()
        num2 = self.pop()
        newnum = num1 / num2
        self.push(newnum)
    def mod(self):                      #Pops two values, does the % thing to them, pushes result to the stack
        num1 = self.pop()
        num2 = self.pop()
        newnum = num1 % num2
        self.push(newnum)
