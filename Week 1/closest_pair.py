def closest_pair(lst):
	pass

def two_dim_sort(lst, dim):
	if dim == 'x':
		array = [item[0] for item in lst]
		dct = dict(lst)
	else:
		array = [item[1] for item in lst]
		lst2 = [(item[1], item[0]) for item in lst]
		dct = dict(lst2)	
	sorted_array = merge_sort(array)
	res = []
	print(sorted_array, dct, array)
	for item in sorted_array:
		if dim == 'x':
			res.append((item, dct[item]))
			dct.pop(item)
		else:
			res.append((dct[item], item))
			dct.pop(item)
	return res



def merge_sort(array):
	if len(array) == 1:
		return array
	middle = len(array) // 2
	return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))

def merge(array1, array2):
	infinity = 10000000
	array1.append(infinity)
	array2.append(infinity)
	i1 = 0
	i2 = 0
	merged_array = []
	for k in range(len(array1) + len(array2) - 2):
		if array1[i1] < array2[i2]:
			merged_array.append(array1[i1])
			i1 += 1
		else:
			merged_array.append(array2[i2])
			i2 += 1
	return merged_array

lst = [(3, 4), (1, 6), (4, 2), (0, 0), (2, 9), (5, 1), (7, 6)]
print('x', two_dim_sort(lst, 'x'))
print('y', two_dim_sort(lst, 'y'))