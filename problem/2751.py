def divide(list):
    list_result = []
    if len(list) <= 1:
        return list
    list_A = divide(list[:int(len(list)/2)])
    list_B = divide(list[int(len(list)/2):])

    while len(list_A) != 0 or len(list_B) != 0:
        if len(list_A) == 0:
            list_result.append(list_B.pop(0))
        elif len(list_B) == 0:
            list_result.append(list_A.pop(0))
        elif list_A[0] < list_B[0]:
            list_result.append(list_A.pop(0))
        else:
            list_result.append(list_B.pop(0))

    return list_result

n = int(input())
li = []
for i in range(n):
    number = int(input())
    li.append(number)

li = divide(li)
for j in range(n):
    print(li.pop(0))