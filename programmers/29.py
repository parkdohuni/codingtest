from math import floor


def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    a = []
    b = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i:i+2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i:i+2])

    intersection_list = set(a) & set(b)
    union_list = set(a) | set(b)

    if len(union_list) == 0:
        return 65536

    intersection_len = sum([min(a.count(intersection), b.count(intersection)) for intersection in intersection_list])
    union_len = sum([max(a.count(union), b.count(union)) for union in union_list])

    answer = floor((intersection_len / union_len) * 65536)

    return answer

# solution("aa1+aa2", "AAAA12")
solution("FRANCE", "french")
solution("aaaaa", "aaa")
