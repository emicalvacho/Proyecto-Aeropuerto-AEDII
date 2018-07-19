#############################################################################################
#                              Datos de DetectarCiclos.py                                   #
#                                                                                           #
#############################################################################################
# - Autor: Jose Rodriguez                                                                   #
#############################################################################################
# - Funcionalidad: detecta si el grafo tiene ciclos o no                                    #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import os
import sys

def find_cycle(origen,grafo):
    existeCiclo = 0
    visitados = []
    pila = [(None,origen)]

    while pila:
        (prev, actual) = pila.pop()
        if actual not in visitados:
        	visitados.append(actual)
        for key in grafo[actual]:
            if key not in visitados:
                    pila.append((actual,key))
            elif key == prev:
                pass
            elif key in visitados:
                existeCiclo = 1
    if existeCiclo == 1:
        print("EXISTE CICLO")
    else:
        print("NO EXISTE CICLO")

def mostrarDectectorCiclos():
	print("EJEMPLO QUE DETECTA QUE NO HAY CICLO")
	print("------------------------------------")
	graph = { "Aeroparque Jorge Newbery" : ["Aeropuerto Internacional Ministro Pistarini"],
              "Aeropuerto Internacional de Puerto Iguazu" : ["Aeropuerto Internacional Ministro Pistarini"],
              "Aeropuerto Internacional Ministro Pistarini" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella"],
              "Aeropuerto Tartagal" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella","Aeropuerto Almirante Marcos A. Zar"],
              "Aeropuerto Internacional Ingeniero Ambrosio Taravella" : ["Aeropuerto Almirante Marcos A. Zar"],
              "Aeropuerto Almirante Marcos A. Zar" : [] }

	print("Lista de algunos aeropuertos para aplicarle detector de ciclos")
	for key in graph:
		print(key,"->",graph[key])
	print()
	print("Como origen tomamos al 'Aeroparque Jorge Newbery'")
	find_cycle("Aeroparque Jorge Newbery",graph)
	print("==============================================================================================")
	print("EJEMPLO QUE DETECTA QUE HAY CICLO")
	print("---------------------------------")
	graph = { "Aeroparque Jorge Newbery" : ["Aeropuerto Internacional Ministro Pistarini"],
          "Aeropuerto Internacional de Puerto Iguazu" : ["Aeropuerto Internacional Ministro Pistarini"],
          "Aeropuerto Internacional Ministro Pistarini" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella"],
          "Aeropuerto Tartagal" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella","Aeropuerto Almirante Marcos A. Zar"],
          "Aeropuerto Internacional Ingeniero Ambrosio Taravella" : ["Aeropuerto Almirante Marcos A. Zar","Aeropuerto Internacional de Puerto Iguazu"],
          "Aeropuerto Almirante Marcos A. Zar" : [] }

	print("Lista de algunos aeropuertos para aplicarle detector de ciclos")
	for key in graph:
		print(key,"->",graph[key])
	print()
	print("Como origen tomamos al 'Aeroparque Jorge Newbery'")
	find_cycle("Aeroparque Jorge Newbery",graph)

# Testing
# mostrarDectectorCiclos()
