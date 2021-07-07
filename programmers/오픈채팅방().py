import copy

record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]


def solution(record):
    answer = []
    temp = []
    change =[]
    tmp =[]
    # 한배열에 들어있는 record를 이차원 배열에 넣기, 띄워쓰기 단위로 split
    for i in range(len(record)):
        temp.append(list(map(str, record[i].split(' '))))

    # 배열의 첫번째 단어가 change라면 ,
    for k in range(len(temp)):
        if temp[k][0] == 'Change' :
            #미리 선언해둔 change에 temp의 'change enter leave' 제외하고 넣기.
            change.extend(temp[k][1:])
            # leave의 경우 except처리.
            try :
                for answers in temp:
                    # 배열 앞순서부터 id로 찾아, change로 바꾸기.
                    if change[0] in answers :
                        answers[2] = change[1]
            except :
                continue
    # ENTER의 경우,
    # tmp에 temp deepcopy
    tmp = copy.deepcopy(temp)
    for j in range(len(temp)):
        if temp[j][0] == 'Enter' :
            for d in range(len(temp)):
                try :
                    if tmp[d][1] == tmp[j][1] :
                        temp[d][2] = tmp[j][2]
                except :
                    continue

    for k in range(len(temp)):
        if temp[k][0] == 'Enter':
            answer += (temp[k][2]) + "님이 들어왔습니다.  "
        elif temp[k][0] == 'Leave' :
            for i in range(len(temp[i])):
                if temp[k][1] == temp[i][1]:
                    answer += (temp[i][2]) + "님이 나갔습니다.  "
                    break
        else :
            continue

    answer = list(map(str,''.join(answer).split('  ') ))
    del answer[-1]
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))