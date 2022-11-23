def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = []
size = int(input("Numbers in arr: "))

for i in range(1,size+1):
    array.append(i)

x = int(input("x = "))

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
# with open("search_engine/binary.txt",'r',encoding="utf-8") as f:
    # for
