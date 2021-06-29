answer = []
def solution(n, m):

    GCD(n,m)
    LCM(n,m)
    return answer

def GCD(n,m):
    temp = []
    n_yaksu = [i for i in range(1, n + 1) if n % i == 0]
    m_yaksu = [j for j in range(1, m + 1) if m % j == 0]
    for a in n_yaksu:
        for b in m_yaksu:
            if a == b:
                temp.append(a)
    answer.append(max(temp))

def LCM(n,m):
    for i in range(max(n,m), n*m+1):
        if i% n == 0 and i % m == 0:
            answer.append(i)
            break



print(solution(2,5))