from itertools import permutations

data = ["A", "B", "C"]
result = list(permutations(data, 3))
print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'C', 'A'), ('B', 'A', 'C'), ('C', 'A', 'B'), ('C', 'B', 'A')]

from itertools import combinations

data = ["A", "B", "C"]
result = list(combinations(data, 3))
print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
