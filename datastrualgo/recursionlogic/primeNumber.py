def primeNumber(n,i):
    if i==1:
        return 1
    elif n%i==0:
        return 0
    return primeNumber(n,i-1)


n=4
result=primeNumber(n,n-1)
if result==1:
    print("prime number")
elif result==0:
    print("NOT A prime number")


