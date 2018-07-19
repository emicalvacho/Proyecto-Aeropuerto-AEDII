##############################################################################################
#                                   Datos de Mapas.py                                        #
#                                                                                            #
##############################################################################################
# - Autor: Gonzalo Grisafi                                                                   #
##############################################################################################
# - Funcionalidad: llama a los scripts creadores de mapas y los crea los archivos html       #
# generados para poder abrirlos en un navegador web                                          # 
##############################################################################################
# - Licencia: Copyright © 2018 - Alumnos de 3er año de Informatica del IDES                  #
##############################################################################################

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

