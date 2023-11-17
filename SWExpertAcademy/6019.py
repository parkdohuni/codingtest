def fly_distance(D, A, B, F):
    time_to_collision = D / (A + B)  # 충돌까지 걸리는 시간
    fly_distance = F * time_to_collision  # 파리가 이동한 거리
    return fly_distance

# 테스트 케이스의 수 입력
tc = int(input())

for t in range(1, tc + 1):
    # 테스트 케이스 입력
    D, A, B, F = map(int, input().split())
    result = fly_distance(D, A, B, F)
    print("#{} {}".format(t, result))