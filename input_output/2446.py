num = int(input())

r = 2 * num - 1

for i in range(r, 0, -2):
    print(" " * int((r - i) / 2), "*" * i)

for i in range(num - 2, -1, -1):
    print(" " * (i+1) + "*" * ((num - i) * 2 - 1))
