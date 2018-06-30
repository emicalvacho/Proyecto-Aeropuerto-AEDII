import sys
sys.path.append("..")
from Visualización.CrearMapa import CrearMapaRutas,CrearMapaAeropuertos
from Visualización.AbrirArchivo import AbrirMapaRutas,AbrirMapaAeropuertos


def MapaAeropuertos():
    CrearMapaAeropuertos()
    AbrirMapaAeropuertos()

def MapaRutas():
    CrearMapaRutas()
    AbrirMapaRutas()

