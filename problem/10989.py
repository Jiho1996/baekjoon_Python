count = int(input())
a = []
for i in range(count):
    [Name, Kor, Eng, Math] = input().split()
    a.append([Name, Kor, Eng, Math])
b = sorted(a, key= lambda a: (-int(a[1]), int(a[2]), -int(a[3]), a[0]))
for i in range(count):
    print(b[i][0])