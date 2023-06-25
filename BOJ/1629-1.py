a, b, c = map(int, input().split())

def re(a, n):
    if n == 1:
        return a % c
    else:
        temp = re(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

print(re(a, b))