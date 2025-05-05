from collections import deque

# # recursive funciton

# def dfs(graph , node , visited):

#     if node not in visited:
#         print(node, end=" ")
#         visited.add(node)

#         for neighbour in graph[node]:
#             dfs(graph,neighbour,visited)



# graph={}

# n= int(input("Enter number of vertices: "))
# e =int(input("Enter number of edeges:"))

# for i in range(n):
#     graph[i] =[]

# print("Enter edges (e.g '0 1) means edge b/w 0 and 1")
# for _ in range(e):

#     u,v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# print("\n Graph [Adjaceny list]")
# for node in graph:
#     print(f"{node}: {graph[node]}")


# start = int(input("\n Enter starting vertex for DFS:"))
# print("DFS Traversal")

# visited =set()

# dfs(graph, start , visited)


# bfs

# def bfs(graph, visited, queue):
    
#     if not  queue:
#         return
    
#     node= queue.popleft()
#     print(node, end=" ")

#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)


#     bfs(graph,visited,queue)     


# graph={}
# n=int(input("Enter no of vertices:"))
# e = int (input("Enter no of edges:"))


# for i in range(n):
#     graph[i]=[]



# print("Enter edges (eg 0 1) mean edge b/w 0 and 1 ")

# for _ in range(e):

#     u,v = map(int, input().split())

#     graph[u].append(v)
#     graph[v].append(u)



# print("Graph Adjacency list")

# for node in graph:

#     print(f"{node}: {graph[node]}")


# start= int(input("Enter starting vertex for bfs:"))
# visited= set()
# queue= deque()

# visited.add(start)
# queue.append(start)

# print("BFS Traversal")

# bfs(graph, visited, queue)


#  Selection sort

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min] =arr[min],arr[i]    
        print(f"Step{i+1}: {arr}")   

str= input("Enter input unsorted no separated by space:")

arr= list(map(int, str.split()))

print("\n Original arr")
print(arr)

selectionSort(arr)

print("\n Sorted arr")
print(arr)