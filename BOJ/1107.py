import sys
from collections import deque

input = sys.stdin.readline

channel = int(input())
n = int(input())
if n > 0:
    broken = list(map(int, input().split()))
controller = [i for i in range(10)]
for i in broken:
    if i in controller:
        controller.remove(i)
print(controller)
start = 100
ans = 0


def remote(channel):
    q = deque()
    while channel != 0:
        num = channel % 10
        channel = channel // 10
        st = min(controller)
        en = max(controller)
        if num in broken:
            if num - st <= en - num:
                q.appendleft(st)
            else:
                q.appendleft(en)
        else:
            q.appendleft(num)
    print(*q)


remote(channel)
