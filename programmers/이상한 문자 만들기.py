def solution(s):
    temp = s.split(' ')
    answer = []
    for i in temp:
        temp_list = ''
        for j in range(len(i)):
            temp_list += i[j].upper() if j%2 == 0 else i[j].lower()
        answer.append(temp_list)
    return ' '.join(answer)


s= "try hello world"
print(solution(s))
