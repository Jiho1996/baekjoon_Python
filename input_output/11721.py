cut = list(input())

for i in range(0,len(cut),1):
    if cut[i] == "":
        break
    else :
        if i == 9:
            print(cut[i],"\n")
        else :
            print(cut[i], end='')