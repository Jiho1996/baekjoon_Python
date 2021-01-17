	l = []
for i in range(int(input())):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: (x[1], x[0]))
for i in range(len(l)):
    print(l[i][0], l[i][1])