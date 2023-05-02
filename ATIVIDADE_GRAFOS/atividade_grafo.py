class Graph:
    def __init__(self, n):
        self.n = n
        self.M = [[0] * n for i in range(n)]
        self.L = [[] for i in range(n)]
        
    def add_edge(self, u, v):
        self.M[u][v] = 1
        self.M[v][u] = 1
        self.L[u].append(v)
        self.L[v].append(u)
        
    def bfs_matriz(self, s):
        visited = [False] * self.n
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            
            for v in range(self.n):
                if self.M[u][v] == 1 and not visited[v]:
                    queue.append(v)
                    visited[v] = True
        print("")
        
    def bfs_lista(self, s):
        visited = [False] * self.n
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            
            for v in self.L[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        print("")
        
    def dfs_matriz(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        for v in range(self.n):
            if self.M[s][v] == 1 and not visited[v]:
                self.dfs_matriz(v, visited)
        

                
    def dfs_lista(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        
        for v in self.L[s]:
            if not visited[v]:
                self.dfs_lista(v, visited)
    

# Cria um grafo com 4 vértices e adiciona as arestas
g = Graph(11)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(2, 8)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 9)
g.add_edge(9, 10)

# Faz a busca em largura usando a matriz de adjacência
print("Busca em Largura (Matriz):")
g.bfs_matriz(0)

# Faz a busca em largura usando a lista de adjacência
print("Busca em Largura (Lista):")
g.bfs_lista(0)

# Faz a busca em profundidade usando a matriz de adjacência
print("Busca em Profundidade (Matriz):")
visited = [False] * g.n
g.dfs_matriz(0, visited)

# Faz a busca em profundidade usando a lista de adjacência
print("Busca em Profundidade (Lista):")
visited = [False] * g.n
g.dfs_lista(0, visited)
