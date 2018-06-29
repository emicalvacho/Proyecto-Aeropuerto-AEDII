import webbrowser as wb
import os
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def AbrirMapaRutas():
    archivo='file:///'+buscarArchivo('MapaRutas.html')
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(browser_path).open_new(archivo)
    except wb.Error:
        wb.open_new(archivo)

def AbrirMapaAeropuertos():
    archivo='file:///'+buscarArchivo('MapaAeropuertos.html')
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(browser_path).open_new(archivo)
    except wb.Error:
        wb.open_new(archivo)
