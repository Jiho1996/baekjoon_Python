from itertools import permutations

n = '011'
print(set(list(map(''.join,permutations(list(n),3)))))
