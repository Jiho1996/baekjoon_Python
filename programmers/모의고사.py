import sys

def solution(answers):
    answer = []
    math = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            ]
    rst = 0
    rst_list = []
    ans_len = len(answers)
    for num in range(3):
        if ans_len > len(math[num]) :
            if ans_len - len(math[num]) > len(math[num]) :
                math[num].extend(math[num] * ((ans_len - len(math[num])) // len(math[num])))
            math[num].extend(math[num][:ans_len-len(math[num])+1])

        for i in range(len(answers)) :
            if answers[i] == math[num][i] :
                rst += 1
        rst_list.append(rst)
        rst = 0

    if rst_list[0] == max(rst_list):
        answer.append(1)
    if rst_list[1] == max(rst_list):
        answer.append(2)
    if rst_list[2] == max(rst_list):
        answer.append(3)
    return answer




print(solution([1,3,2,4,2]))