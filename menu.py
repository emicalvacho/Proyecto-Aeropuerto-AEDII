#############################################################################################
#									Datos de menu.py										#
#																							#
#############################################################################################
# - Autores: Agustin Clemente, Emiliano Calvacho											#
#############################################################################################
# - Funcionalidad: muestra todas las opciones disponibles para el programa de aeorpuertos,	#
# basado en los algoritmos y funciones vistas en la materia de Algoritmo y Estructura de 	#
# de Datos II, refiriendose al tema de GRAFOS 												#
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES 				#
#############################################################################################

import os
import sys
import pprint
from Grafo.crearDicGrafo import Graph
from Grafo.distanciaRutas import distancia
from Grafo.rutasAleatorias import ruteoAleatorio
from MostrarGrafo.mostrarDatos import mostrarDatos
from MostrarGrafo.mostrarAeropuertos import mostrarAeropuertos
from MostrarGrafo.mostrarDistancias import mostrarDistancias
from OperacionesGrafos.RecorridoBFS import BFS
from OperacionesGrafos.RecorridoDFS import DFS
from OperacionesGrafos.AlgoritmoFloydWarshall import FloydWarshall
from OperacionesGrafos.MatrizAdyacencia import matrizAdyacencia
from OperacionesGrafos.TopoSort import mostrarTopoSort
from Eficiencias.complejidades import complejidades
from Visualización.Mapas import MapaAeropuertos,MapaRutas

def wait():
	os.system("pause")

def MP():
	os.system('cls')
	print("╔═════════════════════════════════╗")
	print("║          MENÚ PRINCIPAL         ║")
	print("╠═════════════════════════════════╣")
	print("║   1. ELEGIR ESTACION DEL AÑO    ║")
	print("║   2. INFO. DE LOS AEROPUERTOS   ║")
	print("║   3. RECORRIDOS DEL GRAFO       ║")
	print("║   4. OPERACIONES DEL GRAFO      ║")
	print("║   5. VISUALIZACIÓN EN MAPA      ║")
	print("║   6. COMPLEJIDADES DE LOS ALG.  ║")
	print("║   7. SALIR                      ║")
	print("╚═════════════════════════════════╝")
	try:
		return int(input("Su opción: "))
	except:
		print("Opcion no válida.")
		wait()
		return -1

def Recorridos(grafo):
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║       RECORRIDOS DEL GRAFO      ║")
		print("╠═════════════════════════════════╣")
		print("║   1. EN PRODUNFIDAD             ║")
		print("║   2. EN ANCHURA                 ║")
		print("║   3. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>3 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 3: #Salir
			break
		if opc == 1:
			opc2=0
			while opc2<1 or opc2>25:
				try:
					opc2 = int(input("¿Desde qué nodo desea comenzar? (1-25) -> "))
				except:
					print("Opcion no válida.") #Si no ingreso un int
					wait()
					break
				if opc2<1 or opc2>25:
					print("Opcion no válida.") # Si ingreso un nodo invalido
					wait()
					break
				DFS(opc2, grafo)
				wait()
		if opc == 2:
			opc2=0
			while opc2<1 or opc2>25:
				try:
					opc2 = int(input("¿Desde qué nodo desea comenzar? (1-25) -> "))
				except:
					print("Opcion no válida.") #Si no ingreso un int
					wait()
					break
				if opc2<1 or opc2>25:
					print("Opcion no válida.") # Si ingreso un nodo invalido
					wait()
					break
				BFS(opc2, grafo)
				wait()

def Estacion():
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║     SELECCIÓN DE TEMPORADA      ║")
		print("╠═════════════════════════════════╣")
		print("║   1. VERANO                     ║")
		print("║   2. OTOÑO                      ║")
		print("║   3. INVIERNO                   ║")
		print("║   4. PRIMAVERA                  ║")
		print("║   5. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>5 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 5: #Salir
			break
		ruteoAleatorio(opc)
		if opc==1:
			print("Rutas listas para la estación verano.")
		if opc==2:
			print("Rutas listas para la estación otoño.")
		if opc==3:
			print("Rutas listas para la estación invierno.")
		if opc==4:
			print("Rutas listas para la estación primavera.")
		wait()
		break

def InfoAeropuertos(grafo):
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║   INFORMACIÓN DE AEROPUERTOS    ║")
		print("╠═════════════════════════════════╣")
		print("║   1. DATOS DE AEROPUERTOS       ║")
		print("║   2. RUTAS ENTRE AEROPUERTOS    ║")
		print("║   3. DISTANCIAS DE LAS RUTAS    ║")
		print("║   4. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>4 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 4: #Salir
			break
		if opc == 1:
			mostrarDatos()
		if opc == 2:
			mostrarAeropuertos(grafo)
		if opc == 3:  
			mostrarDistancias()
		wait()		

def Operaciones(dic):
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║      OPERACIONES DEL GRAFO      ║")
		print("╠═════════════════════════════════╣")
		print("║   1. ALGORITMO DE DIJKSTRA      ║")
		print("║   2. ALG. DE FLOYD-WARSHALL     ║")
		print("║   3. TOPOSORT                   ║")
		print("║   4. VER VÉRTICES AISLADOS      ║")
		print("║   5. VER MATRIZ DE ADYACENCIA   ║")
		print("║   6. VER LISTA DE ADYACENCIA    ║")
		print("║   7. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>7 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 7: #Salir
			break
		if opc == 2:
			print("Matriz de cierre transitivo: \n")
			CT = FloydWarshall(dic)
			for x in CT:
				print(x)
		if opc == 3:
			print("Ordenamiento topologico: \n")
			mostrarTopoSort()
		if opc == 5:
			print("Matriz de adyacencia: \n")
			for x in matrizAdyacencia(dic): #Le paso el grafo entero
				print(x)
		if opc == 6:
			print("Lista de adyacencia: \n")
			pprint.pprint(dic.getGrafo())
		wait()

def Visualizar():
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║      VISUALIZACIÓN EN MAPA      ║")
		print("╠═════════════════════════════════╣")
		print("║   1. VISUALIZAR AEROPUERTOS     ║")
		print("║   2. VISUALIZAR RUTAS           ║")
		print("║   3. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>3 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 3: #Salir
			break
		if opc == 1:
			MapaAeropuertos()
		if opc == 2:
			MapaRutas()
		wait()

def Complejidades():
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║ COMPLEJIDADES DE LOS ALGORITMOS ║")
		print("╠═════════════════════════════════╣")
		print("║   1. BFS                        ║")
		print("║   2. DFS                        ║")
		print("║   3. DIJKSTRA                   ║")
		print("║   4. FLOYD-WARSHALL             ║")
		print("║   5. TOPOSORT                   ║")
		print("║   6. ATRÁS                      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>6 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 6: #Salir
			break
		complejidades(opc)	
		wait()

def Eliminacion():
	while(True):
		os.system('cls')
		print("╔═════════════════════════════════╗")
		print("║         ELIMINAR DATOS          ║")
		print("╠═════════════════════════════════╣")
		print("║   1. QUIERO ELIMINAR DATOS      ║")
		print("║   2. QUIERO MANTENER DATOS      ║")
		print("╚═════════════════════════════════╝")
		try:
			opc = int(input("Su opción: "))
		except:
			print("Opcion no válida.")
			wait()
		if opc>2 or opc<1: #Límites
			print("Opcion no válida.")
			wait()
			continue
		if opc == 1:
			# Elimino automaticamente los archivos creados
			try:
				os.remove("Datos\\RutasAeropuertos.csv")
				os.remove("Visualización\\MapaAeropuertos.html")
				os.remove("Visualización\\MapaRutas.html")
			except Exception as error:
				print("Se encontro el siguiente error: ")
				print(error)
				print()
			wait()
			break
		if opc == 2:			
			wait()
			break

# MAIN
def main():
	#Operaciones iniciales obligatorias
	# Crea las rutas aleatorias con estacion por defecto
	ruteoAleatorio(1) #la mejor estación
	# Instancia un objeto como grafo
	dic = Graph()
	# Crea el grafo ya con los archivos listos
	dic.crearGrafoCero()
	# Se obtiene el grafo y se lo guarda en un auxiliar
	grafo = dic.getGrafo()
	opc = 0
	while opc!=7:
		opc = MP()
		if (opc>7 or opc<1) and opc!=-1: #Al retornar -1 indica que el user no ingresó int
			print("Opcion no válida.")   # No entra porque ya lo regañó la función
			wait()
			continue
		if opc == 1:
			Estacion()
		if opc == 2:
			InfoAeropuertos(grafo)
		if opc == 3:
			Recorridos(grafo)
		if opc == 4:
			Operaciones(dic)
		if opc == 5:
			Visualizar()
		if opc == 6:
			Complejidades()
		if opc == 7:
			Eliminacion()
	os.system('cls')

	print("╔══════════════════════════════════════╗")
	print("║ Gracias por usar nuestro programa :) ║")
	print("╠══════════════════════════╦═══════════╝")
	print("║ Proyecto realizado por:  ║")
	print("║ - Gonzalo Grisafi        ║")
	print("║ - Agustin Clemente       ║")
	print("║ - Emiliano Calvacho      ║")
	print("║ - Jose Guareschi         ║")
	print("║ - Jose Rodriguez         ║")
	print("║ - Javier Figueroa        ║")
	print("╠══════════════════════════╩═══════════════════════════════════════════════╗")
	print("║ Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES  ║")
	print("╠════════════════════════════════════════════╦═════════════════════════════╝")
	print("║ Materia: Algoritmos y Estructuras de Datos ║")
	print("╠══════════════════════════════╦═════════════╝")
	print("║ Docente: Lic. Virginia More  ║")
	print("╚══════════════════════════════╝")
	
main()
