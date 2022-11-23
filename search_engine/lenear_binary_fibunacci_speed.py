import timeit
import time
from bisect import bisect_left

# Declaring the needed veriables
input = int(input("Enter the numbers to search: "))
print("----------------------")
flag = False
fileNew = []
file = []

# Opening and creating an arr with the values ("Without \n")

with open("search_engine/file.txt",'r',encoding='utf-8') as f:
	for line in f:
		fileNew.append(line)

for nums in fileNew:
	nums = nums.strip()
	file.append(int(nums))

    
# -------------------------------------------------------
# Linear search

# Checks on what index is the number
def linearSearch(array,input):
	for num in file:
		if num == input:
			print(f"(Linear) Found at index: {num-1}")
			flag = True
			break
	# Checks if the number is even in the file
	if flag == False:
		print("(Linear) Not found")
startLinear = time.time()
linearSearch(file,input)
endLinear = time.time()


# -------------------------------------------------------
# Binary Search
def binarySearch(array, input, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == input:
            return mid
        elif array[mid] < input:
            low = mid + 1
        else:
            high = mid - 1
    return -1

startBinary = time.time()
result = binarySearch(file, input, 0, len(file)-1)

if result != -1:
    print(f"(Binary) Found at index: {str(result)}")
else:
    print("(Binary )Not found")
endBinary = time.time()


# -------------------------------------------------------
# Fibunacci Search
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
		if array[index] < input:
			fn = fn1
			fn1 = fn0
			fn0 = fn - fn1
			offset = index
		# If x < index fn
		# cut array after index+1
		elif array[index] > input:
			fn = fn0
			# fn1 = fn0
			fn1 = fn1-fn0
			fn0 = fn - fn1
		else:
			# It found it!
			return index

	# checking last element
	if (fn1) and (array[size-1] == input):
		return size-1
	return -1

startFibunacci = time.time()

n = len(file)
result = fibunacciSearch(file, input, n)
if result != -1:
    print(f"(Fibunacci) Found at index: {str(result)}")
else:
    print("(Fibunacci) Not found")
endFibunacci = time.time()


print("----------------------")
print(f"Linear took: {endLinear - startLinear} s")
print(f"Binary took: {endBinary - startBinary} s")
print(f"Fibunacci took: {endFibunacci - startFibunacci} s")
