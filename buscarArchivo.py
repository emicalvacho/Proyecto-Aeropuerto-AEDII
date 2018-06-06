import os

#le tienen que pasar el string del nombre del archivo con la extension incluida.
#Ejemplo: "chrome.exe","AeropuertosArg.csv"

def buscarArchivo(archivo):
    #for path,carpetas, archivos in os.walk("C:\\"): #Yo tengo los archivos en el Disco D, ponganlo en el Disco donde tienen los archivos.
    for path,carpetas, archivos in os.walk(os.getcwd()): #Forma mas eficiente, busca a partir del espacio actual de trabajo
        for nombre in archivos:                          #IMPORTANTE: Poner este archivo dentro del directorio gral.
            if nombre == archivo:
                return (os.path.abspath(os.path.join(path, nombre)))

"""
Va a devolver la primera apararicion del archivo, asi que no tengan archivos duplicados
"""
#Ejemplo:
#print(buscarArchivo("AeropuertosArg.csv"))
#Esto Devuelve: D:\Archivos de Gonzalo\Proyecto AED II\AeropuertosArg.csv en mi caso
