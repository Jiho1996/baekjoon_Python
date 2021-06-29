def solution(s):
    return ''.join(sorted(s,reverse=True))

s = "Zbcdefg"
print(solution(s))