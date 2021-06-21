def solution(s):
    s = sorted(s,reverse=True)
    ''.join(s)
    return ''.join(s)

s = "Zbcdefg"
print(solution(s))