
x = int(input())
ct = 0

print(x, end=' ')
while True:

    if x == 1:
        print("\n연산횟수 : ",ct)
        break
    else:
        print("-->", end=' ')
        if (x%3 == 0):
            x = x // 3

        elif (x%2 == 0) :
            x = x //2

        else : x = x-1
        ct = ct+1
    print(x, end=' ')
