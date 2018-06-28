import os
import sys
import msvcrt as m
def wait():
    m.getch()
from Grafo.crearDicGrafo import Graph
from Grafo.distanciaRutas import distancia
from OperacionesGrafos.RecorridoBFS import BFS

def MP():
    os.system('cls')
    print("╔═════════════════════════════╗")
    print("║        MENÚ PRINCIPAL       ║")
    print("╠═════════════════════════════╣")
    print("║   1. IMPRIMIR GRAFO         ║")
    print("║   2. IMPRIMIR RUTAS         ║")
    print("║   3. DATOS DE AEROPUERTOS   ║")
    print("║   4. SALIR                  ║")
    print("╚═════════════════════════════╝")
    try:
        return int(input("Su opción: "))
    except:
        print("Opcion no válida.")
        wait()
        return -1

def Recorridos(grafo):
    while(True):
        os.system('cls')
        print("╔═════════════════════════════╗")
        print("║     RECORRIDOS DEL GRAFO    ║")
        print("╠═════════════════════════════╣")
        print("║   1. EN PRODUNFIDAD         ║")
        print("║   2. EN ANCHURA             ║")
        print("║   3. ATRÁS                  ║")
        print("╚═════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>3 or opc<1:
            print("Opcion no válida.")
            wait()
            continue
        if opc == 3:
            break
        if opc == 1:
            i=0
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


#MAIN
dic = Graph()
dic.crearGrafoCero()
grafo = dic.getGrafo()
opc = 0
while opc!=4:
    opc = MP()
    if (opc>4 or opc<1) and opc!=-1: #Al retornar -1 indica que el user no ingresó int
        print("Opcion no válida.")   # No entra porque ya lo regañó la función
        wait()
        continue
    if opc == 1:
        Recorridos(grafo)

os.system('cls')
