import sys

def solution(n):
    answer = ''
    soo = "수"
    park = "박"
    for i in range(n):
        if i % 2 == 0 :
            answer += soo
        else:
            answer += park
    return answer


n = int(sys.stdin.readline())
print(solution(n))

