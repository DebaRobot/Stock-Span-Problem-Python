Approach 1 :
 
stack = []
result = []
count  = 1
k = 1
arr = [100, 80, 60 , 70, 60, 75, 85]

for i in range(len(arr)):
  if(len(stack) == 0):
    result.append(count)
    stack.append(arr[i])
    print(stack)
  
    
  elif(len(stack) != 0):
    while(len(stack) != 0 and arr[i] > stack[len(stack)-k]):
      count = count + 1      
      k = k + 1
    result.append(count)
    count = 1
    k = 1
    stack.append(arr[i])
----------------------------------------------------------------------------------------------------------------------------

Approach 2

def top(stack):
  return stack[-1]

arr = [100, 80, 60,70, 60, 75, 85] #75
stack =[] 
k = 1
result = [] #-1 0 1 1 3 2
for i in range(len(arr)):
  if(len(stack) == 0):
    result.append(-1)
  elif (len(stack) != 0):
    while(len(stack) != 0 and arr[i] > top(stack)):
      stack.pop()
      k = k + 1 
      
    if(len(stack) == 0):
      result.append(-1)
    else:
      result.append(arr.index(top(stack)))
  stack.append(arr[i])
  k = 1
  
print(result)
update = []
for i in range(len(result)):
  update.append(i - result[i])
print(update)

------------------------------------------------------------------------------------------------------------------
