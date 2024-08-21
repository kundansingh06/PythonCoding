def linearSearch1(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    list = [4, 17, 32, 44, 75, 80, 86]
    print("The list to be searched is: ", list)
    key = 80
    result = linearSearch1(list, len(list), key)
    if(result == -1):
        print("Element is not present in array")
    else:
        print(key,"-: Element is found at index", result)