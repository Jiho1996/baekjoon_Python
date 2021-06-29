def solution(arr):
    temp = []
    temp = sorted(arr, reverse=True) #  temp를 내림차순으로 정렬.
    arr.remove(temp[-1]) # arr의 가장 작은 수 temp를 이용해 제거.
    if len(arr) == 0:
        arr.append(-1) # 빈배열인 경우 -1 채우기.
    return arr