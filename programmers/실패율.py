
def solution(N, stages):
    answer = []
    temp = []
    for level in range(1,N+1):
        bunja = 0
        bunmo = 0
        if stages == []:
            break

        for stage in stages[:]:
            if stage >= level :
                bunmo += 1
            if stage == level :
                bunja += 1
                stages.remove(stage)
        temp.append((bunja/bunmo))

    print(temp)
    for _ in range(len(temp)):
        for i in range(len(temp)):
            if temp[i] == max(temp):
                answer.append(i+1)
                temp[i] = -1
                break
    return answer

stages = [4,4,4,4,4]
N = 5

print(solution(N,stages))
