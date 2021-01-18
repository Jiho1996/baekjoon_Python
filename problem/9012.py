N = int(input())
for i in range(N):
    temp = input()
    while "()" in temp:
        temp = temp.replace("()", "")
    if len(temp) > 0:
        print("NO")
    else:
        print("YES")