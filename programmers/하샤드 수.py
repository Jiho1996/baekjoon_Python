def solution(x):
    temp = []
    temp.extend(str(x)) # temp에 x넣기.
    for i in range(len(temp)): # sum하기 위해 int형변환.
        temp[i] = int(temp[i])
    if x % sum(temp) == 0 : # 자릿수합으로 나뉘어 지면 True , else False
        return True
    else : return False

print(solution(13))