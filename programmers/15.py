from itertools import permutations


def solution(k, dungeons):
    clears = []
    dungeon_per = list(permutations(dungeons, len(dungeons)))

    for case in dungeon_per:
        cnt = 0
        temp = k
        for dungeon in case:
            if temp >= dungeon[0]:
                temp -= dungeon[1]
                cnt += 1
        clears.append(cnt)
    return max(clears)


solution(80, [[80, 20], [50, 40], [30, 10]])
