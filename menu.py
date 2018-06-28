import os
import sys
import msvcrt as m
def wait():
    m.getch()
from Datos.rutasVacias import rutasVacias
from Grafo.crearDicGrafo import Graph
from Grafo.distanciaRutas import distancia
from OperacionesGrafos.RecorridoBFS import BFS
from Grafo.rutasAleatorias import ruteoAleatorio
from OperacionesGrafos.MatrizAdyacencia import matrizAdyacencia

def MP():
    os.system('cls')
    print(grafo.keys())
    print(grafo[15])
    print(grafo[13])
    print(grafo[10])
    print(grafo[7])
    print("╔═════════════════════════════════╗")
    print("║          MENÚ PRINCIPAL         ║")
    print("╠═════════════════════════════════╣")
    print("║   1. ELEGIR ESTACION DEL AÑO    ║")
    print("║   2. INFO. DE LOS AEROPUERTOS   ║")
    print("║   3. RECORRIDOS DEL GRAFO       ║")
    print("║   4. OPERACIONES DEL GRAFO      ║")
    print("║   5. VISUALIZACIÓN EN MAPA      ║")
    print("║   6. COMPLEJIDADES DE LOS ALG.  ║")
    print("║   7. SALIR                      ║")
    print("╚═════════════════════════════════╝")
    try:
        return int(input("Su opción: "))
    except:
        print("Opcion no válida.")
        wait()
        return -1

def Recorridos(grafo):
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║       RECORRIDOS DEL GRAFO      ║")
        print("╠═════════════════════════════════╣")
        print("║   1. EN PRODUNFIDAD             ║")
        print("║   2. EN ANCHURA                 ║")
        print("║   3. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>3 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 3: #Salir
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

def Estacion():
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║     SELECCIÓN DE TEMPORADA      ║")
        print("╠═════════════════════════════════╣")
        print("║   1. VERANO                     ║")
        print("║   2. OTOÑO                      ║")
        print("║   3. INVIERNO                   ║")
        print("║   4. PRIMAVERA                  ║")
        print("║   5. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>5 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 5: #Salir
            break
        ruteoAleatorio(opc)
        if opc==1:
            print("Rutas listas para la estación verano.")
        if opc==2:
            print("Rutas listas para la estación otoño.")
        if opc==3:
            print("Rutas listas para la estación invierno.")
        if opc==4:
            print("Rutas listas para la estación primavera.")
        wait()
        break

def InfoAeropuertos():
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║   INFORMACIÓN DE AEROPUERTOS    ║")
        print("╠═════════════════════════════════╣")
        print("║   1. DATOS DE AEROPUERTOS       ║")
        print("║   2. RUTAS ENTRE AEROPUERTOS    ║")
        print("║   3. DISTANCIAS DE LAS RUTAS    ║")
        print("║   4. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>4 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 4: #Salir
            break
        wait()

def Operaciones():
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║      OPERACIONES DEL GRAFO      ║")
        print("╠═════════════════════════════════╣")
        print("║   1. ALGORITMO DE DIJKSTRA      ║")
        print("║   2. ALG. DE FLOYD-WARSHALL     ║")
        print("║   3. DETECTAR CICLOS            ║")
        print("║   4. VER VÉRTICES AISLADOS      ║")
        print("║   5. VER MATRIZ DE ADYACENCIA   ║")
        print("║   6. VER LISTA DE ADYACENCIA    ║")
        print("║   7. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>7 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 7: #Salir
            break
        if opc == 5:
            print("Matriz de adyacencia: \n")
            for x in (matrizAdyacencia(dic)): #Le paso el grafo entero
                print(x)
        wait()

def Visualizar():
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║      VISUALIZACIÓN EN MAPA      ║")
        print("╠═════════════════════════════════╣")
        print("║   1. VISUALIZAR AEROPUERTOS     ║")
        print("║   2. VISUAIZAR RUTAS            ║")
        print("║   3. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>3 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 3: #Salir
            break
        wait()

def Complejidades():
    while(True):
        os.system('cls')
        print("╔═════════════════════════════════╗")
        print("║ COMPLEJIDADES DE LOS ALGORITMOS ║")
        print("╠═════════════════════════════════╣")
        print("║   1. BFS                        ║")
        print("║   2. DFS                        ║")
        print("║   3. DIJKSTRA                   ║")
        print("║   4. FLOYD-WARSHALL             ║")
        print("║   5. DETECTAR CICLOS            ║")
        print("║   6. ATRÁS                      ║")
        print("╚═════════════════════════════════╝")
        try:
            opc = int(input("Su opción: "))
        except:
            print("Opcion no válida.")
            wait()
        if opc>6 or opc<1: #Límites
            print("Opcion no válida.")
            wait()
            continue
        if opc == 6: #Salir
            break
        wait()

#MAIN
#Operaciones iniciales obligatorias
dic = Graph()
dic.crearGrafoCero()
grafo = dic.getGrafo()
rutasVacias()
ruteoAleatorio(1) #la mejor estación

opc = 0
while opc!=7:
    opc = MP()
    if (opc>7 or opc<1) and opc!=-1: #Al retornar -1 indica que el user no ingresó int
        print("Opcion no válida.")   # No entra porque ya lo regañó la función
        wait()
        continue
    if opc == 1:
        Estacion()
    if opc == 2:
        InfoAeropuertos()
    if opc == 3:
        Recorridos(grafo)
    if opc == 4:
        Operaciones()
    if opc == 5:
        Visualizar()
    if opc == 6:
        Complejidades()


os.system('cls')
