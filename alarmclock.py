import sys

hour, min = map(int, input().split())
if min < 45:
    min = min + 15
    if hour == 0:
        hour = 24
    hour = hour - 1
    print(hour, min)
else:
    min = min - 45
    print(hour, min)
    