
visited = []
graph = []

def dfs(node):
    visited[node] = True
    print(node, end=' ')
    
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor)

def init_graph(num_nodes):
    global graph, visited
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    visited = [False] * num_nodes
    
    graph[0][1] = graph[1][0] = 1
    graph[0][2] = graph[2][0] = 1
    graph[1][3] = graph[3][1] = 1
    graph[1][4] = graph[4][1] = 1

if __name__ == "__main__":
    init_graph(5)
    print("DFS starting from node 0:")
    dfs(0)