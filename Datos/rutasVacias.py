"""rutasVacias es un script que crea un archivo csv de rutas vacio,
esto se hace para asegurar que el archivo se cree en el directorio
Datos, sino se hace esto el archivo se crea en el directorio el cual 
se quiera trabajar desorganizando la estructura del proyecto.
Utiliza la libreria csv para manejar dichos archivos."""

import csv

def rutasVacias():
	"""
		Funcionamiento: crea un archivo vacio de RutasAleatorias
		Precondicion: no recibe parametros
		Postcondicion: no devuelve nada
	"""
	ruta_archivo = "RutasAeropuertos.csv"
	f = open (ruta_archivo,'w')
	f.close()

#rutasVacias()

		
