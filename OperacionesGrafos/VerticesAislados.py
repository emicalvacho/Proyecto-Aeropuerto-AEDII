#############################################################################################
#                           Datos de VerticesAislados.py                                    #
#                                                                                           #
#############################################################################################
# - Autor: Emiliano Calvacho                                                                #
#############################################################################################
# - Funcionalidad: determina una lista de vertices aislados pero por medio de los indices   # 
# de los aeropuertos                                                                        #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

def VerticesAislados(grafo):
	"""
		Funcionalidad: crea una lista con los vertices aislados 
		Precondiciones: recibe un grafo
		Postcondiciones: devuelve una lista de los vertices aislados
	"""
	lista_aislados = []
	for v in grafo:
		if not grafo[v]:
			lista_aislados.append(v)
	return lista_aislados

# Testing
# g={	'a' : ['d'],
#     'b' : [],
#     'c' : ['b','d','e'],
#     'd' : ['a','c'],
#     'e' : ['c'],
#     'f' : []
# }
# print(VerticesAislados(g))