def fac(n):
    sum =1
    for _ in range(1, n+1):
        sum *= _
    return sum

n, r = map(int, input().split())
print(fac(n+r-1)//(fac(r-1)*fac(n))%1000000000)