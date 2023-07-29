import sys

input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    planets = list(map(int, input().split()))
    # 12 50 31
    keys = sorted(list(set(planets)))
    # 12 31 50
    ranks = {keys[i]: i for i in range(len(keys))}
    # 12:0 31:1 50:2
    add = tuple([ranks[x] for x in planets])
    # 0 2 1
    universe[add] += 1
    # (0 2 1): 1

ans = 0

for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2

print(ans)