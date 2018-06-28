import webbrowser as wb
import os
import sys
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def AbrirArchivo():
    archivo='file:///'+buscarArchivo('Mapa.html')
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(browser_path).open_new(archivo)
    except wb.Error:
        wb.open_new(archivo)
#AbrirArchivo()
