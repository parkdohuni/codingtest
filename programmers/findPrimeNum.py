import math
from itertools import permutations


# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    answer = set()  # 중복된 소수를 방지하기 위해 set을 사용합니다.
    for i in range(1, len(numbers) + 1):
        perms = set(permutations(numbers, i))  # 가능한 모든 순열을 구합니다.
        for perm in perms:
            num = int(''.join(perm))
            if is_prime_number(num):
                answer.add(num)
    return len(answer)


print(solution("123"))
