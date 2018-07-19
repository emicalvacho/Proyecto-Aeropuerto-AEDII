import os
import sys
import pprint

# import crearDicGrafo
# dicc = crearDicGrafo.Graph()
# dicc.crearGrafoCero()
# grafo = dicc.getGrafo()


def find_cycle(origen,grafo):
    existeCiclo = 0
    visitados = []
    pila = [(None,origen)]

    while pila:
        (prev, actual) = pila.pop()
        if actual not in visitados:
        	visitados.append(actual)
        for key in grafo[actual]:
            if key not in visitados:
                    pila.append((actual,key))
            elif key == prev:
                pass
            elif key in visitados:
                existeCiclo = 1
    if existeCiclo == 1:
        print("EXISTE CICLO")
    else:
        print("NO EXISTE CICLO")
                
        

    print()


