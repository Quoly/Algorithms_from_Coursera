# Choosing first element as pivot
 
def partition(lst):
	global res
	length = len(lst)
	pivot = lst[0]
	k = 1
	for i in range(1, length):
		if lst[i] < pivot:
			lst[i], lst[k] = lst[k], lst[i]
			k += 1
	res += length - 1
	lst[k - 1], lst[0] = lst[0], lst[k - 1]
	return (lst[:k - 1], [pivot], lst[k:])

def quicksort(lst):
	if len(lst) < 2:
		return lst
	else:
		result = partition(lst)
		return quicksort(result[0]) + result[1] + quicksort(result[2])

res = 0
file_name = 'QuickSort.txt' 
f = open(file_name)
file_list = f.readlines()
lst_to_sort = [int(file_list[i]) for i in range(len(file_list))]
quicksort(lst_to_sort)
print(res)
