arr = [6, 2, 5, 4, 5, 1, 6]
#Nearest Smaller to left


stack = [] 
width = [] 

## Left traversal
for i in range(len(arr)): 
  if(len(stack) == 0):
    width.append(-1)
  elif(len(stack) != 0):
    while(len(stack)!= 0 and arr[i] < top(stack)):
      stack.pop()
    if(len(stack) == 0):
      width.append(-1)
    else:
      width.append(arr.index(top(stack)))
  stack.append(arr[i])

ustack = []
height = []
arr = [6, 2, 5, 4, 5, 1, 6]
#Nearest Smaller to left
#Right traversal
for i in range(len(arr)-1, -1, -1):
  if(len(ustack) == 0):
    height.append(len(arr))
    ustack.append(arr[i])
  elif(len(ustack) != 0):
    while(len(ustack) != 0 and arr[i] < top(ustack)):
      ustack.pop()
    if(len(ustack) == 0):
      height.append(len(arr))
    else:
      height.append(arr.index(top(ustack)))
  ustack.append(arr[i])
height.reverse()

#print(width)
#print(height)

sumation = []
for (i,j) in zip(width, height):
    sumation.append((j-i)-1)
#print(sumation)

maxarray = []
for i in range(len(width)):
    maxarray.append(arr[i]*sumation[i])
print(max(maxarray))
