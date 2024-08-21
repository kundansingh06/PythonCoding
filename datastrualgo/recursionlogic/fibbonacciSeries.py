def fibinnaci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibinnaci(n-2)+fibinnaci(n-1))

n=10
for i in range(1,n+1):
 print(fibinnaci(i))