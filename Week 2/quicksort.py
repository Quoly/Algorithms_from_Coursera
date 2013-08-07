res = 0
def median(a, b, c):
	if b < a < c or c < a < b:
		return a
	if a < b < c or c < b < a:
		return b
	else:
		return c
 
def partition(lst):
	global res
	if len(lst) % 2 == 0:
		middle = len(lst) // 2 - 1
	else:
		middle = len(lst) // 2
	x = median(lst[0], lst[middle], lst[-1])
	ind = lst.index(x)
	lst[0], lst[ind] = lst[ind], lst[0]
	pivot = lst[0]
	k = 1
	for i in range(1, len(lst)):
		if lst[i] < pivot:
			lst[i], lst[k] = lst[k], lst[i]
			k += 1
		res += 1
	lst[k - 1], lst[0] = lst[0], lst[k - 1]
	return (lst[:k - 1], [pivot], lst[k:])

def quicksort(lst):
	if len(lst) < 2:
		return lst
	else:
		result = partition(lst)
		return quicksort(result[0]) + result[1] + quicksort(result[2])

file1 = "10.txt"
file2 = "100.txt"
file3 = "1000.txt"
file0 = 'QuickSort.txt'
l = open(file0,'r')
lis = l.readlines()
lst = [int(lis[i]) for i in range(len(lis))]
quicksort(lst)
print (res)
