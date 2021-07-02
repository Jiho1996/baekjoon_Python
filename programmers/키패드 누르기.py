def solution(numbers, hand):
    location = ['*', '#']
    answer = ''
    for number in numbers :
        if number == 1 or number == 4 or number == 7 :
            answer+='L'
            location[0] = number

        elif number == 3 or number == 6 or number == 9 :
            answer+='R'
            location[1] = number

        #else :
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right" ))

def keypad(start, end) :
    temp = 0

    keypad_graph = [[],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],
                    [4,8],[0,5,7,9],[6,8]]
    visited = [False * len(keypad_graph) ]
    # 다익스트라가 기억이안난다..
    for visit in keypad_graph[start] :
        temp += 1





