num = int(input())
a=[]
for i in range(num):
    cmd = input().split()
    if cmd[0] == 'push_front':
        a.insert(0,cmd[1])
    elif cmd[0] == 'push_back':
        a.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(a)!=0:
            print(a.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(a)!=0:
            print(a.pop(-1))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(a))
    elif cmd[0] == 'empty':
        if len(a) ==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(a)==0:
            print(-1)
        else:
            print(a[0])
    elif cmd[0] == 'back':
        if len(a)==0:
            print(-1)
        else:
            print(a[-1])