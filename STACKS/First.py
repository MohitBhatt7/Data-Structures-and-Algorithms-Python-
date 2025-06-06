# This is the First program to implement stacks using python.
class stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item is: {item}")
        
    def pop(self):
        if self.is_empty():
            print(f"Stack underflow. Cannot pop the element from empty stack.")
            return None
        return self.stack.pop()
    
    
    def display(self):
        print(f"Stack from top to bottom are:- ", self.stack[::-1])
        

S = stack()
S.push(1)
S.push(2)            
S.push(3)            
S.push(4)            
S.push(5)
S.display()