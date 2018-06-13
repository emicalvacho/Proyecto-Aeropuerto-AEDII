"""rutasAleatorias crea un archivo con las rutas disponibles según la temporada que el usuario ingrese y las
respectivas distancias entre dichas rutas.
Se utiliza la librería csv para operar con este tipo de archivos, random para crear una aleatoridad de rutas
y el script de distanciasRutas para calcular la distancia entre las rutas."""

import csv
import random
from distanciaRutas import distancia
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def eleccion_temporada():
	"""
		Funcionamiento: el usuario ingresa una temporada
		Precondiciones: no recibe parametros
		Postcondiciones: devuelve la temporada elegida
	"""
	while True:
		print("Opciones de temporada:")
		print("1- Verano.\n2- Otoño.\n3- Invierno.\n4- Primavera.")
		temporada = int(input("Ingrese la temporada del año: "))
		if (temporada<1 or temporada>4):
			print("Por favor ingrese un temporada válido.")
		else:
			break

	return temporada

def list_ID_aeropuertos():
	"""
		Funcionamiento: se crea una lista con la identificación y coordenadas de los aeropuertos
		Precondiciones: no recibe parametros
		Postcondiciones: devuelve una lista de las ID y coordenadas de los aeropuertos
	"""
	# Cambiar la ruta segun donde se lo guarde
	# ruta_archivo = "C:\\Users\\Tino\\Desktop\\Facultad\\Algoritmos y estructuras de datos 2\\PROYECTO FINAL\\Datos\\AeropuertosArg.csv"
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

def ruteoAleatorio():
	"""
		Funcionamiento: crea un archivo csv con las rutas dispobibles aleatoriamente
		Precondiciones: no recibe parametros
		Postcondiciones: no devuelve nada
	"""
	temporada = eleccion_temporada()
	lista_ID = list_ID_aeropuertos()

	# Calculo la cantidad de aristas o rutas
	# Maximo de rutas: [v*(v-1)]/2, donde v son la cantidad de vertices, o sea la
	# longitud de lista_ID. Pero como maximo solo dejamos hasta 35 rutas.
	# Minimo de rutas: las que se desee. Pero vamos a poner hasta 20 rutas
	if temporada == 1: # Verano
		cant_aristas = random.randrange(20,36)
	elif temporada == 2: # Otoño
		cant_aristas = random.randrange(20,21)
	elif temporada == 3: # Invierno
		cant_aristas = random.randrange(20,26)
	elif temporada == 4: # Primavera
		cant_aristas = random.randrange(20,31)

	# print("\nCantidad de aristas: ",cant_aristas)

	# Se buscan dos vértices aleatorios distintos y se los agrega en forma
	# de tuplas a una lista de rutas. Esto se hace hasta que el contador
	# llegue a la cantidad de aristas que se desea.
	cont = 0
	lista_rutas = []
	while (cont < cant_aristas):
		r1 = random.choice(lista_ID)
		r2 = random.choice(lista_ID)
		if (r1 != r2):
			dist = distancia(r1[0],r2[0])
			t = (r1[0],r2[0],dist)
			if (t not in lista_rutas):
				lista_rutas.append(t)
				cont += 1

	# Verifico la lista_rutas
	# c=1
	# for item in lista_rutas:
	# 	print(c,item)
	# 	c +=1

	# Creo el archivo de las rutas de los aeropuertos
	# Cambiar la ruta segun donde se lo guarde
	# ruta_archivo = "C:\\Users\\Tino\\Desktop\\Facultad\\Algoritmos y estructuras de datos 2\\PROYECTO FINAL\\Datos\\RutasAeropuertos.csv"
	ruta_archivo = buscarArchivo("RutasAeropuertos.csv")
	with open(ruta_archivo,'w',newline = '') as archivo_rutas:
		escribir = csv.writer(archivo_rutas)
		escribir.writerows(lista_rutas)

# Testing (para probar script quiten el comentario de la implementacion)
ruteoAleatorio()
