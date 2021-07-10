

answer_list = []

def solution(priorities, location):
    list1 = list(enumerate(priorities))
    sort_and_append(list1)
    return answer_list.index(location) + 1


def sort_and_append(list1):

    for i in range(len(list1)):
        #print(max(list1, key=lambda x: x[1]))
        if list1[0] == max(list1, key=lambda x:x[1]):
            answer_list.append(list1[0][0])
            del list1[0]
            if list1 == []: print(answer_list)
            else : sort_and_append(list1)
            break
        else :
            list1.append(list1[0])
            del list1[0]

print(solution([2,1,3,2],2))


