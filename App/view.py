"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller as c
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de una artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Consultar costo de transportar todas las obras e un departamento")
    print("0- Salir")

def initCatalog():
    return c.initCatalog()

def loadData(catalog):
    c.loadData(catalog)

def printObrasCr(lista):
    cantidad = lt.size(lista)
    print(str(cantidad) + " obras fueron adquiridas en el rango seleccionado, y " +str(c.getPurchase(lista))+" se compraron." )
    print("Top 3 mas jovenes: ")
    x=1
    while x<=3:
        y=lt.getElement(lista,x)
        print(y)
        x+=1
    print("Top 3 mas viejos: ")
    x=0
    while x<=2:
        y=lt.getElement(lista,(lt.size(lista)-x))
        print(y)
        x+=1


def printArtistasFecha(lista,lista1,lista2):
    cantidad = lt.size(lista)
    print("Hay " + str(cantidad) + " artistas en el rango seleccionado")
    print()
    print("Top 3 mas jovenes: ")
    x=1
    while x<=lt.size(lista2):
        y=lt.getElement(lista2,x)
        print(y)
        x+=1
    print("Top 3 mas viejos: ")
    x=1
    while x<=lt.size(lista1):
        y=lt.getElement(lista1,x)
        print(y)
        x+=1

def PrintArtistaTecnica(catalogo):
    name=input("Ingrese el nombre del artista: ")
    lista=c.obrasPorTecnica(catalog, name)
    return lista


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        datatype=input('Seleccione el tipo de tipo de estructura para los datos (ARRAY_LIST, LINKED_LIST)')
        print('Obras de arte cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Últimas 3 obras cargadas: ')
        print(c.getUltimos(catalog["artworks"]))
        print('Últimos 3 artistas cargados: ')
        print(c.getUltimos(catalog["artists"]))
        
    elif int(inputs[0]) == 2:
        Añoi= int(input("¿Desde que año quiere buscar?:  "))
        Añof = int(input("¿Hasta que año quiere buscar?:  "))
        respuesta=c.cA(catalog,Añoi,Añof)
        resultados= c.sortArtistas(respuesta)
        print("El tiempo en mseg para la muestra de",lt.size(catalog["artists"]), " fue de: ",
                                          str(resultados[0]))
        printArtistasFecha(respuesta,resultados[1],resultados[2])
        

        
    elif int(inputs[0]) == 3:
        FechaInicial = input("¿Desde que fecha quiere buscar? (formato AAAA-MM-DD):   ")
        FechaFin = input("¿Hasta que fecha quiere buscar?(formato AAAA-MM-DD):   ")
        MetodoSort=input('¿Qué algoritmo de ordenamiento quiere implementar, InsertionSort, ShellSort, MergeSort o QuickSort?')
        SizeSubLista=float(input('Ingrese el porecentaje de la muestra (entre 0 y 1):  '))
        CantidadObras=c.obrasFecha(catalog,FechaInicial,FechaFin,MetodoSort,float(SizeSubLista))
        printObrasCr(CantidadObras)

    elif int(inputs[0]) == 4:
        respuesta=PrintArtistaTecnica(catalog)
        print(respuesta)
        nombre_artista = input("Ingrese el nombre del artista: ")
        obras = c.artistas_tecnica(catalog,nombre_artista)
        print(c)
    
    elif int(inputs[0]) == 5:
        print(c.getNacion(catalog))
    elif int(inputs[0])==6:
        departamento=input("Ingrese el departamento del museo que desea consultar: ")  
        print(c.transObras(departamento,catalog))  
    else:
        sys.exit(0)
sys.exit(0)