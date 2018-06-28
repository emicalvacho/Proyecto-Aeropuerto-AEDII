import os
import sys

# import crearDicGrafo
# dicc = crearDicGrafo.Graph()
# dicc.crearGrafoCero()
# grafo = dicc.getGrafo()


def DFS(origen,grafo):	
    visitados = []
    pila = []
    print("\nLista de recorrido en profundidad\n")
    pila.append(origen)
    while pila:
        actual = pila.pop()
        if actual not in visitados:
        	print(actual,"-> ",end="")
        	visitados.append(actual)
        s = actual
        for key in grafo[s]:
             if key not in visitados:
                    pila.append(key)

    print()

# origen = 1
# DFS(origen,grafo)
