
n = int(input("Unesite prirodan broj n: "))
k1 = int(input("Unesite vrijednost prirodnog broja k_1: "))
k2 = int(input("Unesite vrijednost prirodnog broja k_2: "))
k3 = int(input("Unesite vrijednost prirodnog broja k_3: "))
k4 = int(input("Unesite vrijednost prirodnog broja k_4: "))
# n = 8
# k1 = 2
# k2 = 4
# k3 = 6
# k4 = 7
kl = [k1, k2, k3, k4]
edges = [[0 for j in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        for l in kl:
            if abs(i-j) == l:
                edges[i][j] = 1

visited = set()
adj_dict = {}
for i in range(len(edges)):
    neighbors = []
    for j in range(len(edges[i])):
        if edges[i][j] == 1:
            neighbors.append(j)
    adj_dict[i] = neighbors

graph = adj_dict
visited = []


def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, 0)
graph = edges
path = [0] * n


def display_cycle():
    print("Cycle: ", end="")
    for i in range(n):
        print(path[i], end=" ")
    print(path[0])


def is_valid(v, k):
    if graph[path[k-1]][v] == 0:
        return False
    for i in range(k):
        if path[i] == v:
            return False
    return True


def cycle_found(t):
    if t == n:
        if graph[path[t-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, n):
        if is_valid(v, t):
            path[t] = v
            if cycle_found(t+1) == True:
                return True
            path[t] = -1
    return False


def hamiltonian_cycle():
    for i in range(n):
        path[i] = -1
    path[0] = 0  # first vertex as 0
    if cycle_found(1) == False:
        return False
    return True


if len(visited) == n:
    print("Graf G je povezan.")
    if hamiltonian_cycle() and n != 2 and n != 1:
        print("Graf G je hamiltonski.")
    else:
        print("Graf G nije hamiltonski.")

else:
    print("Graf G nije povezan.")
    print("Graf G nije hamiltonski.")
