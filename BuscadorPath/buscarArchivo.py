#############################################################################################
#                                Datos de buscarArchivo.py                                  #
#                                                                                           #
#############################################################################################
# - Autor: Gonzalo Grisafi                                                                  #
#############################################################################################
# - Funcionalidad: se ocupa de almacenar la ruta del archivo a tratar                       #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

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
