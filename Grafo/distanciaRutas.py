#############################################################################################
#							     Datos de distanciaRutas.py									#
#																							#
#############################################################################################
# - Autores: Gonzalo Grisafi, Agustin Clemente												#
#############################################################################################
# - Funcionalidad: permite calcular las distancias entre dos aeropuertos, realizando 		#
# determinadas operaciones matermaticas.													#
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES 				#
#############################################################################################

from math import cos,radians,sin,pow,asin,sqrt
import csv
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def distancia(id1, id2):
	"""
		-Funcionamiento: Esta funcion se encarga de calcular la distancia entre dos aeropuertos
		-Precondiciones: Recibe como parametros dos ID de aeropuertos
		-Postcondiciones: Calcula con ciertas operaciones matematicas la distancia y la devuelve
	"""
	radio = 6371 # Este es el radio de la Tierra

	ruta_archivo = buscarArchivo("AeropuertosArg.csv") 
	with open(ruta_archivo) as archivo_csv:
		leer = csv.reader(archivo_csv)
		encontro = False
		encontro2 = False
		for linea in leer:
			if float(linea[0]) == id1:
				lat1 = float(linea[4])
				long1 = float(linea[5])
				encontro = True
			if float(linea[0]) == id2:
				lat2 = float(linea[4])
				long2 = float(linea[5])
				encontro2 = True
		#Si los ID no existen
		if not encontro or not encontro2:
			return -1

	lat1 = radians(lat1)
	lat2 = radians(lat2)
	long1 = radians(long1)
	long2 = radians(long2)

	dlat = lat2-lat1
	dlon = long2-long1

	a = pow(sin(dlat/2),2) + cos(lat1)*cos(lat2)*pow(sin(dlon/2),2)
	dist = 2 * radio * asin(sqrt(a))
	return dist

# Testing
# print(distancia(8,20))
# Debe imprimir 821.0526371448975
