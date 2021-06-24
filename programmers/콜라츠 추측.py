def solution(num):
    result = 0
    if num == 1: # num이 1일때 연산횐수 0 리턴
        return 0
      # result 가 500이상 또는 입력된 수가 1이 될때 까지 반복.
    while(True):
        if num % 2 == 0 : # 짝수일때.
            num = num / 2
            result += 1
            if num == 1: break # 1일 시 break.
        else : # 홀수일때.
            num = num*3 + 1
            result += 1
            if num == 1: break # 1일시 break.
        if result > 500: # result가 500넘을시 조기리턴.
            return -1
    return result