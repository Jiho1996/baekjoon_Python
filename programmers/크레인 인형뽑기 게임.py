answer_list = []
num_list = []

def solution(board, moves):
    list_sort(board, num_list)
    #print(num_list)
    for i in range(len(num_list)):
        num_list[i] = (list(reversed(num_list[i]))) # 중요!
    #print(num_list)
    stack_insert(num_list,answer_list, moves)
    #print(answer_list)
    for j in range(len(answer_list[:])-1):
        if answer_list[j] == answer_list[j+1]:
            answer_list[j], answer_list[j+1] = 'x' ,'x'
            if answer_list[j-1] == answer_list[j+2]:
                answer_list[j-1], answer_list[j+2] = 'x','x'
            #[4, 3, 1, 1, 3, 2]

    return (answer_list.count('x'))




def stack_insert(num_list, answer_list, moves):
    try :
        for i in moves :
            answer_list.append(num_list[i-1].pop())
    except :
        pass


def list_sort(board_list, num_list):
    for i in range(len(board_list)):
        if i != 0 :
            num_list.extend([temp])
        temp = []
        for j in range(len(board_list)):
            if board_list[j][i] != 0 :
                temp.append(board_list[j][i])
            if i == 4 and j == 4 : num_list.extend([temp])

# [1,5,3,5,1,2,1,4] 4
# 분홍-(초록-(파랑-파랑)-초록)-노랑-분홍
# 0 비어있음 1 파랑 2 노랑 3 초록 4 분홍 5 갈

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],[1, 5, 3, 5, 1, 2, 1, 4]))