def solution(sizes):
    answer = 0
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]

    xsize = sorted(sizes,reverse=True)
    sizes.sort(key=lambda x:x[1], reverse=True)
    return xsize[0][0] * sizes[0][1]

print(solution([[30, 50], [50, 70], [60, 30], [80, 40]]))
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
