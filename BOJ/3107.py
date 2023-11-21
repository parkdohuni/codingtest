def expand_ipv6(ipv6):
    # 그룹을 콜론 (:)으로 분할
    groups = ipv6.split(':')
    check = False
    arr = []
    # 축약된 그룹을 찾아서 확장
    for i in groups:
        if i == '' and not check:
            arr += ['0000' for _ in range(8 - len(groups) + 1)]
            check = True
        else:
            # 각 그룹의 앞자리에 0을 채워 4자리로 만듦
            arr.append(i.zfill(4))

    # 확장된 그룹을 콜론 (:)으로 조합하여 IPv6 주소 생성
    expanded_ipv6 = ':'.join(arr)

    return expanded_ipv6

# 입력 받기
input_ipv6 = input().strip()

# IPv6 확장 및 출력
result_ipv6 = expand_ipv6(input_ipv6)
print(result_ipv6)
