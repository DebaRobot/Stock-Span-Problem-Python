## Maximum area of Rectangle in Binary Matrix
def max_area_histogram(histogram):
	stack = list()
	max_area = 0 
	index = 0
	while index < len(histogram):
		if (not stack) or (histogram[stack[-1]] <= histogram[index]):
			stack.append(index)
			index += 1
		else:
			# pop the top
			top_of_stack = stack.pop()
			area = (histogram[top_of_stack] *
				((index - stack[-1] - 1)
				if stack else index))
			max_area = max(max_area, area)
	while stack:
		top_of_stack = stack.pop()
		area = (histogram[top_of_stack] *((index - stack[-1] - 1) if stack else index))
		max_area = max(max_area, area)
	return max_area
-----------------------------------------------------------------------

arr = [[0,1,1,0], [1,1,1,1], [1,1,1,1], [1, 1, 0 , 0]]
li = []

for i in range(len(arr[0])) :
  li.append(arr[0][i]) 
maxnum =  max_area_histogram(li) #2

for i in range(1,len(arr)): #2
  li1 = []
  for j in range(0, len(arr)):
    if(arr[i][j] == 0):
      li1.append(0)
    else:
      arr[i][j] = arr[i][j] + arr[i-1][j] ## arr[1][0] + arr[0][0] ##arr[2][1] + arr[1][1]
      li1.append(arr[i][j])
    maxnum = max(maxnum, max_area_histogram(li1))
print(maxnum)
----------------------------------------------------------------------------------
