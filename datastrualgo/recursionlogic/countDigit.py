def countDigit(n):
    if n<10:
        return 1
    return 1+countDigit(n//10)

