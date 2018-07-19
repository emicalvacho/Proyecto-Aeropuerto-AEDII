##############################################################################################
#                                   Datos de CrearMapa.py                                    #
#                                                                                            #
##############################################################################################
# - Autor: Gonzalo Grisafi                                                                   #
##############################################################################################
# - Funcionalidad: abre el archivo html en un navegador                                      # 
##############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                  #
##############################################################################################

import webbrowser as wb
import os
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def AbrirMapaRutas():
    """
        Funcionamiento: abre el mapa de rutas
        Precondicion: no recibe nada
        Postcondicion: no devuelve nada
    """
    archivo='file:///'+buscarArchivo('MapaRutas.html')
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(browser_path).open_new(archivo)
    except wb.Error:
        wb.open_new(archivo)

def AbrirMapaAeropuertos():
    """
        Funcionamiento: abre el mapa de aeropuertos
        Precondicion: no recibe nada
        Postcondicion: no devuelve nada
    """
    archivo='file:///'+buscarArchivo('MapaAeropuertos.html')
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(browser_path).open_new(archivo)
    except wb.Error:
        wb.open_new(archivo)
