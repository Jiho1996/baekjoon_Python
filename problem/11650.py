N = int(input())
array = []

for _ in range(N):
    x, y = map(int,input().split())
    array.append((x,y))

array.sort()
array.sort(key= lambda x : x[0])


for i in array :
    print(*i)