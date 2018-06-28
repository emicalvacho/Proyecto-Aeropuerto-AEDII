import sys
import math
sys.path.append("..")
from Grafo.crearDicGrafo import Graph
from Grafo.distanciaRutas import distancia

"""
    Floyd-Warshall crea la matriz de cierre transitivo del grafo dado.
    Utiliza la función distancia para crear la matriz de distancias.
"""

def FloydWarshall(grafo):

    """
		Precondiciones: un grafo de la clase Graph
		Postcondiciones: devuelve la matriz de cierre transitivo del grafo
	"""

    #Creo la matriz de Nro.vertices x Nro.vertices con todos los valores en infinito
    v = len(grafo.vertices())
    dist = [[float("inf") for y in range(v)] for y in range(v)]
    #Lleno la matriz con las distancias
    for x in range(v):
        for y in range(v):
            if int(distancia(x+1, y+1))!=-1: #Sólo si es alcanzable
                dist[x][y] = int(distancia(x+1, y+1)) #+1 porque no existe el nodo 0
    #La distancia de cada aeropuerto a sí mismo es cero
    for x in range(v):
        dist[x][x] = 0
    #Algoritmo principal
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Testing
grafo = Graph()
grafo.crearGrafoCero()
FW = FloydWarshall(grafo)
for x in FW:
    print(x)
