# DFS function (recursive)
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


graph = {}
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))


for i in range(n):
    graph[i] = []  #empty list for every node


print("Enter edges (e.g., '0 1' means edge between vertex 0 and 1):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


print("\nGraph (Adjacency List):")
for node in graph:
    print(f"{node}: {graph[node]}")


start = int(input("\nEnter starting vertex for DFS: "))
print("DFS Traversal:")
visited = set()
dfs(graph, start, visited)

#input dalo ye wala
#6
#5
#0 1
#0 2
#1 3
#1 4
#2 5