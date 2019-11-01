# ДЗ к Уроку №8 Гладышев ВВ

"""
Задание №2
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    path = ['inf' for _ in range(length)]
    path[start] = start
    net = {}

    while min_cost < float('inf'):
        cost_c = cost.copy()
        is_visited[start] = True
        print(f'Вершина: {start}')
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    if cost[i] != cost_c[i]:
                        net[start] = i
                        #net[start].append(i)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                #print(start)

        #print(cost_c)
        print(cost)

    print(net)
    return cost, path


s = int(input('От какой вершины идти: '))
cost_s, path_s = dijkstra(g, s)
print(f'Цена: {cost_s}')
print(f'Путь: {path_s}')
