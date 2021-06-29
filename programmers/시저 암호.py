def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else :
            temp = ord(s[i]) +n
            if 97<=ord(s[i])<=122 and temp > 122 :
                temp = 97 + (temp - 122 - 1)
            if 65<=ord(s[i])<=90 and temp > 90 :
                temp = 65 + (temp - 90 - 1)
            answer += chr(temp)

    return answer

print(solution("zZz",4))
