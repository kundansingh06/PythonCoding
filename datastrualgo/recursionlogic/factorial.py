def factorial1(n):
    if n==0:
        return 1
    return n * factorial1(n-1)

def factorial2(n):
    if n==0:
        return 1
    else:
        return n * factorial2(n-1)

result=factorial2(5)
print(result)
