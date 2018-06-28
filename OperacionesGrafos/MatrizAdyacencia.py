def matrizAdyacencia(G):
    v = len(G.vertices())
    #Creo una matriz de ceros con las dimensiones NroVertices x NroVertices
    matriz = [[0 for y in range(v)] for y in range(v)]
    x=0
    y=0
    dic = G.getGrafo()
    #Recorro el diccionario del grafo para encontrar los adyacentes de cada vertice
    for key1 in dic.keys():
        #Lista con los adyacentes de "key1"
        lista = dic[key1]
        for key2 in dic.keys():
            if key2 in lista:
                #Es adyacente de "key1"
                matriz[x][y] = 1
            else:
                #No es adyacente de "key1"
                matriz[x][y] = 0
            y+=1
        x+=1
        y=0
    return matriz
