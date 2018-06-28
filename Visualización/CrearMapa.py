import folium
import pandas as pd
import branca
import sys
import os
from pathlib import Path
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def CrearMapa():
    ruta=buscarArchivo("AeropuertosArg.csv")
    map_osm=folium.Map(location=[-40.1872152,-64.6290514],zoom_start=4)
    #df=pd.read_csv('Argentina.csv',names=['AirportID','Name','City','Country','Latitud','Longitud'])
    df=pd.read_csv(ruta,names=['ID','Nombre','Ciudad','Provincia','Latitud','Longitud'])
    for index,row in df.iterrows():
        #info = "<h4>%s</h4><p>Provincia: %s</p><p>Ciudad: %s</p>" %(row['Nombre'],row['Provincia'],row['Ciudad'])
        info="""
            <p><font face="verdana" color="black">
                <p style="text-align: center;"><strong>%s</strong></p>
                <p style="text-align: center;"><em><strong>Provincia:</strong></em><strong>&nbsp;</strong>%s</p>
                <p style="text-align: center;"><em><strong>Ciudad:</strong></em> %s</p>
                <p>&nbsp;</p>
            </font></p>
        """%(row['Nombre'],row['Provincia'],row['Ciudad'])
        iframe=branca.element.IFrame(html=info,width="400",height="150")
        folium.Marker(
        [row['Latitud'],row['Longitud']],
        popup=folium.Popup(iframe,max_width=400),
        icon=None).add_to(map_osm)

    directorio=Path(os.getcwd())
    directorio=directorio.parent
    directorio=str(directorio)
    directorio+='\\Visualización\\Mapa.html'
    map_osm.save(directorio)
