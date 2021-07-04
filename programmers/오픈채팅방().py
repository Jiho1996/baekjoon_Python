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
    for i in range(len(record)):
        temp.append(list(map(str, record[i].split(' '))))
    #print(temp)
    tmp = temp

    for k in range(len(temp)):
        if temp[k][0] == 'Change' :
            change.extend(temp[k][1:])
            try :
                for answers in temp:
                    if change[0] in answers :
                        answers[2] = change[1]
            except :
                continue

    for j in range(len(temp)):
        if temp[j][0] == 'Enter' :
            answer+= (temp[j][2])+ "님이 들어왔습니다.  "
            for d in range(len(temp)):
                try :
                    if tmp[d][1] == tmp[j][1] :
                        temp[d][2] = tmp[j][2]
                except :
                    continue

        elif temp[j][0] == 'Leave' :
            answer += (temp[j][1]) + "님이 나갔습니다.  "

    #print(change)
    #print(temp)
    #answer = ''.join(answer)
    answer = list(map(str,''.join(answer).split('  ') ))
    del answer[-1]

    print(answer)

                #for a in range(len(temp)):
                #    if temp[a][1] == change[0] :
                #        temp[a][2] = change[1]



    #print(answer)





print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))