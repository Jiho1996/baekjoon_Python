new_id = "123_.def"


def solution(new_id):
    new_id = FirstStep(new_id)
    new_id = SecondStep(new_id)
    new_id = ThridStep(new_id)
    new_id = FourthStep(new_id)
    new_id = FifthStep(new_id)
    new_id = SixthStep(new_id)
    new_id = SeventhStep(new_id)
    return new_id

def FirstStep(new_id):
    new_id = new_id.lower()
    return new_id

def SecondStep(new_id):
    #알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    temp = []
    for i in range(len(new_id)):
        temp.append(ord(new_id[i]))
        if not (97 <= temp[-1] <= 122 or 48 <= temp[-1] <= 57 or temp[-1] == 45 \
                or temp[-1] == 46 or temp[-1] == 95) :
            del temp[-1]
            continue
        temp[-1] = chr(temp[-1])
    return ''.join(temp)

def ThridStep(new_id):
    count = 0
    temp = []
    for num in new_id:
        temp.append(num)
        if temp[-1] == '.':
            count+=1
        else : count = 0
        if count > 1 :
            temp.pop(-1)
    return ''.join(temp)

def FourthStep(new_id):
    try :
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    except :
        pass

    return new_id


def FifthStep(new_id):
    if new_id == '' :
        new_id = 'a'
    return new_id

def SixthStep(new_id):
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    return new_id

def SeventhStep(new_id):
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id = new_id + new_id[-1]
    return new_id






print(solution(new_id))
#print(ord(new_id))