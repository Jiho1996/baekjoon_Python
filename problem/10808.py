str = input()

result = [0] * 26

for i in range(str):
    result[ord(i) - 97] = str.count(i)

for i in result:
    print(i, end=" ")