def merge_sort(array):
	if len(array) == 1:
		return array
	middle = len(array) // 2
	return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))

def merge(array1, array2):
	global inversions
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
			inversions += len(array1[i1:-1])
	return merged_array

def main():
	f = open('IntegerArray.txt')
	lst = [int(char) for char in f.readlines()]
	merge_sort(lst)
	print(inversions)

if __name__ == '__main__':
	inversions = 0
	main()

