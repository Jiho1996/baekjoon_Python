N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(1)

else:
    temp_1 = 1
    temp_2 = 1
    current = 0
    for _ in range(N - 2):
        current = temp_1 + temp_2
        temp_1 = temp_2
        temp_2 = current
    print(current)