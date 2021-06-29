def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] +arr2[i][j])
        answer.append(arr_sum)
    return answer

print(solution([[1,2,3],[2,3,4]],[[3,4,5],[5,6,7]]))