import sys

N = int(sys.stdin.readline())
arr = [[0 for _ in range(N+1)] for _ in range(11)]
for i in range(1, 11):
    arr[i][1] = 1
for i in range(1, N+1):
    arr[0][i] = 1
for column in range(2, N+1):
    for row in range(1, 10):
        arr[row][column] = arr[row-1][column] + arr[row][column-1]

sumV = 0
for row in range(0, 10):
    sumV += arr[row][N]
print(sumV % 10007)