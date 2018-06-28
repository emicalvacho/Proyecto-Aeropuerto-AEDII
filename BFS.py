import os

import crearDicGrafo
dicc = crearDicGrafo.Graph()
dicc.crearGrafoCero()
grafo = dicc.getGrafo()

#DEFINIENDO EL GRAFO MEDIANTE UN DICCIONARIO DE PYTHON:
#PARA MEJOR COMPRENSION EL VALOR 'a': [('p',4), ('j',15), ('b',1)],
#INDICA QUE EL VERTICE 'a' ES ADYACENTE CON 'P', CON 'J' Y CON 'b' 
#CADA UNO CON SU RESPECTIVO PESO, AUNQUE EL PESO PARA HACER RECCORRIDOS EN PROFUNDIDAD
#NO ES NECESARIO, SE LO AGREGUE PARA MOSTRAR TAMBIEN LA IMPLEMENTACION DE UN GRAFO PONDERADO

"""grafo = {'a': [('p',4), ('j',15), ('b',1)],
         	'b': [('a',1), ('d',2), ('e',2), ('c',3)],
			'j': [('a',15)],
			'p': [('a', 4)],
			'd': [('b',2), ('g',3)],
			'e': [('b',2), ('g',4), ('f',5), ('c',2)],
			'c': [('b',3), ('e',2), ('f',5), ('i',20)],
			'g': [('d',3), ('e',4), ('f',10), ('h',1)],
			'f': [('g',10), ('e',5), ('c',5)],
			'i': [('c',20)],
			'h': [('g',1)] 
		}"""
def BFS(origen,grafo):
        #MUESTRA EL GRAFO ANTES DEL RECORRIDO
        print("Muestra el grafo antes del recorrido: \n")
        for key, lista in grafo.items():
                print(key)
                print(lista)

        print()
        os.system("pause")
                        
        visitados = []
        cola = []

        origen = input("Ingresa el nodo origen: ")
        print("\nLista de recorrido en anchura\n")
        #Paso 1: SE COLOCA EL VERTICE ORIGEN EN UNA COLA
        cola.append(origen)
        #Paso 2: MIENTRAS LA COLA NO ESTE VACIA
        while cola:
                #paso 3: DESENCOLAR UN VERTICE, ESTE SERA AHORA EL VERTICE ACTUAL
                actual = cola.pop(0)

                #paso 4: SI EL VERTICE ACTUAL NO HA SIDO VISITADO
                if actual not in visitados:
                        #paso 5: PROCESAR (IMPRIMIR) EL VERTICE ACTUAL
                        print("Vertice actual -> ", actual)
                        #paso 6: COLOCAR VERTICE ACTUAL EN LA LISTA DE VISITADOS
                        visitados.append(actual)
                #paso 7: PARA CADA VERTICE QUE EL VERTICE ACTUAL TIENE COMO DESTINO,
                #        Y QUE NO HA SIDO VISITADO:
                #        ENCOLAR EL VERTICE
                S = str(actual)
                for key, lista in grafo[S]:
                        if key not in visitados: #SI NO FUE VISITADO
                                cola.append(key)

        print()
BFS(origen,grafo)
os.system("pause")
