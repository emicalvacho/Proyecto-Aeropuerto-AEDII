#############################################################################################
#                              Datos de RecorridoDFS.py                                     #
#                                                                                           #
#############################################################################################
# - Autor: Jose Rodriguez                                                                   #
#############################################################################################
# - Funcionalidad: realiza el recorrido en profundidad del grafo de aeropuertos             #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import os
import sys

def DFS(origen,grafo):
    """
        Funcionamiento: realiza el recorrido en profundidad del grafo de aeropuertos        
        Precondicion: recibe un origen y un grafo
        Postcondicion: no devuelve nada
    """	
    visitados = []
    pila = []
    print("\nLista de recorrido en profundidad\n")
    pila.append(origen)
    while pila:
        actual = pila.pop()
        if actual not in visitados:
        	print(actual,"-> ",end="")
        	visitados.append(actual)
        s = actual
        for key in grafo[s]:
             if key not in visitados:
                    pila.append(key)
    print()

# Testing
# origen = 1
# DFS(origen,grafo)
