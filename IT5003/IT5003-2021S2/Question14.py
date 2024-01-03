'''
V, E = map(int, input().split())
graph = [[] for _ in range(V)]
visited = [False] *V
# Read the directed edges
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dfs(visited, path, current_vertex, current_cost):
    path.append(current_vertex)
    visited[current_vertex] = True
    if( not graph[current_vertex]):
        return( path,current_cost)
    for next_vertex, next_weight in graph[current_vertex]:
        next_cost = current_cost+next_weight
        result_path = dfs(visited,path, next_vertex,  next_cost)
        print(result_path)
        path = []
        visited = [False] *V

path = []
dfs(visited, path,0,0)
'''
'''
use dfs to iterate through every path till the end vertex
record the path which has even count and compare the cost, choose the cheapest path
'''

'''
use modified dijkstra 
'''
def dijkstra(AL, start, V):
    distance = [float('inf')] * V
    distance[start] = 0

    for u in range(V):
        for v, d1 in AL[u]:
            for z, d2 in AL[v]:
                new_dist = d1 + d2

                if new_dist < distance[z]:
                    distance[z] = new_dist
    print(distance)
    return distance[-1] if distance[-1] != float('inf') else -1

# Example usage
V, E = map(int, input().split())
AL = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))

result = dijkstra(AL, 0, V)
print(result)

'''
4 5
0 1 5
0 3 1
0 2 4
1 3 3
2 3 3

'''