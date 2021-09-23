"""
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
               'artists': None,
               'obrasPorArtistas': None,
               'artistasPorObras': None,
               'nacionalidades':None}

    catalog['artworks'] = lt.newList("ARRAY_LIST")
    catalog['artists'] = lt.newList("ARRAY_LIST")
    return catalog


# Funciones para creacion de datos

def nuevoArtwork(name,dateacquired,constituentid,date,medium,dimensions,department,creditline,classification,largo,altura,ancho,circun,diametro,peso):
    if dateacquired:
        datel=dateacquired.split('-')
        dateacquired2=datetime.date(int(datel[0]),int(datel[1]),int(datel[2]))
    else:
        dateacquired2=datetime.date(1,1,1)
    artwork={'name':'','dateacquired':'','constituentid':'','date':'','medium':'',
             'dimensions':'','department':'','creditline':'','classification':'','largo':'',
             'altura':'','ancho':'','circunferencia':'','diametro':'','peso':''}
    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    artwork['constituentid']=constituentid
    artwork['date']=date
    artwork['medium']=medium
    artwork['dimensions']=dimensions
    artwork['department']=department
    artwork['creditline']=creditline
    artwork['classification']=classification
    artwork['largo']=largo
    artwork['altura']=altura
    artwork['ancho']=ancho
    artwork['circunferencia']=circun
    artwork['diametro']=diametro
    artwork['peso']=peso 
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
                       artwork['Department'],artwork['CreditLine'],
                       artwork['Classification'],artwork['Length (cm)'],
                       artwork['Height (cm)'],artwork['Width (cm)'],
                       artwork['Circumference (cm)'],artwork['Diameter (cm)'],
                       artwork['Weight (kg)'])
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

def get_artistas_tecnica(catalog, nombre_artista,diccionario,retorno):
    artistas=lt.iterator(catalog['artists'])
    obras=lt.iterator(catalog['artworks'])
    valor=0
    for artista in artistas:
        if artista["Nombre"]==nombre_artista:
            id=artista["ConstituentID"]
            break
    for obra in obras:
        constituent=obra["constituentid"].strip('[]')
        constituent=constituent.split(",")
        if id in constituent:
            tecnica=obra["medium"]
            if tecnica not in diccionario:
                diccionario[tecnica]=1
                retorno["Obras"+tecnica]=[dict(obra)]
            else:
                diccionario[tecnica]+=1
                retorno["Obras"+tecnica]=retorno["Obras"+tecnica].append(dict(obra))
    for keys,values in diccionario.items():
        if values>valor:
            valor=values
            key=keys
    respuesta={"obra":len(retorno.values()),"tecnicas":len(diccionario),"TecnicaMasUsada":key,"ObraPorTecnica":retorno["Obras"+key]}
    print('\nEl artista '+nombre_artista+' tiene en total de obras: '+str(respuesta["obra"]))
    print('Total de tecnicas: '+str(respuesta["tecnicas"]))
    print('Tecnica mas utilizada: '+str(respuesta["TecnicaMasUsada"]))
    print('Las obras de la tecnica más utilizada: ' +str(respuesta["ObraPorTecnica"]))
    return None


def getNacion(lista):
    obras=lista["artworks"]  
    artistas=lista["artists"]
    retorno = {}  
    naciones=lt.newList("ARRAY_LIST")    
    for i in range(lt.size(obras)):
        llave = lt.getElement(obras, i)
        dateacquired = llave["dateacquired"]
        name = llave["name"]
        medium = llave["medium"]
        dimensions = llave["dimensions"]
        art=llave["constituentid"]
        artista=art.replace('[','').replace(']','').replace(' ','').split(",")

        na=lt.newList("ARRAY_LIST")
        agregar = {"name" : name,"artistas":artista, "dateacquired" : dateacquired, 
                       "medium" : medium, "dimensions" : dimensions}
        for i in range(lt.size(artistas)):
            
            llave2=lt.getElement(artistas,i)
            id=llave2['ConstituentID']
            nacion=llave2["Nacion"]
            if (id in artista) and (lt.isPresent(naciones,nacion)==0)  :            
                lt.addLast(naciones,nacion)
                retorno[nacion]=lt.newList("ARRAY_LIST")  
                lt.addLast(retorno[nacion], agregar)
            elif (id in artista) :  
                lt.addLast(na,nacion)    
                lt.addLast(retorno[nacion], agregar)                       
                                      
                              
    total=lt.newList("ARRAY_LIST")           
    for i in range(lt.size(naciones)):
        pais=lt.getElement(naciones,i)
        if (pais!="") and (pais!="Nationality unknown"):
         num=lt.size(retorno[pais])
        
         new={"pais":pais,"numero de obras":num}
         
         lt.addLast(total,new)
    nu1=lt.size(retorno["Nationality unknown"])
    nu2=lt.size(retorno[""])                                               
    new={"pais":"Nationality unknown","numero de obras":nu1+nu2}
    
    lt.addLast(total,new)
    
    retorn=sa.sort(total,sortnacion)
    pos=lt.getElement(retorn,1)["pais"]
    re1=getPrimeros(retorno[pos])
    re2=getUltimos(retorno[pos]) 
 
    return lt.subList(retorn,1,10),re1,re2,print(naciones)             

def transObras(dep,lis):
    obras=pordepartamento(dep,lis)
    precio=0
    pesoo=0
    for i in range (lt.size(obras)):
        llave=lt.getElement(obras,i)
        if llave["largo"]!="":
            largo=(float(llave["largo"])*100)
        else:
            largo=0
        if llave["diametro"]!="":
            diametro=(float(llave["diametro"])*100)
        else:
            diametro=0
        if llave["ancho"]!="":
            ancho=(float(llave["ancho"])*100)
        else:
            ancho=0
        if llave["altura"]!="":
            altura=(float(llave["altura"])*100)
        else:
            altura=0    
        if llave["circunferencia"]!="":
            circunferencia=(float(llave["circunferencia"])*100)
        else:
            circunferencia=0
        if llave["peso"]!="":
            peso=(float(llave["peso"])*100)
        else:
            peso=0
        
        pre=0
        if peso:
            pre=72*peso
            pesoo+=peso
        if largo>0 and ancho>0 and altura>0:
            vol=largo*altura*ancho
            if pre==0 or (vol*72>pre):
             pre=72*vol
        if largo>0 and ancho>0:
            area=largo*ancho
            if pre==0 or (area*72>pre):
                pre=area*72
        if diametro!="":
            r=(int(diametro)/2)
        else:
            r=0            
        if diametro>0 and altura>0:
            vol=3.1416*(r**2)*altura
            if pre==0 or (vol*72>pre):
                pre=area*72
        if diametro>0:
            vol=((4*3.1416)/3)*(r**3)
            if pre==0 or (vol*72>pre):
                pre=area*72
        if circunferencia>0:
            area=(circunferencia/2)*(circunferencia/6.2831)
            if pre==0 or (area*72>pre):
                pre=area*72
                        
        if pre==0:
            pre=48
        lt.getElement(obras,i)["costo"]=pre            
        precio+=pre
        pesoo+=peso
    return precio, lt.size(obras), pesoo,sortantiguedad(obras),sortcosto(obras)
def pordepartamento(dep,lista):
    obras=lista["artworks"]
    retorno=lt.newList("ARRAY_LIST")
    for i in range(lt.size(obras)):
        llave = lt.getElement(obras, i)
        dateacquired = llave["dateacquired"]
        name = llave["name"]
        depa=llave["department"]
        medium = llave["medium"]
        if llave["date"]!="":
            antiguedad=(2021-int(llave["date"]))
        else:
            antiguedad=0    
        clasificacion=llave["classification"]
        dimensions = llave["dimensions"]
        art=llave["constituentid"]
        largo=(llave["largo"])
        diametro=(llave["diametro"])
        ancho=(llave["ancho"])
        altura=(llave["altura"])
        circunferencia=(llave["circunferencia"])
        peso=(llave["peso"])

        artista=art.replace('[','').replace(']','').replace(' ','').split(",")

        agregar = {"name" : name,"artistas":artista, "dateacquired" : dateacquired, 
                    "medium" : medium, "dimensions" : dimensions, 
                    "clasificacion":clasificacion,"antiguedad":antiguedad,"largo":largo, "diametro" : diametro, 
                    "ancho" : ancho, "altura" : altura, 
                    "circunferencia":circunferencia,"peso":peso}
        if depa.lower() == dep.lower():
            lt.addLast(retorno,agregar)
    return retorno
def sortantiguedad(lista):    
    retorno=sa.sort(lista,comparea)
    return lt.subList(retorno,1,5)
def sortcosto(lista):
    retorno=sa.sort(lista,comparep)
    return lt.subList(retorno,1,5)    


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


def sortnacion(pais1,pais2):
    return pais1["numero de obras"]>pais2["numero de obras"]

def comparea(obra1,obra2):
    return obra1["antiguedad"]>obra2["antiguedad"]
def comparep(obra1,obra2):
    return obra1["costo"]>obra2["costo"]    
