import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

if len(heap) == 1:
    print(0)
else:
    ans = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans += a + b
        heapq.heappush(heap, a + b)
    print(ans)