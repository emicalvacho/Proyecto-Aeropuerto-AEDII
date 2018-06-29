
import csv
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo
from MostrarGrafo.mostrarAeropuertos import listaAero

def mostrarDistancias():
	ruta_archivo = buscarArchivo("RutasAeropuertos.csv")
	with open(ruta_archivo) as archivo_rutas:
		leer_arc = csv.reader(archivo_rutas)
		lista_rutas = []
		for fila in leer_arc:
			r1 = int(fila[0])
			r2 = int(fila[1])
			dist = float(fila[2])
			lista_rutas += [(r1,r2,dist)]
			# print("»»» Del",r1,"al",r2,"hay",dist, "km «««")
			# print("════════════════════════════════════════════════════════")

	# print(listaAero())

	lista_aeropuertos = listaAero()
	
	for i in range(len(lista_rutas)):
		for x in range(len(lista_aeropuertos)):
			if lista_aeropuertos[x][0] == lista_rutas[i][0]:
				print(str(i+1).ljust(2),"# Del",lista_aeropuertos[x][1])
				break
		for y in range(len(lista_aeropuertos)):
			if lista_aeropuertos[y][0] == lista_rutas[i][1]:
				print("      al",lista_aeropuertos[y][1])
				break
		print("     hay",lista_rutas[i][2],"Km.")
		print("═══════════════════════════════════════════════════════════════════════════════════════════════════")

# Testing
# mostrarDistancias()
