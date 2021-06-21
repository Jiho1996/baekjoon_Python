def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if answer == [] :
        answer.append(-1)
    return sorted(answer)

print(solution([5,9,7,10],5))