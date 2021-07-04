def solution(numbers):
    answer = ''
    for num in range(len(numbers)) :
        if numbers[num] // 10 == 0 :
            continue
        else :
            numbers[num] = list(map(int, str(numbers[num])))

    return numbers





numbers = [3, 30, 34, 5, 9]
print(solution(numbers))