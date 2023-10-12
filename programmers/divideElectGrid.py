from collections import deque


def make_graph(wire, n):
    graph = []

    for i in range(n + 1):
        node = []
        graph.append(node)

    for i in range(len(wire)):
        graph[wire[i][0]].append(wire[i][1])
        graph[wire[i][1]].append(wire[i][0])

    return graph


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    arr = []

    while q:
        s = q.popleft()
        arr.append(s)
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return arr


def solution(n, wires):
    answer = 100
    wires = sorted(wires, key=lambda x: (x[0], x[1]))

    for i in range(len(wires)):
        wire = wires[:i] + wires[i + 1:]

        graph = make_graph(wire, n)

        node = []
        node = set(node)
        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            bfs(graph, j, visited)
            node.add(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
