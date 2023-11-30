import sys

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken, house, val = [], [], []


def close(a, b):  # 요구사항인 M개 만큼 치킨집을 폐업해보자
    global distance_min
    if a > len(chicken):
        return
    if b == M:
        distance_all = 0
        for x, y in house:
            distance = float('inf')
            for i in val:
                r, c = chicken[i]
                dist = min(distance, abs(r - x) + abs(c - y))
            distance_all += dist
        distance_min = min(distance_min, distance_all)
        return

    val.append(a)
    close(a + 1, b + 1)
    val.pop()
    close(a + 1, b)


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

distance_min = float('inf')
close(0, 0)
print(distance_min)
