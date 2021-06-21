import sys

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v] :
        if not visited[i-1]:
            dfs(graph,i-1,visited)



n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph=[[] for _ in range(n)]
for _ in range(m):
    f_node , s_node = map(int,sys.stdin.readline().split())
    graph[f_node-1].append(s_node)
    graph[s_node-1].append(f_node)

visited = [False] * 7

print(dfs(graph,0,visited))
print(visited.count(True)-1)




