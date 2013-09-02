import random

def rand_select(array, i):
	'''
	This function is looking for the i_th 
	smallest number in array
	'''
	if len(array) == 1:
		return array[0]
	(array, pivot_index) = partition(array)
	pivot = array[pivot_index]
	if pivot_index == i:
		return pivot
	elif pivot_index > i:
		return rand_select(array[:pivot_index], i)
	else:
		new_i = i - pivot_index - 1
		return rand_select(array[pivot_index + 1:], new_i)

def partition(array):
	'''
	This function partitions an array 
	depending on the pivot element. The pivot is chosen
	uniformly random.
	Everything less than pivot -> first subarray
	Everything more than pivot -> second subarray
	'''
	pivot_index = random.randint(0, len(array) - 1)
	array[0], array[pivot_index] = array[pivot_index], array[0]
	# Exchange first and randomly chosen element
	pivot = array[0]
	j = 1
	for i in range(1, len(array)):
		if array[i] < pivot:
			array[i], array[j] = array[j], array[i]
			j += 1
	array[j - 1], array[0] = array[0], array[j - 1]
	return (array, array.index(pivot))