import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
cups = []
time = 0
for _ in range(n):
    deadLine, cup = map(int, input().split())
    time = max(time, deadLine)
    heapq.heappush(heap, (-deadLine, cup))


ans = 0
while time > 0:
    while heap:
        x, y = heapq.heappop(heap)

        if time == -x:
            heapq.heappush(cups, -y)
        else:
            heapq.heappush(heap, (x, y))
            break
    if cups:
        ans += -heapq.heappop(cups)

    time -= 1

print(ans)