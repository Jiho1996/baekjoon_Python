def solution(phone_number):
    # answer에 뒷 4자리를 제외한 나머지 전부 * + 뒷 4자리
    return ('*' * (len(phone_number[:-4]))) + phone_number[-4:]