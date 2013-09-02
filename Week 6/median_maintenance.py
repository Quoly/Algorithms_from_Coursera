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

def ins(sorted_list, item):
	ind = len(sorted_list)
	while ind:
		if

res = 0
file_name = 'Median.txt' 
f = open(file_name)
file_list = f.readlines()
lst_to_sort = [int(file_list[i]) for i in range(len(file_list))]
test1 = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
test2 = [3, 7, 4, 1, 2, 6, 5]
t = lst_to_sort
result = 0
for i in range(1, len(t) + 1):
	lst = quicksort(t[:i])
	#print(lst)
	length = len(lst)
	result += lst[length // 2 - 1 + length % 2]
	#print(lst[length // 2 - 1 + length % 2])
print(result % 10000)
