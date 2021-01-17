n_members = int(input())

age = []
name = []
for _ in range(n_members):
    x,y = input().split()
    x = int(x)
    age.append(x)
    name.append(y)

idx = sorted(range(len(age)), key=lambda k: age[k])

name = [name[i] for i in idx]
sorted_list = list(zip(sorted(age), name))

for i in sorted_list:
    print(i[0],i[1])