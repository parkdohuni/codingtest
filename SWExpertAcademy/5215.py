def max_taste(n, l, ingredients):
    dp = [[0] * (l + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(l + 1):
            taste, calorie = ingredients[i - 1]

            # 현재 재료를 선택하지 않는 경우
            dp[i][j] = dp[i - 1][j]

            # 현재 재료를 선택하는 경우
            if j >= calorie:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - calorie] + taste)

    return dp[n][l]


t = int(input())  # 테스트 케이스 수

for case in range(1, t + 1):
    n, l = map(int, input().split())  # 재료의 수, 제한 칼로리
    ingredients = [tuple(map(int, input().split())) for _ in range(n)]  # 재료 정보

    result = max_taste(n, l, ingredients)
    print(f"#{case} {result}")
