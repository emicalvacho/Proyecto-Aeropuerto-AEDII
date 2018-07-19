#############################################################################################
#                                Datos de RecorridoBFS.py                                   #
#                                                                                           #
#############################################################################################
# - Autor: Jose Guareschi                                                                   #
#############################################################################################
# - Funcionalidad: realiza el recorrido en anchura del grafo de aeropuertos                 #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import os
import sys

def BFS(origen,grafo):
	"""
		Funcionamiento: realiza el recorrido en anchura del grafo de aeropuertos		
		Precondicion: recibe un origen y un grafo
		Postcondicion: no devuelve nada
	"""
	visitados = []
	cola = []
	print("\nLista de recorrido en anchura a partir del nodo",origen,"\n")
	cola.append(origen)
	while cola:
		actual = cola.pop(0)
		if actual not in visitados:
			print(actual,"-> ",end="")
			visitados.append(actual)
		S = actual
		for key in grafo[S]:
			if key not in visitados:
				cola.append(key)
	print()

# Testing 
# dicc = Graph()
# dicc.crearGrafoCero()
# grafo = dicc.getGrafo()
# BFS(4,grafo)
# os.system("pause")
