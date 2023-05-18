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

# a = 10 , b = 11 , c = 12
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12