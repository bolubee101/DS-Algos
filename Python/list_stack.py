#create a class to implement stack functions
class Stack:
    #define a stack (list)
    def __init__(self):
        self.items = []
    
    #defining an empty stack
    def empty_stack(self):
        return self.items == []
    
    #to add an element to a stack
    def push(self,item):
        return self.items.append(item) 
    
    #to delete the first element from the list
    def pop_item(self):
        return self.items.pop()
    
    #to remove the top item from the list
    def peek_item(self):
        return self.items[len(self.items)-1]
    
    #to determine the size of the stack
    def size(self):
        return len(self.items)
'''
word = Stack()
word.push('x')
word.push('y')
word.pop_item()
word.push('z')
print(word.peek_item()) 
'''