def complejidadesAlg(opc):
	print("La complejidad del ",end="") 
	if opc == 1:
		print("Recorrido BFS es O(V+E)")
	if opc == 2:
		print("Recorrido DFS es O(V+E) ")
	if opc == 3:
		print("Algoritmo DIJKSTRA es O((E+V) * log V)")
	if opc == 5:
		print("Algoritmo FLOYD-WARSHALL es O(V^3)")
	if opc == 6:
		print("Algoritmo DETECTAR CICLOS es O(V)")

# complejidadesAlg(1)
