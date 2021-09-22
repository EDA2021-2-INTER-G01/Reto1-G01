﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import datetime
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mrgsort
from DISClib.Algorithms.Sorting import quicksort as quicks
import time
assert cf
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList("""'SINGLE_LINKED',
                                    cmpfunction=compareartists""")
    return catalog

# Funciones para creacion de datos

def nuevoArtwork(name,dateacquired,constituentid,date,medium,dimensions,department,creditline,classification):
    if dateacquired:
        datel=dateacquired.split('-')
        dateacquired2=datetime.date(int(datel[0]),int(datel[1]),int(datel[2]))
    else:
        dateacquired2=datetime.date(1,1,1)
    
    artwork={'name':'','dateacquired':'','constituentid':'','date':'','medium':'',
             'dimensions':'','department':'','creditline':'','classification':''}
    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    artwork['constituentid']=constituentid
    artwork['date']=date
    artwork['medium']=medium
    artwork['dimensions']=dimensions
    artwork['department']=department
    artwork['creditline']=creditline
    artwork['classification']=classification 
    return artwork

def newArtist(ConstituentID,nom,aN,aF,nacion,genero):
    artista = {"ConstituentID": "","Nombre":"", "Año De Nacimiento": "",  
               "Año De Fallecimiento": "","Nacion":"","Genero":""}
    artista["ConstituentID"] = ConstituentID
    artista["Nombre"]=nom
    artista["Año De Nacimiento"]=aN
    artista["Año De Fallecimiento"]=aF
    artista["Nacion"]=nacion
    artista["Genero"]=genero

    return artista

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    nuevo=nuevoArtwork(artwork['Title'],artwork['DateAcquired'],
                       artwork['ConstituentID'],artwork['Date'],
                       artwork['Medium'],artwork['Dimensions'],
                       artwork['Department'],artwork['CreditLine'],artwork['Classification'])
    lt.addLast(catalog['artworks'],nuevo)

def addArtist(catalog, artista):
    art = newArtist(artista['ConstituentID'], artista['DisplayName'],artista['BeginDate'],
                    artista['EndDate'],artista['Nationality'],artista['Gender'])
    lt.addLast(catalog['artists'], art)


# Funciones de consulta

def getUltimos(lista):
    posicionl=lt.size(lista)-2
    return lt.subList(lista, posicionl, 3)
def getPrimeros(lista):
    
    return lt.subList(lista, 1, 3)
def getPurchase(lista):
    cont=0
    x=1
    while x <=lt.size(lista):
        if "purchase" in (lt.getElement(lista,x)["creditline"].lower()):
            cont+=1
        x+=1    
    return cont   
<<<<<<< HEAD

def get_artistas_tecnica(catalog, nombre_artista):
    sub_list = catalog['artists']
    artistas = sub_list['elements']
    sub_list2 = catalog['obrasPorArtistas']
    obras = sub_list2['elements']
    lista_tecnicas = []
    ObrasTecnica= []

    for llave in artistas:
        if llave['DisplayName'] == nombre_artista:
            id = llave['ConstituentID']

    totalObras = 0
    totalTecnicas = 0
    for llave in obras:
        if llave['ConstituentID'] == id:
            lista = llave['artworks']
            artworks = lista['elements']
            for cadaObra in artworks:
                totalObras += 1
                tecnica = cadaObra['Medium']
                if tecnica not in lista_tecnicas:
                    totalTecnicas += 1
                lista_tecnicas.append(tecnica)

    TecnicaMasUtilizada = max(key=lista_tecnicas.count)
    for obras in artworks:
        if obras['Medium'] == TecnicaMasUtilizada:
            info = {'Titulo': obras['Title'],
                    'Fecha': obras['Date'],
                    'Medio': obras['Medium'],
                    'Dimensiones': obras['Dimensions']}
            ObrasTecnica.append(info)

    return totalObras, totalTecnicas, TecnicaMasUtilizada, ObrasTecnica
=======
def getNacion(lista):
    obras=lista["artworks"]  
    artistas=lista["artists"]
    retorno = {"na":{}}        
    for i in range(round(lt.size(obras))):
        llave = lt.getElement(obras, i)
        dateacquired = llave["dateacquired"]
        name = llave["name"]
        medium = llave["medium"]
        dimensions = llave["dimensions"]
        artistas=llave["constituentid"]
        naciones=lt.newList()
        
        for i in range(round(lt.size(artistas))):
            llave2=lt.getElement(artistas,i)
            id=llave2["ConstituentID"]
            nacion=llave2["Nacion"]
            if id in artistas:
                lt.addLast(naciones,nacion
                )        
        for i in lt.size(naciones):
            agregar = {"name" : name,"artistas":artistas, "dateacquired" : dateacquired, 
                       "medium" : medium, "dimensions" : dimensions}
            if  lt.getElement(naciones,i) in retorno['na'] :
                lt.addLast(retorno["na"][lt.getElement(naciones,i)], agregar)    
            else:
                retorno["na"][lt.getElement(naciones,i)]=lt.newList()  
                lt.addLast(retorno["na"][lt.getElement(naciones,i)], agregar)
    return retorno               

            


>>>>>>> 38796cc606f9b6d05bbdb35d3ff23e79cd755553

def obrasCronologicoacq(lista,inicio,final,metodo,sizesublista): 
    obras = lista["artworks"]
    respuesta = lt.newList()
    for i in range(round(lt.size(obras)*sizesublista)):
        llave = lt.getElement(obras, i)
        dateacquired = llave["dateacquired"]
        name = llave["name"]
        medium = llave["medium"]
        dimensions = llave["dimensions"]
        creditline=llave["creditline"]
        artistas=llave["constituentid"]
        if  dateacquired >= inicio and dateacquired <= final:
            agregar = {"name" : name,"artistas":artistas, "dateacquired" : dateacquired, 
                       "medium" : medium, "creditline":creditline, "dimensions" : dimensions}
            lt.addLast(respuesta, agregar)
            tiempo_inicio=time.process_time()
    if metodo=='ShellSort':
        sa.sort(respuesta, cmpArtworkByDateAcquired)
    elif metodo=='InsertionSort':
        ins.sort(respuesta, cmpArtworkByDateAcquired)
    elif metodo=='MergeSort':
        mrgsort.sort(respuesta, cmpArtworkByDateAcquired)
    elif metodo=='':
        quicks.sort(respuesta,cmpArtworkByDateAcquired)
    tiempo_fin=time.process_time()
    TimeMseg=(tiempo_fin-tiempo_inicio)*1000
    return respuesta

def sortArtistas(Artistasc):
    sub_list = lt.subList(Artistasc,1,lt.size(Artistasc))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, compareartists)
    stop_time = time.process_time()
    
    tiempo = (stop_time - start_time)*1000
    final=lt.newList()
    final2=lt.newList()
    final=getPrimeros(sorted_list)
    final2=getUltimos(sorted_list)   
    return tiempo, final, final2
def cArtistas(catalog,aInicio,aFinal) :
    Artistasc=lt.newList()
    x=1
    while x<=lt.size(catalog["artists"]):
        y=lt.getElement(catalog["artists"],x)
        if (aInicio<=int(y["Año De Nacimiento"])<=aFinal):
            lt.addLast(Artistasc,y)
        x+=1    
    return Artistasc

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artist1,artist2):
    return (float(artist1['Año De Nacimiento']) < float(artist2['Año De Nacimiento']))
    

def cmpArtworkByDateAcquired(artwork1,artwork2): 
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1['dateacquired']<artwork2['dateacquired']
