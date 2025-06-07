class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
        print(f"The stack is:- {self.stack}")
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            Popped =  self.stack.pop()
            print(f"The  popped elements is:- {Popped}")
            print(f"The stack after popped is:- {self.stack}")
        
S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.pop()