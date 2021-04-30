# Essential Sorting Algorithms in Pyhton
import random


def quicksort(arr):
	_quicksort(arr, 0, len(arr) - 1)
	return arr


def _quicksort(arr, low, high):
	if low < high: 						# if low == high, we are done (1 element in array, so it's as sorted as it gets)
		p = partition(arr, low, high) 	# Put one element in right place; move other elements left or right of it based on size

# NOTE: The following line is the only difference between Lomuto and Hoare.
# Notice the left half quicksort is from low to p in Hoare.
		
		_quicksort(arr, low, p) 		# Sort left half, before the sorted element
		_quicksort(arr, p + 1, high)	# Sort right half, after the sorted element


def partition(arr, low, high):			# We already know low < high, so there's at least 2 elements in arr
	# Optional: Set pivot as median of three values, and swap to last position
	
	pivot = arr[low] 					# Pivot is lower part.
	i = low - 1							# Set left hand index to the first element
	j = high + 1						# Set right hand index to the last element.
	while True:
		
		# print('we out here piv%s lo%s hi%s' % (pivot, low, high))
		# print('arr[i] = %s; arr[j] = %s' % (arr[i],arr[j]))
		
		while True:						# If less than pivot AND on left (i) side, it's okay. No action needed.
			i += 1						# Slide past this element and check the next one, moving toward the middle
			if not (i < j and arr[i] < pivot): break
		
		while True:						# If greater than pivot AND on right (j) side, it's okay. No action needed.
			j -= 1						# Slide past this element and check the next one, moving toward the middle
			if not (i < j and arr[j] > pivot): break
		
		if i >= j:						# i >= j indicates that the two indexes have converged in the middle; we are done swapping
			return j					# j is the location where the pivot should be
		swap(arr, i, j)					# Otherwise, i and j point to two elements in the wrong half of the array. Swap them and both will be corrected.


def swap(arr, i, j):					# Swap indices i and j in arr
	# tmp = arr[i]						# Set i's value to tmp, to prevent overwriting it
	# arr[i] = arr[j]					# Swap j's value into i's place
	# arr[j] = tmp						# Swap i's value into j's place
	arr[i], arr[j] = arr[j], arr[i]
	return arr



if __name__ == "__main__":
	unsorted_list = random.sample(range(200), 50)
	print(unsorted_list)
	f_sorted = quicksort(unsorted_list)
	print(f_sorted)

	i = 0
	wall = 0
	pivot = len(unsorted_list)-1
	while i < pivot:
		sorted_list = quicksort(unsorted_list)
		if sorted_list[i] > sorted_list[pivot]:
			i += 1
		else:
			wall += 1  
		
		if sorted_list[wall] >= pivot:
			break
	
	print(sorted_list)
