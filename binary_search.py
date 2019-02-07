def binary_search(list, item):
	#low and high keep track of which part of the list you're searching in
	low = 0
	high = len(list)-1

	while low <= high: #while you haven't narrowed the search to one element...
		mid = (low + high) #check the middle element
		guess = list[mid]
		if guess == item: #Found the item
			return mid
		if guess > item: #If the guess is too high
			high = mid -1
		else: #if the guess is too low
			low = mid + 1 
	return None #If the item doesn't exist

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 25, 29, 31, 37, 43, 47, 51, 52, 53, 54, 57, 58, 61]

print(binary_search(my_list, 13))
print(binary_search(my_list, 7))
print(binary_search(my_list, 58))