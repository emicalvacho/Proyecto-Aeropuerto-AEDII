"""geo_distance Es el script que me permite calcular las distancias entre dos aeropuertos,
utilizando la libreria math de Python para realizar determinadas operaciones matermaticas."""

from math import cos,radians,sin,pow,asin,sqrt

def distancia(lat1, long1, lat2, long2):
	"""	
		-Funcionamiento: Esta funcion se encarga de calcular la distancia entre dos aeropuertos
		-Precondiciones: Recibe como parametros las latitudes y longitudes de los aeropuertos
		-Postcondiciones: Calcula con ciertas operaciones matematicas la distancia y la devuelve
	"""
	radio = 6371 # Este es el radio de la Tierra

	lat1 = radians(lat1)
	lat2 = radians(lat2)
	long1 = radians(long1)
	long2 = radians(long2)

	dlat = lat2-lat1
	dlon = long2-long1

	a = pow(sin(dlat/2),2) + cos(lat1)*cos(lat2)*pow(sin(dlon/2),2)
	dist = 2 * radio * asin(sqrt(a))
	return dist
