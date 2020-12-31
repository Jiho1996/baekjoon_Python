num = int(input())

pit = 2*num -1

for i in range (1,(num*2)//2+1,1):
    print("*"*i," "*(2*num-2*i),"*"*i)

for i in range ((num*2)//2-1,0,-1) :
    print("*"*i," "*(2*num-2*i),"*"*i)