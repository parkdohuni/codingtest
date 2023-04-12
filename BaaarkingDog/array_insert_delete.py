import sys
input = input = sys.stdin.readline


arr = [10, 50, 40, 30, 70, 20]
len = 6
def insert_arr(idx, n, arr, length):
    arr.insert(idx, n)
    length += 1
    print(arr)

def delet_arr(idx, arr, length):
    del arr[idx]
    length -= 1
    print(arr)

insert_arr(3, 60, arr, len)
delet_arr(1, arr, len)
        
