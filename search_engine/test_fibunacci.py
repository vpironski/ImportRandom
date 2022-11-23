def fibunacciSearch(array,x,size):
	# start of algorithm
	offset = -1
	# first 3 nums of sequences
	fn0 = 0 
	fn1 = 1 
	fn = fn0 + fn1

	while (fn<len(array)):
		# creating the sequences while we are in the array
		fn0 = fn1
		fn1 = fn
		fn = fn0 + fn1

	while(fn > 1):
		index = min(offset + fn0, size-1)
		# If x > index fn
		# cut array from offset to i
		if array[index] < x:
			fn = fn1
			fn1 = fn0
			fn0 = fn - fn1
			offset = index
		# If x < index fn
		# cut array after index+1
		elif array[index] > x:
			fn = fn0
			# fn1 = fn0
			fn1 = fn1-fn0
			fn0 = fn - fn1
		else:
			# It found it!
			return index

	# checking last element
	if (fn1) and (array[size-1] == x):
		return size-1
	return -1


array = [10,20,30,40,50,60,70,80,90,100,110]
size = len(array)
x = int(input())
result = fibunacciSearch(array,x,size)
if result != -1:
    print(f"(Fibunacci) Found at index: {str(result)}")
else:
    print("(Fibunacci) Not found")
