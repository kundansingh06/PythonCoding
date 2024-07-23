def binarySearchRecursive1(list, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)// 2
        if list[mid] == key:   # If found at mid, then return it
            return mid
        elif list[mid] > key: # Search the left half
            return binarySearchRecursive1(list, key, low, mid - 1)
        else:                  # Search the right half
            return binarySearchRecursive1(list, key, mid + 1, high)
    return -1



def binarySearchRecursive2(list, key, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if list[mid] == key:
            return mid
        if list[mid] > key:
            return binarySearchRecursive2(list, key, low, mid - 1)
        return binarySearchRecursive2(list, key, mid + 1, high)
    return -1



list = [4, 17, 32, 44, 75, 80, 86]
print("The array to be searched is: ", list)
key = 80
recursive1_result = binarySearchRecursive1(list, key, 0, len(list) - 1)
recursive2_result = binarySearchRecursive2(list, key, 0, len(list) - 1)
if recursive1_result == -1:
    print("Not found")
else:
    print(key,"-: Element is found at index", recursive1_result)