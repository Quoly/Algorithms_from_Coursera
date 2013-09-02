def merge_inverse_sort(array):
	if len(array) == 1:
		return array
	middle = len(array) // 2
	return merge_inverse(merge_inverse_sort(array[:middle]), merge_inverse_sort(array[middle:]))

def merge_inverse(array1, array2):
	infinity = 10000000
	array1.append(infinity)
	array2.append(infinity)
	i1 = 0
	i2 = 0
	merged_array = []
	for k in range(len(array1) + len(array2) - 2):
		if array1[i1] > array2[i2] and array1[i1] != infinity or array2[i2] == infinity:
			merged_array.append(array1[i1])
			i1 += 1
		else:
			merged_array.append(array2[i2])
			i2 += 1
	return merged_array

def min_weight_sum(lst):
	weights = [int(lst[i][0]) for i in range(len(lst))]
	lengths = [int(lst[i][1]) for i in range(len(lst))]
	diffs = {}
	for i in range(len(lst)):
		difference = int(lst[i][0]) / int(lst[i][1])
		diffs[difference] = diffs.get(difference, []) + [i]
	for key in diffs.keys():
		diffs[key] = merge_inverse_sort(diffs[key])
	diffs_list = list(diffs)
	sorted_diffs_list = merge_inverse_sort(diffs_list)
	length = 0
	result = 0
	for item in sorted_diffs_list:
		curr_weights = []
		curr_lengths = []
		for i in diffs[item]:
			curr_weights.append(weights[i])
			curr_lengths.append(lengths[i])
		curr_weights_sorted = merge_inverse_sort(curr_weights)
		for i in curr_weights_sorted:
			ind = curr_weights.index(i)
			length += curr_lengths[ind]
			result += curr_weights[ind] * length
	return result


if __name__ == '__main__':
	f = open('jobs.txt')
	lst = [item.split() for item in f.readlines()]
	test1 = [[1, 1], [1, 3], [2, 2]]
	test2 = [[30, 90], [10, 30], [20, 40], [30, 50], [20, 60], [10, 50]]
	to_count = lst
	print(min_weight_sum(to_count))