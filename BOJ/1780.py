n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
ans_plus = 0
ans_zero = 0
ans_minus = 0
def re(x, y, len_arr):
    global ans_plus, ans_minus, ans_zero
    check = arr[x][y]
    for i in range(x, x + len_arr):
        for j in range(y, y + len_arr):
            if (arr[i][j] != check):
                for k in range(3):
                    for l in range(3):
                        re(x + k * len_arr // 3, y + l * len_arr // 3 ,len_arr // 3)
                return
    
    if check == -1:
        ans_minus += 1
    elif check == 0:
        ans_zero += 1
    elif check == 1:
        ans_plus += 1
        
re(0, 0, n)
print(ans_minus)
print(ans_zero)
print(ans_plus)