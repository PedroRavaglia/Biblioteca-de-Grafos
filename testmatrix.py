


g = [[0,8,0,3],[8,0,2,5],[0,2,0,6],[3,5,6,0]]
v_1 = 3
v_n = len(g) # número de vértices do grafos

print("v_n -> " + str(v_n))

if isinstance(g, list):

    infinity = 999999999
    selected_node = [0] * len(g)
    selected_node[v_1] = True
    num_edge = 0

    print("Edge : weight \n")
    while(num_edge < (v_n - 1)):
        min = infinity
        a=0
        b=0
        for m in range(v_n):
            if selected_node[m]:
                for n in range(v_n):
                    if((not selected_node[n] and g[m][n])):
                        if(min > g[m][n]):
                            min = g[m][n]
                            a=m
                            b=n
        
        print(str(a) + "-" + str(b)+": "+ str(g[a][b]))
        selected_node[b] = True
        num_edge += 1


