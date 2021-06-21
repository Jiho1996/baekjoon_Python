import sys

def solution(a, b):
    answer = 0
    if a > b :
        a , b = b , a
    return sum(range(a, b + 1))

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

print(solution(a,b))




