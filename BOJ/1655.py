import sys
import heapq

input = sys.stdin.readline
n = int(input())
leftHeap = []
rightHeap = []
ans = []
for _ in range(n):
    data = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-data, data))
    else:
        heapq.heappush(rightHeap, (data, data))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        right = heapq.heappop(rightHeap)[0]
        left = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-right, right))
        heapq.heappush(rightHeap, (left, left))

    ans.append(leftHeap[0][1])

for i in ans:
    print(i)
