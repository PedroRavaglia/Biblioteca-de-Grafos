

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
        # as arrays que representam as arestas
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
                    la[a[0]].update([a[1]])
                else:
                    la[a[0]] = {a[1]}

                if a[1] in la:
                    la[a[1]].update([a[0]])
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
    v_n = len(g) # número de vértices do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        a_n = 0
        x = 0
        for l in g:
            for i in range(x, v_n):
                a_n += l[i]
            x += 1

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        ...

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
    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        degrees = [] # Lista que conterá o grau de cada vértice do grafo
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        d_min = min(degrees) 

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        ...

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
    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        degrees = [] # Lista que conterá o grau de cada vértice do grafo
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        d_max = max(degrees)

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        ...

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

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        degrees = [] # Lista que conterá o grau de cada vértice do grafo
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        mean = sum(degrees)/v_n

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        ...

    return mean


def median_degree(g):
    """
    Determina a mediana dos graus dos vértices de um grafo
    ------------------------------------------------------------------------------
    ENTRADA:
        - g (lista ou dicionário): grafo reprasentado por uma matriz de adjacência 
        ou uma lista de adjacência
    ------------------------------------------------------------------------------
    SAÍDA:
        - mean (int): mediana dos graus
    """
    v_n = len(g) # número de vértices do grafo

    # Caso o grafo seja representado por uma matriz de adjacência
    if isinstance(g, list):
        degrees = [] # Lista que conterá o grau de cada vértice do grafo
        d = 0 # Grau do vértice que está sendo analisado
        for l in g:
            for e in l:
                d += e
            degrees.append(d)
            d = 0
        degrees.sort()
        
        if v_n % 2 == 0:
            median = degrees[v_n//2]
        else:
            median = (degrees[(v_n - 1)//2] + degrees[(v_n + 1)//2]) // 2

    # Caso o grafo seja representado por uma lista de adjacência
    if isinstance(g, dict):
        ...

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