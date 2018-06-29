import folium
import pandas as pd
import branca
import sys
import random
import os
from pathlib import Path
sys.path.append("..")
from BuscadorPath.buscarArchivo import buscarArchivo

def colorRandom():
    return "#"+str(hex(random.randint(0,16777216))[2:])

def CrearMapaRutas():
    ruta=buscarArchivo("AeropuertosArg.csv")
    ruta2=buscarArchivo("RutasAeropuertos.csv")
    map_osm=folium.Map(location=[-40.1872152,-64.6290514],zoom_start=4)
    #df=pd.read_csv('Argentina.csv',names=['AirportID','Name','City','Country','Latitud','Longitud'])
    df=pd.read_csv(ruta,names=['ID','Nombre','Ciudad','Provincia','Latitud','Longitud'])
    df2=pd.read_csv(ruta2,names=['ID Origen','ID Destino','Distancia'])

    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    aislados=dict.fromkeys(lista)

    for index,row in df2.iterrows():
        aislados[row['ID Origen']]=1
        aislados[row['ID Destino']]=1

    grupo2=folium.FeatureGroup(name='Aeropuertos Aislados')

    for index,row in df.iterrows():
        info="""
            <p><font face="verdana" color="black">
                <p style="text-align: center;"><strong>%s</strong></p>
                <p style="text-align: center;"><em><strong>Provincia:</strong></em><strong>&nbsp;</strong>%s</p>
                <p style="text-align: center;"><em><strong>Ciudad:</strong></em> %s</p>
                <p>&nbsp;</p>
            </font></p>
        """%(row['Nombre'],row['Provincia'],row['Ciudad'])
        iframe=branca.element.IFrame(html=info,width="400",height="150")
        if aislados[row['ID']]==1:
            folium.Marker(
            [row['Latitud'],row['Longitud']],
            popup=folium.Popup(iframe,max_width=400),
            icon=folium.Icon(color='blue',icon='plane',prefix='fa')).add_to(map_osm)
        else:
            folium.Marker(
            [row['Latitud'],row['Longitud']],
            popup=folium.Popup(iframe,max_width=400),
            icon=folium.Icon(color='red',icon='plane',prefix='fa')).add_to(grupo2)

    grupo2.add_to(map_osm)

    latitudes={}
    longitudes={}
    ciudades={}
    for index,row in df.iterrows():
        latitudes[row['ID']]=round(row['Latitud'],6)
        longitudes[row['ID']]=round(row['Longitud'],6)
        ciudades[row['ID']]=str(row['Ciudad'])

    for index,row in df2.iterrows():
        lineas=[]
        li=[]
        li.append(latitudes[row['ID Origen']])
        li.append(longitudes[row['ID Origen']])
        lineas.append(li)
        li=[]
        li.append(latitudes[row['ID Destino']])
        li.append(longitudes[row['ID Destino']])
        lineas.append(li)
        mostrar=ciudades[row['ID Origen']]+" - "+ciudades[row['ID Destino']]
        #folium.PolyLine(locations=lineas,color=colorRandom(),weight=3,opacity=1,popup=mostrar).add_to(map_osm)
        folium.PolyLine(locations=lineas,color=colorRandom(),weight=3.5,opacity=1,popup=mostrar+" "+str(row['Distancia'])+" km").add_to(folium.FeatureGroup(name=mostrar).add_to(map_osm))

    folium.LayerControl().add_to(map_osm)

    leyenda =   '''
            <div style="position: fixed;
                        bottom: 50px; left: 50px; width: 288px; height: 160px;
                        border:3px solid black; z-index:9999; font-size:18px;
                        background:#F9EECF;
                        ">&nbsp;<p style="text-align: center;"><strong> Leyenda <br></strong></p>
                          &nbsp;<strong> Aeropuerto No Aislado</strong> &nbsp; <i class="fa fa-plane fa-2x" style="color:blue"></i><br>
                          &nbsp;<strong> Aeropuerto Aislado</strong> &nbsp; <i class="fa fa-plane fa-2x" style="color:red"></i>
            </div>
            '''

    map_osm.get_root().html.add_child(folium.Element(leyenda))


    directorio=Path(os.getcwd())
    directorio=directorio.parent
    directorio=str(directorio)
    directorio+='\\Visualización\\MapaRutas.html'
    map_osm.save(directorio)

def CrearMapaAeropuertos():
    ruta=buscarArchivo("AeropuertosArg.csv")
    ruta2=buscarArchivo("RutasAeropuertos.csv")
    map_osm=folium.Map(location=[-40.1872152,-64.6290514],zoom_start=4)
    #df=pd.read_csv('Argentina.csv',names=['AirportID','Name','City','Country','Latitud','Longitud'])
    df=pd.read_csv(ruta,names=['ID','Nombre','Ciudad','Provincia','Latitud','Longitud'])
    df2=pd.read_csv(ruta2,names=['ID Origen','ID Destino','Distancia'])

    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    aislados=dict.fromkeys(lista)

    for index,row in df2.iterrows():
        aislados[row['ID Origen']]=1
        aislados[row['ID Destino']]=1

    for index,row in df.iterrows():
        info="""
            <p><font face="verdana" color="black">
                <p style="text-align: center;"><strong>%s</strong></p>
                <p style="text-align: center;"><em><strong>Provincia:</strong></em><strong>&nbsp;</strong>%s</p>
                <p style="text-align: center;"><em><strong>Ciudad:</strong></em> %s</p>
                <p>&nbsp;</p>
            </font></p>
        """%(row['Nombre'],row['Provincia'],row['Ciudad'])
        iframe=branca.element.IFrame(html=info,width="400",height="150")
        if aislados[row['ID']]==1:
            folium.Marker(
            [row['Latitud'],row['Longitud']],
            popup=folium.Popup(iframe,max_width=400),
            icon=folium.Icon(color='blue',icon='plane',prefix='fa')).add_to(map_osm)
        else:
            folium.Marker(
            [row['Latitud'],row['Longitud']],
            popup=folium.Popup(iframe,max_width=400),
            icon=folium.Icon(color='red',icon='plane',prefix='fa')).add_to(map_osm)

        leyenda =   '''
                <div style="position: fixed;
                            bottom: 50px; left: 50px; width: 288px; height: 160px;
                            border:3px solid black; z-index:9999; font-size:18px;
                            background:#F9EECF;
                            ">&nbsp;<p style="text-align: center;"><strong> Leyenda <br></strong></p>
                              &nbsp;<strong> Aeropuerto No Aislado</strong> &nbsp; <i class="fa fa-plane fa-2x" style="color:blue"></i><br>
                              &nbsp;<strong> Aeropuerto Aislado</strong> &nbsp; <i class="fa fa-plane fa-2x" style="color:red"></i>
                </div>
                '''

    map_osm.get_root().html.add_child(folium.Element(leyenda))
    directorio=Path(os.getcwd())
    directorio=directorio.parent
    directorio=str(directorio)
    directorio+='\\Visualización\\MapaAeropuertos.html'
    map_osm.save(directorio)
