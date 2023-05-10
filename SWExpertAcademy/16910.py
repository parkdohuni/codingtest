import sys

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if ((x ** 2) + (y ** 2)) <= (N ** 2):
                count += 1

    print(f'#{test_case} {count}')
