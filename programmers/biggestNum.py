def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))  # 정수를 문자열로 변환하여 비교

    # 정렬 기준을 재정의하여 문자열을 비교
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 모든 원소가 0인 경우 처리
    if numbers[0] == "0":
        return "0"

    return ''.join(numbers)



print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([87, 19]))
print(solution([87, 91]))
