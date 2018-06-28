"""crearDicGrafo es una clase que se ocupa de crear un grafo como diccionario desde los 
archivos CSV, además tiene la posibilidad de ver sus vertices y aristas.
Utiliza la libreria csv para trabajar con dichos archivos y pprint para debuggin.
Ademas utiliza el script de buscador de archivos para acortar rutas conjunto a la libreria sys"""

import csv
import pprint
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

class Graph (object):
	def __init__(self, graph_dict = {}):
		"""
			Funcionamiento: crea un grafo desde cero o tomar uno recibido
			Precondicion: recibe un grafo diccionario y sino lo crea por defecto.
			Postcondicion: crea una variable de la clase con ese diccionario vacio o recibido
		"""
		self._graph_dict = graph_dict

	def vertices(self):
		"""
			Funcionamiento: dar una lista de vertices del grafo
			Precondicion: no recibe parametros
			Postcondicion: devuelve lista de las claves del diccionario
		"""
		return list(self._graph_dict.keys())

	def edges(self):
		"""
			Funcionamiento: dar un conjunto de aristas del grafo
			Precondicion: no recibe parametros
			Postcondicion: devuelve conjunto de aristas
		"""
		return self._generate_edges()

	def _add_vertices(self):
		"""
			Funcionamiento: agrega los vertices al diccionario desde un archivo
			Precondicion: no recibe parametros
			Postcondicion: no devuelve nada
		"""
		ruta_archivo = buscarArchivo("AeropuertosArg.csv")
		with open(ruta_archivo) as archivo_vertices:
			leer_vertices = csv.reader(archivo_vertices)
			for fila_vert in leer_vertices:
				vert = int(fila_vert[0])
				if vert not in self._graph_dict:
					self._graph_dict[vert] = [] 

	def _add_edges(self):
		"""
			Funcionamiento: agrega las aristas al diccionario desde un archivo
			Precondicion: no recibe parametros
			Postcondicion: no devuelve nada
		"""
		ruta_archivo = buscarArchivo("RutasAeropuertos.csv")
		with open(ruta_archivo) as archivo_edges:
			leer_edges  = csv.reader(archivo_edges)
			for fila_edge in leer_edges:
				v1 = int(fila_edge[0])
				v2 = int(fila_edge[1])
				aux = (v1,v2)
				edge = set(aux)
				(vertex1,vertex2) = tuple(edge) 
				if vertex1 in self._graph_dict:
					if vertex2 not in self._graph_dict[vertex1]:
						self._graph_dict[vertex1].append(vertex2)
						self._graph_dict[vertex2].append(vertex1)
 
	def _generate_edges(self):
		"""
			Funcionamiento: genera las aristas para mostrarlas
			Precondicion: no recibe parametros
			Postcondicion: devuelve conjunto de aristas
		"""
		edges = []
		for vertex in self._graph_dict:
			for neighbour in self._graph_dict[vertex]:
				if{neighbour,vertex} not in edges:
					edges.append({vertex,neighbour})
		return edges

	def crearGrafoCero(self):
		"""
			Funcionamiento: crea un grafo desde los archivos
			Precondicion: no recibe parametros
			Postcondicion: no devuelve nada
		"""
		self._add_vertices()
		self._add_edges()

	def getGrafo(self):
		"""
			Funcionamiento: devuelve el grafo creado
			Precondicion: no recibe parametros
			Postcondicion: devuelve grafo-diccionario
		"""
		return self._graph_dict

# Testing 
# grafo = Graph()
# grafo.crearGrafoCero()
# # No se asusten que pprint lo imprime desordenado pero print normal no
# pprint.pprint(grafo.getGrafo())
# print(buscarArchivo("AeropuertosArg.csv"))