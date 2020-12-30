num = int(input())
tmp = 0

for k in range(0, num + 1, 1):
    list[k]

for i in range(0, num + 1, 1):
    list[i] = int(input())

for i in range(0, num, 1):
    if list[i] > list[i + 1]:
        tmp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = tmp
    else:
        continue
print(list[0], ",", list[num])
