import sys
sys.path.append("..")   #Para localizarse en una carpeta más arriba que la actual
from Visualización.CrearMapa import CrearMapa     
from Visualización.AbrirArchivo import AbrirArchivo

CrearMapa() #Crea el archivo html en la carpeta Visualización

AbrirArchivo() #Busca el archivo y lo abre en el navegador
