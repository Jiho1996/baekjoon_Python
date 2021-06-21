def solution(strings, n):
    answer = []
    # 문자열 가장앞에 n번째 인덱스 넣기.
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    # 문자열 정렬.
    strings.sort()
    # 문자열 복구 및 정답도출.
    for i in range(len(strings)):
        strings[i] = strings[i][1:]
    answer.extend(strings)
    return answer

print(solution(["abcd", "abce", "cdx"],2))
