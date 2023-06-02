
t = int(input())

for test_case in range(t):
    chess = [list(map(str, input().split())) for _ in range(8)]
    
    rook = 0
    for i in range(8):
        for j in range(8):
            if chess == 'O':
                chess += 1
                