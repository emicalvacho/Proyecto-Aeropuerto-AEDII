import sys
sys.path.insert(0, 'C:\\Users\\Tino\\Desktop\\Facultad\\Algoritmos y estructuras de datos 2\\PROYECTO FINAL\\Grafo')
from crearDicGrafo import Graph
from distanciaRutas import distancia

"""
    Floyd-Warshall crea la matriz de cierre transitivo del grafo dado.
    Utiliza la función distancia para crear la matriz de distancias.
"""

def FloydWarshall(grafo):

    """
		Precondiciones: un grafo de la clase Graph
		Postcondiciones: devuelve la matriz de cierre transitivo del grafo
	"""

    #Creo la matriz de Nro.vertices x Nro.vertices
    v = len(grafo.vertices())
    dist = [[0 for y in range(v)] for y in range(v)]
    #Lleno la matriz con las distancias
    for x in range(v):
        for y in range(v):
            dist[x][y] = distancia(x, y)
    #Algoritmo principal
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

#PRUEBA
#grafo = Graph()
#grafo.crearGrafoCero()
#FW = FloydWarshall(grafo)
#for x in FW:
#    print(x)
