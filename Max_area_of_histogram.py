#Using Class and Objects

arr = [6,2,5,4,5,1,6]

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, num):
        return self.stack.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
def nextsmallertoright(arr):
    stack = Stack()
    result = []
    for i in range(len(arr) - 1, -1, -1):
        if stack.isEmpty():
            result.append(-1)
            stack.push(arr[i])
        elif not stack.isEmpty():
            while (not stack.isEmpty() and arr[i] < stack.peek()):
                stack.pop()
            if stack.isEmpty():
                result.append(-1)
            else:
                result.append(arr.index(stack.peek()))
        stack.push(arr[i])
    result.reverse()
    return result
def nextsmallertoleft(arr):
    stack = Stack()
    result = []
    for i in range(len(arr)):
        if stack.isEmpty():
            result.append(-1)
            stack.push(arr[i])
        elif not stack.isEmpty():
            while (not stack.isEmpty() and arr[i]<stack.peek()):
                stack.pop()
            if stack.isEmpty():
                result.append(-1)
            else:
                result.append(arr.index(stack.peek()))
            stack.push(arr[i])

    return result
Result = nextsmallertoleft(arr)
Result1 = nextsmallertoright(arr)

width = []
for (i,j) in zip(Result,Result1):
    width.append((j-i)-1)
maxarray = []
for i in range(len(width)):
    maxarray.append(arr[i]*width[i])
print(max(maxarray))
