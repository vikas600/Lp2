from collections import deque


def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    
    # Recursive call for next level
    bfs_recursive(graph, queue, visited)


graph = {}
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))


for i in range(n):
    graph[i] = []

print("Enter edges (like 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # undirected graph

print("\nGraph (Adjacency List):")
for node in graph:
    print(f"{node}: {graph[node]}")


start = int(input("\nEnter starting vertex for BFS: "))
visited = set()
queue = deque()


visited.add(start)
queue.append(start)

print("BFS Traversal:")
bfs_recursive(graph, queue, visited)


#input dalo ye wala
#6
#5
#0 1
#0 2
#1 3
#1 4
#2 5