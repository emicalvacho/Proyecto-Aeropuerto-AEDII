#############################################################################################
#							   Datos de rutasAleatorias.py									#
#																							#
#############################################################################################
# - Autor: Emiliano Calvacho																#
#############################################################################################
# - Funcionalidad: crea un archivo con las rutas disponibles según la temporada que el 		#
# usuario ingrese y las respectivas distancias entre dichas rutas.							#
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES 				#
#############################################################################################

import csv
import random
import pandas as pd
import sys
import os
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo
from Grafo.distanciaRutas import distancia

def list_ID_aeropuertos():
	"""
		Funcionamiento: se crea una lista con la identificación y coordenadas de los aeropuertos
		Precondiciones: no recibe parametros
		Postcondiciones: devuelve una lista de las ID y coordenadas de los aeropuertos
	"""
	# Cambiar la ruta segun donde se lo guarde
	ruta_archivo = buscarArchivo("AeropuertosArg.csv")
	with open(ruta_archivo) as archivo_csv:
		leer = csv.reader(archivo_csv)

		list_ID = []

		for linea in leer:
			ID = linea[0]
			latitud = float(linea[4])
			longitud = float(linea[5])
			list_ID.append((ID,latitud,longitud))

	return list_ID

def ruteoAleatorio(opc):
	"""
		Funcionamiento: crea un archivo csv con las rutas dispobibles aleatoriamente
		Precondiciones: no recibe parametros
		Postcondiciones: no devuelve nada
	"""
	temporada = opc
	lista_ID = list_ID_aeropuertos()

	# Calculo la cantidad de aristas o rutas
	# Maximo de rutas: [v*(v-1)]/2, donde v son la cantidad de vertices, o sea la
	# longitud de lista_ID. Pero como maximo solo dejamos hasta 35 rutas.
	# Minimo de rutas: las que se desee. Pero vamos a poner hasta 20 rutas
	cant_aristas=1
	if temporada == 1: # Verano
		cant_aristas = random.randrange(30,36)
	elif temporada == 2: # Otoño
		cant_aristas = random.randrange(20,21)
	elif temporada == 3: # Invierno
		cant_aristas = random.randrange(20,26)
	elif temporada == 4: # Primavera
		cant_aristas = random.randrange(20,31)

	# Se buscan dos vértices aleatorios distintos y se los agrega en forma
	# de tuplas a una lista de rutas. Esto se hace hasta que el contador
	# llegue a la cantidad de aristas que se desea.
	cont = 0
	lista_rutas = []
	while (cont < cant_aristas):
		r1 = random.choice(lista_ID)
		r2 = random.choice(lista_ID)
		if (r1 != r2):
			dist = round(distancia(float(r1[0]),float(r2[0])),2)
			t1 = (r1[0],r2[0],dist)
			t2 = (r2[0],r1[0],dist)
			if ((t1 not in lista_rutas) and (t2 not in lista_rutas)):
				lista_rutas.append(t1)
				cont += 1

	# Creo el archivo de las rutas de los aeropuertos
	# ruta_archivo = buscarArchivo("RutasAeropuertos.csv")

	df=pd.DataFrame(lista_rutas)
	dir=os.getcwd()
	dir+="\\Datos\\RutasAeropuertos.csv"
	df.to_csv(dir,index=False,header=False)
