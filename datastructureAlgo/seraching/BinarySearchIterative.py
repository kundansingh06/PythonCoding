def binarySearchIterative1(list, key, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == key:
            return mid
        if list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


list = [4, 17, 32, 44, 75, 80, 86]
print("The list to be searched is: ", list)
key = 80
iterative1_result = binarySearchIterative1(list, key, 0, len(list) - 1)
if iterative1_result == -1:
    print("Not found")
else:
    print(key,"-: Element is found at index", iterative1_result)