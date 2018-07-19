#############################################################################################
#                              Datos de mostrarAeropuertos.py                               #
#                                                                                           #
#############################################################################################
# - Autor: Emiliano Calvacho                                                                #
#############################################################################################
# - Funcionalidad: muestra la lista de adyacencia de cada aeropuerto pero con los nombres,  #
# viendo cuales son los destinos disponibles.                                               #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import sys
import os
import csv
sys.path.append("..")
from Grafo.crearDicGrafo import Graph
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def listaAero():
	"""
		Funcionamiento: crea una lista de tuplas con (id,nombreAeropuerto)
		Precondicion: no recibe nada
		Postcondicion: devuelve lista de tuplas con la informacion necesaria
	"""
	# Leyendo el archivo de aeropuertos
	ruta_archivo = buscarArchivo("AeropuertosArg.csv")
	with open(ruta_archivo) as archivo_aero:
		leer_aero = csv.reader(archivo_aero)
		lista_aeropuertos = []
		for fila in leer_aero:
			indice = int(fila[0])
			nombreAero = fila[1]
			lista_aeropuertos += [(indice,nombreAero)]
	return lista_aeropuertos

def mostrarAeropuertos(grafo):
	"""
		Funcionamiento: imprime lista de adyacencia pero con nombres
		Precondicion: recibe un grafo
		Postcondicion: no devuelve nada
	"""

	lista_aeropuertos = listaAero()
	
	for i in range(len(lista_aeropuertos)): # Se itera toda la lista de aeropuertos
		
		# Imprimo el vertice correspondiente del grafo
		print()
		print("╔═══════════════════════════════════════════════════════════════════════════╗")	
		print("║",str(lista_aeropuertos[i][0]).ljust(3),"#", lista_aeropuertos[i][1].ljust(65),"  ║") 
		print("╠═══════════════════════════════════════════════════════════════════════════╣")
		
		vertice = lista_aeropuertos[i][0] # Identifico la ID de la lista
		lista_ady = grafo[vertice] # Creo la lista de adyacencia de ese ID
		if lista_ady: # Si la lista_ady no esta vacia imprimo los destinos
			print("║ Tiene disponible los siguientes destinos: ".ljust(72),"   ║")

			for item in lista_ady:
				for j in range(len(lista_aeropuertos)): # Vuelvo a iterar lista de aeropuertos
					if item == lista_aeropuertos[j][0]: # Identifico el aeropuerto
						print("║  -",lista_aeropuertos[j][1].ljust(65),"     ║") # Imprimo su nombre
						break
		else: # Si la lista_ady esta vacia envio un mensaje
			print("║ No hay destinos diponibles".ljust(72),"   ║")

		print("╚═══════════════════════════════════════════════════════════════════════════╝")	

# Testing	
# grafo_obj = Graph()
# grafo_obj.crearGrafoCero()
# graph = grafo_obj.getGrafo()
# mostrarAeropuertos(graph)
