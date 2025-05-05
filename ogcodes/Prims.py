import sys

def prims_algorithm(graph, V):
    selected = [False] * V
    edge_count = 0
    selected[0] = True
    total_weight = 0

    print("\nEdge : Weight")
    while edge_count < V - 1:
        minimum = sys.maxsize
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] > 0:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        if minimum == sys.maxsize:
            print("Graph is disconnected. MST cannot be formed completely.")
            return

        print(f"{x} - {y} : {graph[x][y]}")
        total_weight += graph[x][y]
        selected[y] = True
        edge_count += 1

    print(f"\nTotal weight of MST: {total_weight}")

# Input
V = int(input("Enter number of vertices: "))
print("Enter the adjacency matrix (use 0 if no edge):")
graph = []
for i in range(V):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    graph.append(row)

# Run Prim's Algorithm
prims_algorithm(graph, V)


#input dalo ye wala

# Enter number of vertices: 4
# Enter the adjacency matrix (use 0 if no edge):
# Row 1: 0 1 3 0
# Row 2: 1 0 2 4
# Row 3: 3 2 0 5
# Row 4: 0 4 5 0
