def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m+1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        print("Coloring of nodes:", color)
    else:
        print("No solution possible with", m, "colors.")

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (use 0/1):")
graph = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    graph.append(row)

m = int(input("Enter number of colors: "))
graph_coloring(graph, m)

#ye input dalo
# Enter number of vertices: 4
# Enter adjacency matrix:
# Row 1: 0 1 1 1
# Row 2: 1 0 1 0
# Row 3: 1 1 0 1
# Row 4: 1 0 1 0
# Enter number of colors: 3
