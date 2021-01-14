num = int(input())

lt = [0,1,3]
if num == 1:
  print(lt[1])
elif num == 2:
  print(lt[2])
else:
  for i in range(3, num + 1):
    lt.append(lt[i - 1] + lt[i - 2] * 2)
  print(lt[num] % 10007)