def solution(n):
    n = ''.join(list(map(str,sorted(str(n), reverse=True))))
    return int(n)