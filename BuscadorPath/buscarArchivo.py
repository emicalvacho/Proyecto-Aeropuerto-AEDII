"""buscarArchivo es un script que se ocupa de alamacenar la ruta del archivo a tratar
Utiliza la libreria os y pathlib para poder manejarse con los archivos y rutas."""

import os
from pathlib import Path

def buscarArchivo(archivo):
	"""
		Funcionamiento: se ocupa de convertir las rutas en string y devolverlas para 
		facilitar el manejo de los archivos y no tener que cambiar los directorios
		constantemente
		Precondicion: recibe el nombre del archivo
		Postcondicion: devuleve la ruta del archivo
	"""
	p=Path(os.getcwd())
	for path,carpetas, archivos in os.walk(p.parent): 
		for nombre in archivos:                         
			if nombre == archivo:
				return (os.path.abspath(os.path.join(path, nombre)))
	
# Testing
# print(buscarArchivo("AeropuertosArg.csv"))
# Esto devuelven  por ejemplo: D:\Archivos de Gonzalo\Proyecto AED II\AeropuertosArg.csv 
