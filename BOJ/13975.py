import sys
import heapq

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    ans = 0

    while len(heap) > 1:
        add = 0
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        add += a + b
        ans += add
        heapq.heappush(heap, add)

    print(ans)
