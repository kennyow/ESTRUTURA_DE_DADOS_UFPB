class Graph:
    def __init__(self, n):
        #Número de Vértices do Grafo
        self.n = n
        #Matriz de Adjacência de Tamanho n inicializada com zeros
        self.M = [[0] * n for i in range(n)]
        #Lista que armazena os vértices adjacentes a cada vértice
        self.L = [[] for i in range(n)]
        
    def add_aresta(self, u, v):
        # valor 1 na posição correspondente aos vértices u e v e v e u (não direcionado).
        self.M[u][v] = 1
        self.M[v][u] = 1
        #adiciona o vértice v na lista de adjacência correspondente ao vértice u.
        self.L[u].append(v)
        #adiciona o vértice u na lista de adjacência correspondente ao vértice v.
        self.L[v].append(u)
        
    #BUSCA EM LARGURA POR MATRIZ
    def bfs_matriz(self, s):
        visitado = [False] * self.n
        #Lista vazia que será usada como fila na busca em largura.
        queue = []
        #Adiciona o vértice s na lista
        queue.append(s)
        #Marca o vértice s como visitado
        visitado[s] = True
        
        #Enquanto a lista não está vazia
        while queue:
            #Remove o primeiro elemento da fila e o atribui à variável u, que será o vértice atual da busca.
            u = queue.pop(0)
            print(u, end=" ")
            
            #Loop que percorre todos os vértices do grafo
            for v in range(self.n):
                #Confirma a aresta e se v ainda não foi visitado.
                if self.M[u][v] == 1 and not visitado[v]:
                    queue.append(v)
                    visitado[v] = True
        print("")

    #BUSCA EM LARGURA POR LISTA  
    def bfs_lista(self, s):
        visitado = [False] * self.n
        queue = []
        queue.append(s)
        visitado[s] = True
        
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            
            # Percorre a lista de adjacências do vértice visitado 'u'
            for v in self.L[u]:
                if not visitado[v]:
                    queue.append(v)
                    visitado[v] = True
        print("")

    #BUSCA EM PROFUNDIDADE POR MATRIZ    
    def dfs_matriz(self, s, visitado):
        #Vértice s visitado
        visitado[s] = True
        print(s, end=" ")
        #Percorre todos os vértices adjacentes a s
        for v in range(self.n):
            if self.M[s][v] == 1 and not visitado[v]:
                #Método é chamado recursivamente para visitar o vértice v
                self.dfs_matriz(v, visitado)
 

     #BUSCA EM PROFUNDIDADE POR LISTA          
    def dfs_lista(self, s, visitado):
        visitado[s] = True
        print(s, end=" ")
        
        #Verifica os vizinhos de s na lista de adjacências
        for v in self.L[s]:
            if not visitado[v]:
                self.dfs_lista(v, visitado)
    

# Cria um grafo com 11 vértices e adiciona as arestas
g = Graph(11)
g.add_aresta(0, 3)
g.add_aresta(1, 2)
g.add_aresta(2, 4)
g.add_aresta(2, 8)
g.add_aresta(2, 5)
g.add_aresta(3, 4)
g.add_aresta(3, 6)
g.add_aresta(4, 5)
g.add_aresta(5, 6)
g.add_aresta(6, 9)
g.add_aresta(9, 10)

# Faz a busca em largura usando a matriz de adjacência
print("Busca em Largura (Matriz):")
g.bfs_matriz(0)

# Faz a busca em largura usando a lista de adjacência
print("Busca em Largura (Lista):")
g.bfs_lista(0)

# Faz a busca em profundidade usando a matriz de adjacência
print("Busca em Profundidade (Matriz):")
visitado = [False] * g.n
g.dfs_matriz(0, visitado)
print("")

# Faz a busca em profundidade usando a lista de adjacência
print("Busca em Profundidade (Lista):")
visitado= [False] * g.n
g.dfs_lista(0, visitado)