import os
import sys
sys.path.append("..")
from Grafo.crearDicGrafo import Graph

def BFS(origen,grafo):
	visitados = []
	cola = []
	print("\nLista de recorrido en anchura\n")
	cola.append(origen)
	while cola:
		actual = cola.pop(0)
		if actual not in visitados:
			print(actual,"-> ",end="")
			visitados.append(actual)
		S = str(actual)
		for key in grafo[S]:
			if key not in visitados:
				cola.append(key)

	print()

dicc = Graph()
dicc.crearGrafoCero()
grafo = dicc.getGrafo()
BFS(origen,grafo)
os.system("pause")
