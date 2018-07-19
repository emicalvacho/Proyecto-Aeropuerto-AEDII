Este script debe utilizarse para evitar tener que cambiar las rutas de los archivos cada vez que se mueve el proyecto.
La forma de utilizarlo es:
1-Primero importan la libreria sys.
2-Luego llaman a la siguiente funcion de sys para poder manejarse con los '..'
3-Importan desde la rusta correspondiente a este script.
4-Finalmente lo utilizan poniendo el nombre del archivo que se quiere buscar en sus parametros.

Ejemplo:
	import sys
	sys.path.append("..")
	from BuscadorPath.buscarArchivo import buscarArchivo
	ruta_archivo = buscarArchivo("AeropuertosArg.csv")