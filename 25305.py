#25305번 커트라인
import sys

n, k = map(int, input().split())

print(sorted(map(int, input().split()), reverse=True)[k-1])
