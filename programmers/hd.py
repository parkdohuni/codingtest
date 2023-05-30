n = int(input())

arr = list(map(int, input()))
arr2 = [list(map(int, input())) for _ in range(n)]

### 정수 1개 입력받기
N = int(input())

### 한줄 정수 리스트 입력받기
li = [*map(int, input().split())]

### 여러개 정수 입력받기
a, b, c = map(int, input().split())

### 여러 줄의 정수 리스트 입력받기
n = int(input())
li = [int(input()) for _ in range(n)]
## n 없이 한 줄로
li = [int(input()) for _ in range(int(input()))]

### N행 배열 입력받기
#### 숫자인 경우
N = int(input())  # N개의 행
arr = [[*map(int, input().split())] for _ in range(N)]

#### 문자열인 경우
N = int(input())  # N개의 행
arr = [list(input()) for _ in range(N)]

## 입력 빠르게하기
import sys

input = sys.stdin.readline  # input함수 바꾸기
