from itertools import permutations
# permutation 없이 풀어보기!!


def solution(numbers):
    answer = 0
    prime_num(int(numbers))
    numberList = []
    for n in range(len(numbers)):
        temp = list(permutations(numbers,n+1))
        numberList+=[int(''.join(i)) for i in temp] # 리스트 컴프리핸션으로 문자열로 변환.
    for i in set(numberList):
        answer +=prime_num(i)

    print(answer)
#
def prime_num(numbers):
    temp = 0
    rst = 0
    for i in range(1,numbers+1):
        if numbers % i == 0 and numbers != 0:
            temp += 1
        if temp >= 3:
            break
    if temp == 2 :
        rst+=1
    return rst

solution("17")