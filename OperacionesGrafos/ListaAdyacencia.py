#############################################################################################
#                              Datos de ListaAdyacencia.py                                  #
#                                                                                           #
#############################################################################################
# - Autores: Emiliano Calvacho                                                              #
#############################################################################################
# - Funcionalidad: muestra de forma mas elegante la lista de adyacnetes                     #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

def ListaAdyacencia(grafo):
	"""
		Funcionalidad: muestra lista de adyacencia
		Precondiciones: recibe un grafo
		Postcondiciones: no devuelve nada
	"""
	for vertice in grafo:
		print("Nodo:",str(vertice).rjust(2),"- Adyacentes: [",end="")
		longitud = len(grafo[vertice])
		for i in range(longitud):
			print(str(grafo[vertice][i]).rjust(2),end="")
			if i != longitud-1:
				print(" --> ",end="")
		print("]")