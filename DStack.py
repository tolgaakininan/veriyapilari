import collections
class Stack:
    def __init__(self) -> None:
        self.container=collections.deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
def reverseString(string):
    stack=Stack()
    for ch in string:
        stack.push(ch)
    reversedString=''
    while stack.isEmpty is False:
        reversedString+=stack.pop()
    return reversedString
if __name__=='__main__':
   print(reverseString("Racecar issi racecar"))


   
