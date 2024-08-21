def missing_number(n, arr):
    # Create hash array of size n+1
    hash = [0] * (n + 1)
    # Store frequencies of elements
    for num in arr:
        hash[num] = hash[num] + 1
    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    # Edge case handling (though problem guarantees a solution)
    return -1


def missing_number2(n, arr):
    sum_arr = sum(arr)
    expected_sum = (n * (n + 1)) // 2
    return expected_sum - sum_arr


# Driver code
arr = [1, 2, 3, 5]
n = 5
print(missing_number(n, arr))