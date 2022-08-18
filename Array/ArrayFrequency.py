'''This program calculates the frequency with which numbers 0 to n-1 occurs in an array of size n and provides a list of duplicates. It makes use of HASHMAP/HASHTABLE. A count array is generated to keep track of frequencies and original array is modified. Using a hasmap reduced time and space complexity to O(N).'''


def arr_freq (A, N):
	count_arr = [0 for i in range(N)]
	duplicate_arr = []
	for a in A:
		count_arr[a] += 1
	#print(count_arr)
	for a in A:
		index = a%N
		A[index] += N
	for i in range(N):
		if A[i]/N>2:
			duplicate_arr.append(i)
	#print(duplicate_arr)
	return count_arr,duplicate_arr

A = [2,3,1,2,3]
N = 5
c,d = arr_freq(A,N)
print("*******Frequency count of array*******")
for i in range(N):
	print("{} occurs {} times".format(i, c[i]))
print("\n\nElements having duplicates are: {}".format(d))



