
from operator import itemgetter
from bitarray import bitarray

def read_graph(path, g_type, weight=False):
    """ 
    Cria uma representação do grafo a partir de um arquivo texto
    ------------------------------------------------------------------------------
    ENTRADA:
        - path (string): caminho para o arquivo texto do grafo que será lido
        - g_type (string): tipo de representção do grafo, podendo ser 'ma' (matriz
        de adjacência) ou 'la' (lista de adjacência)
        - weight: indica se é um grafo tem pesos nas arestas ou não
    ------------------------------------------------------------------------------
    SAÍDA:
        - matriz de adjacência (lista)
        ou
        - lista de adjacência (dicionário)
    """
    with open(path, 'r') as f:
        n = f.readline()
        n = int(n) # Número de vértices do grafo
        A = [] # Lista que conterá as arestas do grafo

        # Percorrendo o restante das linhas do arquivo e adicionando em A
        # as listas que representam as arestas
        for line in f:
            a = line.split(' ')
            for i in range(2):
                a[i] = int(a[i])
            if (weight == True):
                a[2] = float(a[2])

            A.append(a)

        # Criando a matriz de adjacência
        if (g_type == 'ma'):
            if (weight == False):
                ma = [bitarray([0]*n) for i in range(n)]
                for a in A:
                    ma[a[0]-1][a[1]-1] = 1
                    ma[a[1]-1][a[0]-1] = 1
                return ma

            elif (weight == True):
                # ma_w = [[None]*n for i in range(n)]
                ma_w = [[float('inf')]*n for i in range(n)]
                for i in range(n):
                    ma_w[i][i] = 0
                for a in A:
                    ma_w[a[0]-1][a[1]-1] = a[2]
                    ma_w[a[1]-1][a[0]-1] = a[2]
                return ma_w

        # Criando a lista de adjacência
        if (g_type == 'la'):
            la = {} # Dicionário inicialmente vazio 
            if (weight == False):
                for a in A:
                    if a[0] in la:
                        la[a[0]].add(a[1])
                    else:
                        la[a[0]] = {a[1]}

                    if a[1] in la:
                        la[a[1]].add(a[0])
                    else:
                        la[a[1]] = {a[0]}
                
            elif (weight == True):
                for a in A:
                    if a[0] in la:
                        la[a[0]].add((a[1], a[2]))
                    else:
                        la[a[0]] = {(a[1], a[2])}

                    if a[1] in la:
                        la[a[1]].add((a[0], a[2]))
                    else:
                        la[a[1]] = {(a[0], a[2])}

            return la



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
    elif isinstance(g, dict):
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
        while Q:
            v = Q.pop(0)
            for u in sorted(g[v]):
                if u in g[v] and visited[u-1] == 0:
                    visited[u-1] = 1
                    Q.append(u)
            explored.append(v) 
    
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
        - path (string): caminho que será usado para criar o arquivo texto contendo
        as informações da árvore
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
        while Q:
            v = Q.pop(0)
            for u in sorted(g[v]):
                if u in g[v] and visited[u-1] == 0:
                    visited[u-1] = 1
                    Q.append(u)
                    prev[u-1] = v

                for w in layers[layer]:
                    if u in g[w] and levels[u-1] == None:
                        levels[u-1] = layer + 1
                        cur_layer.append(u)

            layers.append(cur_layer)
            if cur_layer:
                layer += 1
                cur_layer = []


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
    visited = [0] * len(g) # Lista informando quais vértices já foram visitados
    visited[v_1-1] = 1
    explored = []
    P = [v_1]
    
    # Caso o grafo seja representado por uma matriz de adjacência
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
        while P:
            u = P.pop()
            if u not in explored:
                explored.append(u)
                for v in sorted(g[u], reverse=True):
                    P.append(v)

    return explored



def genTree_DFS(g, v_1, path):
    '''
    Cria um novo arquivo texto contendo a árvore gerada pelo algoritmo de busca em
    profundidade (DFS) a partir do vértice v_1
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): vértice inicial
        - path (string): caminho que será usado para criar o arquivo texto contendo
        as informações da árvore
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram visitados
    levels = [[i, None] for i in range(len(g))] # Lista dos níveis de cada vértice da árvore gerada 
    levels[v_1-1][1] = 0
    prev = [None] * len(g) # Lista informando o pai de cada vértice
    layer = 0 # Variável que nos informará em que layer estamos conforme formos entrando e saindo da
              # função de recursão

    # Definimos a função de recursão que usaremos para percorrer o grafo
    def recur_DFS(g, v, visited, layer):
        visited[v-1] = 1
        layer += 1

        # Caso o grafo seja representado por uma matriz de adjacência
        if isinstance(g, list):
            for i in range(len(g)):
                if g[v-1][i] == 1 and visited[i] == 0:
                    levels[i][1] = layer
                    prev[i] = v
                    recur_DFS(g, i+1, visited, layer)

        # Caso o grafo seja representado por uma lista de adjacência
        elif isinstance(g, dict):
            for u in g[v]:
                if visited[u-1] == 0:
                    levels[u-1][1] = layer
                    prev[u-1] = v
                    recur_DFS(g, u, visited, layer)


    # Chamando então a função para no final termos as listas dos níveis dos vértices e de seus vértices 
    # pais completas
    recur_DFS(g, v_1, visited, layer)

    # Organizamos a lista de níveis de forma crescente, ou seja, do menor nível para o maior nível
    levels = sorted(levels, key=itemgetter(1))

    # Por fim escrevemos as informações obtidas da árvore no arquivo texto
    with open(path, 'w') as f:
        f.write('Árvore gerada pelo algoritmo de busca em profundidade (DFS) a partir do vértice ' + str(v_1) + ': \n\n')

        for v in levels:
                f.write('Vértice: ' + str(v[0]+1) + ', Pai: ' + str(prev[v[0]]) + ', Nível: ' + str(v[1]) + '\n')



def dist(g, v_1, v_2):
    '''
    Determina a distância entre dois vértices no grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): Primeiro vértice
        - v_2 (int): Segundo vértice
    ------------------------------------------------------------------------------
    SAÍDA:
        - (int): Distância entre o vértice v_1 e v_2
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram explorados
    visited[v_1-1] = 1
    levels = [None] * len(g) # Lista dos níveis de cada vértice da árvore gerada 
    levels[v_1-1] = 0
    Q = [v_1]

    layer = 0 # Atual camada na qual estamos buscando os seus vértices
    cur_layer = [] # Lista em que serão adicionados os vértices correspondendo à camada atual
    layers = [[v_1]] # Lista contendo os vértices agrupados pelas suas respectivas camadas
                     # Ex: layers[i] é a lista dos vértices contidos na camada i

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        while Q:
            v = Q.pop(0)
            for i in range(len(g)):
                # Encontrando os vértices filhos de v
                if g[v-1][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    Q.append(i+1)

                for u in layers[layer]:
                    if g[i][u-1] == 1 and levels[i] == None:
                        #
                        if i+1 == v_2:
                            return layer + 1
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
        while Q:
            v = Q.pop(0)
            for u in sorted(g[v]):
                if u in g[v] and visited[u-1] == 0:
                    visited[u-1] = 1
                    Q.append(u)

                for w in layers[layer]:
                    if u in g[w] and levels[u-1] == None:
                        if u == v_2:
                            return layer + 1
                        levels[u-1] = layer + 1
                        cur_layer.append(u)

            layers.append(cur_layer)
            if cur_layer:
                layer += 1
                cur_layer = []

    return layers



def last_level(g, v_1):
    '''
    Determina o último nível da árvore gerada pelo algoritmo de busca em largura a
    partir do vértice v_1
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
        - v_1 (int): vértice inicial
    ------------------------------------------------------------------------------
    SAÍDA:
        - layer (int): Nível da última camada da árvore gerada apartir de v_1 usando
        a BFS
    '''
    visited = [0] * len(g) # Lista informando quais vértices já foram explorados
    visited[v_1-1] = 1
    levels = [None] * len(g) # Lista dos níveis de cada vértice da árvore gerada 
    levels[v_1-1] = 0
    Q = [v_1]

    layer = 0 # Atual camada na qual estamos buscando os seus vértices
    cur_layer = [] # Lista em que serão adicionados os vértices correspondendo à camada atual
    layers = [[v_1]] # Lista contendo os vértices agrupados pelas suas respectivas camadas
                     # Ex: layers[i] é a lista dos vértices contidos na camada i

    if isinstance(g, list):
        while Q:
            v = Q.pop(0)
            for i in range(len(g)):
                # Encontrando os vértices filhos de v
                if g[v-1][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    Q.append(i+1)

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

    return layer



def diameter(g):
    '''
    Determina o diâmetro do grafo 
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - diam (int): diâmetro
    '''
    diam = 0
    cur_diam = 0 # Valor do maior diâmetro achado até o momento
    
    if isinstance(g, list):
        for i in range(len(g)):
            cur_diam = last_level(g, i+1)
            if cur_diam > diam:
                diam = cur_diam
    return diam



def connected(g):
    '''
    Determina as componentes conexas do grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - C (list): Lista contendo as listas de vértices de cada componente conexa
        do grafo em ordem decrescente de tamanho
    '''
    C = []
    G = set([i+1 for i in range(len(g))]) # Contunto de todos os vértices do grafo

    # Como a função BFS() retorna todos os vértices que podemos chegar a partir de 
    # um vértice inicial, BFS(g, 1) nos retornará uma das partes conexas do grafo
    c = set(BFS(g, 1))
    # Ordenamos o conjunto de vértices desta parte conexa e adicionamos à C
    C.append(sorted(c))

    while G:
        # Iremos subtrair de G os vértices da parte conexa encontrada
        G = G - c
        if G:
            # Enquanto G não estiver vazio usamos o primeiro vértice de G (v) e 
            # repetimos o mesmo processo
            v = next(iter(G)) # 
            c = set(BFS(g, v))
            C.append(sorted(c))

    return sorted(C, key=len, reverse=True)



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
        f.write('Mediana de grau: ' + str(median_degree(g)) + '\n\n')

        # Sobre as partes conexas:
        C = connected(g)
        f.write('Componentes conexas: ' + str(len(C)) + '\n')
        f.write('Tamanho da maior componente conexa: ' + str(len(C[0])) + '\n')
        f.write('Tamanho da menor componente conexa: ' + str(len(C[-1])) + '\n')
