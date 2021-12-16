
# import csv

# f = open('Grafos\grafo_1.txt', 'r') 
# f.close()

# Cria uma matriz de arrays nxn com todas as entradas iguais a zero
def create_matrix(n):
    M = []
    l = []
    for i in range(n):
        l.append(0)
    for i in range(n):
        M.append(l)
    return M

def read_file(path, g_type):
    # with open('Grafos\grafo_1.txt', 'r') as f:
    with open(path, 'r') as f:
        # Pegamos a primeira linha do arquivo texto 
        f_content = f.readline()
        n = int(f_content)

        #
        A = []
        for i in range(n):
            f_content = f.readline()
            f_content = f_content[:-1]
            f_content = f_content.split(' ')
            for j in range(2):
                f_content[j] = int(f_content[j])
            A.append(f_content)
        # print(A)
        # print(len(A))
        
        if (g_type == 'ma'):
            M = create_matrix(n)
            # print(M[n-1][n-1])
            for i in range(n):
                print(A[i][0], A[i][1])
                M[A[i][0]-1][A[i][1]-1] = 1

            return M

M = read_file('Grafos\grafo_1.txt', 'ma')
print(M)
# read_file('Grafos\grafo_1.txt', 'ma')

# print(A)
# print(len(A))


# M = create_matrix(100)
# print(len(M[0]))
    
