import copy

def solution(priorities, location):
    answer=[]
    priorities = list(enumerate(priorities))
    temp = copy.deepcopy(priorities)
    #print(temp)
    #print(max(priorities, key=lambda  x:x[0])[0])
    # 왜 max가 계속 3일까? 요소가 remove되면 max가 바뀌어야 하지 않나?
    for k in range(len(priorities)):
        for i in range(len(priorities)):
            if max(priorities, key=lambda x: x[0])[0] != priorities[i][1]:
                print(max(priorities, key=lambda x: x[0])[0])
                print(priorities)
                temp.append(priorities[i])
                temp.remove(priorities[i])
        answer.append(temp[0])
        priorities.remove(temp[0])
        del temp[0]

    print(priorities)
    print(answer)




print(solution([3, 1, 3, 2], 2))