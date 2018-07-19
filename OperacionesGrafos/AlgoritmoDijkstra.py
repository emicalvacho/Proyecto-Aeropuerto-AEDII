#############################################################################################
#                           Datos de AlgoritmoDijkstra.py                                   #
#                                                                                           #
#############################################################################################
# - Autor: Javier Figueroa                                                                  #
#############################################################################################
# - Funcionalidad: es un algoritmo para la determinación del camino más corto, dado un      #
# vértice origen hacia el resto de los vértices en un grafo que tiene pesos en cada arista. #
#############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                 #
#############################################################################################

import sys
import heapq

import Queue as queue

def Dijkstra(aGraph,start):
    pq=PriorytyQueue()
    start.setdistance(a)
    pq.buildHeap([(v.getdistance(),v)for v in aGraph])
    while not pq is empty():
        currentvert=pq.delMin()
        for nextvert in currentvert.getconections():
            newdist=currentvert.getdistance+currentvert.getweight(nextvert)
            if newdist<nextvert.getdistance():
                nextvert.setdistance(newdist)
                nextvert.setpred(currentvert)
                pq.decreasekey(nextvert,newdist)
                

def heapsort(iterable):
    h=[]
    for value in iterable:
        heapush(h,value)
    return [heapop(h)for i in range (len(h))]


# Testing
"""
g={	'a' : ['d'],
    'b' : ['c'],
    'c' : ['b','d','e'],
    'd' : ['a','c'],
    'e' : ['c'],
    'f' : []
}
"""

