def solution(s):
    if 8>=len(s)>=1 and len(s) == 4 or len(s) == 6 :
        answer = True
        try :
            s = int(s)
        except :
            answer = False
        finally:
            return answer
    else : return False

s = "11a111"
print(len(s))
print(solution(s))