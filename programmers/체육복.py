import sys

def solution(n, lost, reserve):
    answer = 0
    for k in reserve[:]:
        if k in lost:
            lost.remove(k)
            reserve.remove(k)

    for i in reserve[:]:
        for j in lost[:]:
            if i not in reserve or j not in lost:
                continue
            else:
                if i +1 == j or i -1 ==j :
                    reserve.remove(i)
                    lost.remove(j)
    answer = n - len(lost)
    return answer




n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

print(solution(n,lost,reserve))