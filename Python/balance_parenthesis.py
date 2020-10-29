#we check if the open parenthesis has a matching close parenthesis
from list_stack import Stack

def brackets(symbol):
    stack = Stack()
    balance = True
    index = 0
    while index < len(symbol) and balance:
        text = symbol[index]
        #if the text is (, add it to the stack, else delete from the stack
        if text in "({[":
            stack.push(text)
        else:
            if stack.empty_stack():
                balance = False
            else:
                stack.pop_item()
        index = index + 1
#if the stack is empty after the loop runs, it contains matching number of parenthesis
    if balance and stack.empty_stack():
        return True
    #else the parenthesis aren't complete in pairs
    else:
        return False
print(brackets("((()))"))
print(brackets("((()"))
print(brackets("[[]]"))

