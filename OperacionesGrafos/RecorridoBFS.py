import os
import sys

def BFS(origen,grafo):
	visitados = []
	cola = []
	print("\nLista de recorrido en anchura a partir del nodo",origen,"\n")
	cola.append(origen)
	while cola:
		actual = cola.pop(0)
		if actual not in visitados:
			print(actual,"-> ",end="")
			visitados.append(actual)
		S = str(actual)
		for key in grafo[S]: #grafo.vertices() ?
			if key not in visitados:
				cola.append(key)

	print()

"""
dicc = Graph()
dicc.crearGrafoCero()
grafo = dicc.getGrafo()
BFS(4,grafo)
os.system("pause")
"""
