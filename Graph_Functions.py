

def read_graph(path, g_type):
    """ 
    Cria uma representação do grafo a partirde um arquivo texto
    ------------------------------------------------------------------------------
    ENTRADA:
        - path (string): caminho para o arquivo texto do grafo
        - g_type (string): tipo de representção do grafo, podendo ser 'ma' (matriz
        de adjacência) ou 'la' (lista de adjacência)
    ------------------------------------------------------------------------------
    SAÍDA:
        - matriz de adjacência (lista)
        ou
        - lista de adjacência (dicionário)
    """
    with open(path, 'r') as f:
        n = f.readline()
        n = int(n) # Número de vértices do grafo
        A = [] # Array que conterá as arestas do grafo

        # Percorrendo o restante das linhas do arquivo e adicionando em A
        # as listas que representam as arestas
        for line in f:
            a = line.split(' ')
            for i in range(2):
                a[i] = int(a[i])
            A.append(a)

        # Criando a matriz de adjacência
        if (g_type == 'ma'):
            ma = [[0]*n for i in range(n)] # matriz nxn com todas as entradas iguais a zero 
            for a in A:
                ma[a[0]-1][a[1]-1] = 1
                ma[a[1]-1][a[0]-1] = 1
            return ma

        # Criando a lista de adjacência
        if (g_type == 'la'):
            la = {} # Dicionário inicialmente vazio 
            for a in A:
                if a[0] in la:
                    la[a[0]].add(a[1])
                else:
                    la[a[0]] = {a[1]}

                if a[1] in la:
                    la[a[1]].add(a[0])
                else:
                    la[a[1]] = {a[0]}
            return la

        # Caso o usuário tenha passado um tipo errado de representação
        else:
            print('\nTipo errado de representção do grafo. Escolher entre "ma" (matriz'
                + 'de adjacência) ou "la" (lista de adjacência)')



def num_edges(g):
    """
    Determina o número de arestas de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - a_n (int): número de arestas
    """
    a_n = 0
    v_n = len(g) # número de vértices do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        x = 0 # Variável que nos fará percorrer apenas a perte triangular superior da matriz
        for l in g:
            for i in range(x, v_n):
                a_n += l[i]
            x += 1
        

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        edges = [[0] for i in range(v_n)] # Lista em que na posição i iremos adicionar os vértices
                                          # que se ligam ao vértice i.
        for v in g:
            for u in g[v]:
                if u not in edges[v-1]:
                    a_n += 1
                edges[v-1].append(u)
                edges[u-1].append(v)

    return a_n



def min_degree(g):
    """
    Determina o grau mínimo dos vértices de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - d_min (int): grau mínimo
    """
    degrees = [] # Lista que conterá o grau de cada vértice do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        d_min = min(degrees) 

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        for v in g:
            degrees.append(len(g[v]))
        d_min = min(degrees)

    return d_min



def max_degree(g):
    """
    Determina o grau máximo dos vértices de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - d_min (int): grau máximo
    """
    degrees = [] # Lista que conterá o grau de cada vértice do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        d_max = max(degrees)

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        for v in g:
            degrees.append(len(g[v]))
        d_max = max(degrees)

    return d_max



def mean_degree(g):
    """
    Determina a média dos graus dos vértices de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - mean (float): média dos graus
    """
    v_n = len(g) # número de vértices do grafo
    degrees = [] # Lista que conterá o grau de cada vértice do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        for v in g:
            degrees.append(len(g[v]))
    
    mean = sum(degrees)/v_n
    return round(mean, 2)



def median_degree(g):
    """
    Determina a mediana dos graus dos vértices de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - median (int): mediana dos graus
    """
    v_n = len(g) # número de vértices do grafo
    degrees = [] # Lista que conterá o grau de cada vértice do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        for v in g:
            degrees.append(len(g[v]))

    # Ordenamos a lista de graus para podermos selecionar a mediana
    degrees.sort()
    if v_n % 2 == 0:
        median = degrees[v_n//2]
    else:
        median = (degrees[(v_n - 1)//2] + degrees[(v_n + 1)//2]) // 2

    return median



def out_graph(g, path):
    """
    Cria um novo arquivo texto contendo informações sobre o grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - path (string): caminho que será usado para criar o arquivo texto
    """
    with open(path, 'w') as f:
        f.write('Número de vértices: ' + str(len(g)) + '\n')
        f.write('Número de arestas: ' + str(num_edges(g)) + '\n')
        f.write('Grau mínimo: ' + str(min_degree(g)) + '\n')
        f.write('Grau máximo: ' + str(max_degree(g)) + '\n')
        f.write('Grau médio: ' + str(mean_degree(g)) + '\n')
        f.write('Mediana de grau: ' + str(median_degree(g)) + '\n')



def BFS(g, v_1):
    '''
    Implementação do algoritmo de busca em largura
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): vértice inicial
    ------------------------------------------------------------------------------
    SAÍDA:
        - explored (list): lista contendo os vértices do grafo na ordem em que foram
        explorados (removidos da fila)
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram explorados
    visited[v_1-1] = 1
    explored = []
    Q = [v_1]

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, list):
        while Q:
            v = Q.pop(0)
            for i in range(len(g)):
                if g[v-1][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    Q.append(i+1)
            explored.append(v) 

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        ...
    
    return explored



def genTree_BFS(g, v_1, path):
    '''
    Cria um novo arquivo texto contendo a árvore gerada pelo algoritmo de busca em
    largura (BFS) a partir do vértice v_1
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): vértice inicial
        - path (string):
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram explorados
    visited[v_1-1] = 1
    levels = [None] * len(g) # Lista dos níveis de cada vértice da árvore gerada 
    levels[v_1-1] = 0
    prev = [None] * len(g) # Lista informando o pai de cada vértice
    Q = [v_1]

    layer = 0 # Atual camada na qual estamos buscando os seus vértices
    cur_layer = [] # Lista em que serão adicionados os vértices correspondendo à camada atual
    layers = [[v_1]] # Lista contendo os vértices agrupados pelas suas respectivas camadas
                     # Ex: layers[i] é a lista dos vértices contidos na camada i

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, list):
        while Q:
            v = Q.pop(0)
            for i in range(len(g)):
                # Encontrando os vértices filhos de v
                if g[v-1][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    Q.append(i+1)
                    prev[i] = v

                # Determinando em que camada os véstices se encontram
                for u in layers[layer]:
                    if g[i][u-1] == 1 and levels[i] == None:
                        levels[i] = layer + 1
                        cur_layer.append(i+1)

            # Depois teremos todos os vértices da camada atual contidos em cur_layer
            layers.append(cur_layer)
            # Caso a camada atual não seja vazia, incrementamos 'layer' para podermos encontrar os 
            # vértices da próxima camada
            if cur_layer:
                layer += 1
            cur_layer = []

    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        ...

    with open(path, 'w') as f:
        f.write('Árvore gerada pelo algoritmo de busca em largura (BFS) a partir do vértice ' + str(v_1) + ': \n\n')

        for i in range(layer+1):
            for v in layers[i]:
                f.write('Vértice: ' + str(v) + ', Pai: ' + str(prev[v-1]) + ', Nível: ' + str(levels[v-1]) + '\n')



def DFS(g, v_1):
    '''
    Implementação do algoritmo de busca em profundidade
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): vértice inicial
    ------------------------------------------------------------------------------
    SAÍDA:
        - explored (list): lista contendo os vértices do grafo na ordem em que foram
        explorados (removidos da pilha)
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram explorados
    visited[v_1-1] = 1
    explored = []
    P = [v_1]
    
    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, list):
        while P:
            u = P.pop()
            if u not in explored:
                explored.append(u)
                for i in range(len(g)-1, -1, -1):
                    if g[u-1][i] == 1:
                        P.append(i+1)


    # Caso o grafo seja representado por uma lista de adjacência
    elif isinstance(g, dict):
        ...

    return explored



def genTree_DFS(g, v_1):
    ...
    

def dist(g, v_1, v_2):
    ...

def diameter(g):
    ...
