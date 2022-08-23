
'''LC - 1480 - Running sum of 1D Array
Remember, using ele in for loop does not change the array. 
Whereas using index, changes the array'''

A = [1,2,3,4]
for ele in A:
	ele = ele + 1
print (A)
#In above for loop, input array does not change. 
i = 1
while i < len(A):
	A[i] += 1
	i += 1
print(A)
#In above for loop, input array changes. 

#------------------------------LC1418--------------------
def runningSum(A):
	i = 1
	while (i<len(A)):
		A[i] += A[i-1]
		i += 1
	return A

a = [3,5,7,3,0, -1, -55]
print("The running sum of the 1D array is:", runningSum(a))
