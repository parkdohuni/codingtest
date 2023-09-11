import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = list(map(int, input().split()))
    for i in num:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)


print(heap[0])
