import math

def solution(s):
    if len(s) % 2 != 0:
        return s[math.floor(len(s) // 2)]
    else :
        return s[len(s)//2 - 1 : len(s)//2 + 1]


s = "abcde"

print(solution(s))