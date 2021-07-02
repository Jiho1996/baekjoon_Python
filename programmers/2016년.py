month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
temp = 0

def solution(a, b):
    temp = 0
    result = ''
    for i in range(a-1) :
        temp += month[i]
    temp += b
    temp = (temp+4) % 7
    return day[temp]

print(solution(5,24))