#############################################################################################
#							     Datos de complejidades.py									#
#																							#
#############################################################################################
# - Autor: Emiliano Calvacho																#
#############################################################################################
# - Funcionalidad: muestra las complejidades de los algoritmos utilizados					#
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES 				#
#############################################################################################

def complejidades(opc):
	"""
		Funcionamiento: muestra complejidades
		Precondicion: recibe una opcion
		Postcondicion: no devuelve nada
	"""
	print("La complejidad del ",end="") 
	if opc == 1:
		print("Recorrido BFS es O(V+E)")
	if opc == 2:
		print("Recorrido DFS es O(V+E) ")
	if opc == 3:
		print("Algoritmo DIJKSTRA es O((E+V) * log V)")
	if opc == 4:
		print("Algoritmo FLOYD-WARSHALL es O(V^3)")
	if opc == 5:
		print("Algoritmo DETECTAR CICLOS es O(V)")

# Testing
# complejidadesAlg(1)
