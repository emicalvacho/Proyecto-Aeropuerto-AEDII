"""geo_distance Es el script que me permite calcular las distancias entre dos aeropuertos,
utilizando la libreria math de Python para realizar determinadas operaciones matermaticas
y la libreria csv para abrir la lista de aeropuertos."""

from math import cos,radians,sin,pow,asin,sqrt
import csv

def distancia(id1, id2):
	"""
		-Funcionamiento: Esta funcion se encarga de calcular la distancia entre dos aeropuertos
		-Precondiciones: Recibe como parametros dos ID de aeropuertos
		-Postcondiciones: Calcula con ciertas operaciones matematicas la distancia y la devuelve
	"""
	radio = 6371 # Este es el radio de la Tierra

	ruta_archivo = "C:\\Users\\Tino\\Desktop\\Facultad\\Algoritmos y estructuras de datos 2\\PROYECTO FINAL\\Datos\\AeropuertosArg.csv"
	with open(ruta_archivo) as archivo_csv:
		leer = csv.reader(archivo_csv)
		encontro = False
		encontro2 = False
		for linea in leer:
			if linea[0] == id1:
				lat1 = float(linea[4])
				long1 = float(linea[5])
				encontro = True
			if linea[0] == id2:
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

# # Testing
#print(distancia(8,20))
