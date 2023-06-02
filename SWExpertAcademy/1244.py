t = int(input())

for test_case in range(1, t + 1):
    n, c = input().split()
    now = set([n])
    next = set()

    for _ in range(int(c)):
        while now:
            s = list(now.pop())
            for i in range(0, len(n)):
                for j in range(i + 1, len(n)):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[j], s[i] = s[i], s[j]
        now, next = next, now

    print("#{} {}".format(test_case, max(map(int, now))))
