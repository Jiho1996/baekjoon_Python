case= int(input())

for i in range(case):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, ans ))