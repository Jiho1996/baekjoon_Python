def solution(board, moves):
    basket = []  # 인형들을 담아줄 바구니~
    answer = 0  # 팡 터진 인형들 계산

    for move in moves:  # 사용자의 움직임 하나씩 출력
        for column in board:  # columns 출력
            # move는 1부터 시작하기 때문에 index로 사용하기 위해선 -1씩 해줘야 함
            if column[move - 1] != 0:  # 만약 column의 move가 0이 아니라면 (인형이 있다는 말)
                basket.append(column[move - 1])  # 해당 값을 인형 바구니에 담기

                if len(basket) > 1:  # 바구니에 인형이 2개 이상 들어가는데
                    if basket[-2] == basket[-1]:  # 인형이 두개가 겹친다면
                        del basket[-2]  # 터뜨린다
                        del basket[-1]  # 터뜨린다
                        answer += 2  # 터뜨린 인형 갯수 추가

                column[move - 1] = 0  # 뽑은 인형은 0 처리
                break
    return answer



print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],[1, 5, 3, 5, 1, 2, 1, 4]))
