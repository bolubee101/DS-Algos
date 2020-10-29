#implement a stack in Python
#FIFO: the first item entered into the list, is the first to get out of the list
#items are added at one end called 'rear'
#items are removed from one end called 'front'

class Queue:
    def __init__(self):
        self.items = []
    
    #an empty queue
    def empty_queue(self):
        return self.items == []
    
    #add an element to the stack
    def enqueue(self,item):
        return self.items.insert(0,item)
    
    #delete the last item in the list
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

new_list = Queue()
new_list.empty_queue()
new_list.enqueue('hello')
new_list.enqueue('dog')
new_list.enqueue(3)
print(new_list.dequeue())