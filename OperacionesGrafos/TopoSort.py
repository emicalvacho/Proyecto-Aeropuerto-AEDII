#############################################################################################
#                                   Datos de TopoSort.py                                    #
#                                                                                           #
#############################################################################################
# - Autores: Jose Guareschi                                                                 #
#############################################################################################
# - Funcionalidad: realiza el ordenamiento topologico de un grafo forzado, osea inventado,  #
# para poder ver bien la funcionalidad del algoritmo en el mismo. Esto se debe porque el    # 
# TopoSort es para un grafo dirgido pero en nuestro proyecto tratamos un grafo no dirgido.  #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import os
import csv
import random
import sys
import pprint

def dfs_topsort(graph):         
    L = []                     
    color = { u : "white" for u in graph }
    found_cycle = [False]
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break
 
    if found_cycle[0]:           
        L = []                
 
    L.reverse()           
    return L                  
 
def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "gray":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = "black"   
    L.append(u)             

def mostrarTopoSort():
    graph_tasks = { "Aeroparque Jorge Newbery" : ["Aeropuerto Internacional Ministro Pistarini"],
                      "Aeropuerto Internacional de Puerto Iguazu" : ["Aeropuerto Internacional Ministro Pistarini"],
                      "Aeropuerto Internacional Ministro Pistarini" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella"],
                      "Aeropuerto Tartagal" : ["Aeropuerto Internacional Ingeniero Ambrosio Taravella","Aeropuerto Almirante Marcos A. Zar"],
                      "Aeropuerto Internacional Ingeniero Ambrosio Taravella" : ["Aeropuerto Almirante Marcos A. Zar"],
                      "Aeropuerto Almirante Marcos A. Zar" : [] }

    print("Lista de algunos aeropuertos para aplicarle toposort")
    for key in graph_tasks:
        print(key,"->",graph_tasks[key])
    print()
    print("Ordenamiento topologico de los aeropuertos")
    order = dfs_topsort(graph_tasks)
    i=0
    for task in order:
        i+=1
        print(i,".-",task)

# Testing
# mostrarTopoSort()
