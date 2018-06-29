import csv 
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def mostrarDatos():
	ruta_archivo = buscarArchivo("AeropuertosArg.csv")
	with open(ruta_archivo) as archivoAeropuertos:
		leer_archivo = csv.reader(archivoAeropuertos)
		print("╔════╦══════════════════════════════════════════════════╦═════════════════════════════════════╦══════════════════╗")
		print("║",("ID").rjust(2),"║",("Aeropuertos").center(48),"║",("Ciudades").center(35),"║",("Provincias").center(16),"║")
		print("╠════╬══════════════════════════════════════════════════╬═════════════════════════════════════╬══════════════════╣")
		for fila in leer_archivo:
			nombre = fila[1][11:]
			print("║",fila[0].rjust(2),"║",nombre.center(48),"║",fila[2].center(35),"║",fila[3].center(16),"║")
		print("╚════╩══════════════════════════════════════════════════╩═════════════════════════════════════╩══════════════════╝")

# Testing
# mostrarDatos()
