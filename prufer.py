import heapq
import math
from typing import List, Tuple

#n = input("Hello")
#a
#b
#c
#n = int(input("Unesite prirodan broj n: "))
#a = int(input("Unesite vrijednost prirodnog broja k_1: "))
#b = int(input("Unesite vrijednost prirodnog broja k_2: "))
#c = int(input("Unesite vrijednost prirodnog broja k_3: "))
susjedstvo = []
n = 32
a = 40
b = 38
c = 78


def prufer(mst, ponavljanja):
    pruferkod = []
    temp = mst
    for i in range(0, ponavljanja-2):
        num = temp[-2] if temp[0] > temp[-1] else temp[1]
        pruferkod.append(num)
        if temp[0] > temp[-1]:
            temp.pop(-1)
        else:
            temp.pop(0)
    print(pruferkod)



def dict_maker(edges):
    help_dict = {}
    for i in range(len(edges)):
        neighbors = []
        for j in range(len(edges[i])):
            if edges[i][j] != 0:
                neighbors.append(j+1)
        help_dict[i+1] = neighbors
    return help_dict


def matrix_maker(edges, n, a, b, c):
    edges = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                solution = a * (i+1) / c - b * (j+1) / c
                solution = math.floor(abs(solution))
                if solution != 0:
                    edges[i][j] = solution
                    edges[j][i] = solution
    return edges


def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def najmanji(dic):
    f = {}
    for t in dic:
        f[len(dic.get(t))] = t
    return list(f.values())[0]


def mst(G, V):
    INF = 9999
    selected = [0] * n
    no_edge = 0
    path = {}
    selected[0] = True
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        path[x+1] = j+1
        #print(str(x+1) + "-" + str(y+1) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1

    print(path)
    return path


susjedstvo = matrix_maker(susjedstvo, n, a, b, c)
stablo = mst(susjedstvo, n)
visit = set()
graphs = susjedstvo
visit = []
dfs(visit, graphs, 1)
#if len(visited) == n:
#    print("Graf G je povezan.")
def minimum_spanning_tree_and_prufer(n: int, a: int, b: int, c: int) -> Tuple[int, List[int]]:
    g = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            w = math.floor(abs(a * min(i, j) - b * max(i, j)) / c)
            if w != 0:
                g[i].append((j, w))
                g[j].append((i, w))

    visited = [False] * (n + 1)
    q = [1]
    visited[1] = True
    while q:
        u = q.pop(0)
        visited[u] = True
        for v, w in g[u]:
            if not visited[v]:
                q.append(v)

    connected = all(visited)
    if not connected:
        return 0, []

    parent = [-1] * (n + 1)
    key = [float("inf")] * (n + 1)
    in_mst = [False] * (n + 1)
    pq = [(0, 1)]
    key[1] = 0
    while pq:
        w, u = heapq.heappop(pq)
        in_mst[u] = True
        for v, w in g[u]:
            if not in_mst[v] and key[v] > w:
                key[v] = w
                heapq.heappush(pq, (key[v], v))
                parent[v] = u

    mst = sum(key[i] for i in range(2, n + 1))
    prufer = []
    for i in range(2, n):
        prufer.append(parent[i])
    return mst, prufer


mast, pruf = minimum_spanning_tree_and_prufer(n, a, b, c)
print(mast)
print(pruf)
# d[i] = [x for x in d[i] if x != pamti]
#(5,2,3)
###
