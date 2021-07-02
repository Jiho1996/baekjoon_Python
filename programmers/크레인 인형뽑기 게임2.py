

def solution(board, moves):

    basket = []
    answer = 0
    for move in moves :
        for i in board :
            if i[move-1] != 0:
                basket.append(i[move-1])
                i[move-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)# -2부터 터뜨려야 됨 -1 부터 터뜨린다면 -1 터지고 그앞에 거가 터짐.
                        basket.pop(-1)
                        answer += 2
                break
    return answer



print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],[1, 5, 3, 5, 1, 2, 1, 4]))
