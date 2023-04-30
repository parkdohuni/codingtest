import sys
from collections import deque

n = int(sys.stdin.readline())
deck = deque([])
for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push_front":
        deck.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deck.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.popleft())
    elif cmd[0] == "pop_back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())
    elif cmd[0] == "size":
        print(len(deck))
    elif cmd[0] == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif cmd[0] == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])