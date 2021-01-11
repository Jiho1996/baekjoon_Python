n = int(input())
lst = list(map(int, input().split()))

a = [1 for i in range(n)]
b = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            a[i] = max(a[i], a[j] + 1)
lst.reverse()
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            b[i] = max(b[i], b[j] + 1)
b.reverse()
c = [0 for i in range(n)]
for i in range(n):
    c[i] = a[i] + b[i]
print(max(c) - 1)