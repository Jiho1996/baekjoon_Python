def solution(record):
    dic, log = {}, []
    for i in range(len(record)):
        data = record[i].split()
        if (data[0] == 'Enter') or (data[0] == 'Leave'): log.append((data[0], data[1]))
        if (data[0] == 'Enter') or (data[0] == 'Change'): dic[data[1]] = data[2]
    answer = []
    for state, uid in log:
        if state == 'Enter': answer.append(dic[uid]+'님이 들어왔습니다.')
        else: answer.append(dic[uid]+'님이 나갔습니다.')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))