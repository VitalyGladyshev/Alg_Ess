# ДЗ к Уроку №8 Гладышев ВВ

"""
Задание №3
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
"""


#
#   2--0--6--7   1--9   5
#   |  |  |
#   3--4  8
#
n = 10
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]

visited = [False] * n
component = [-1] * n  # для каждой вершины храним номер её компоненты
num_components = 0

def dfs(v):
    component[v] = num_components
    visited[v] = True
    for w in adj_list[v]:
        if visited[w] == False:
            dfs(w)

visited = [False] * n
for v in range(n):
    if not visited[v]:
        dfs(v)
        num_components += 1