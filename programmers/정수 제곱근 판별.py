import math

def solution(n):
    num = math.sqrt(n)
    if num == int(num):
        return (int(num)+1)**2
    else : return -1

print(solution(121))