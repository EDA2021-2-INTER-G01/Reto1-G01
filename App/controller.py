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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def getUltimos(lista):
    Elements=model.getUltimos(lista)
    return Elements 
def getPurchase(lista):
    return model.getPurchase(lista)       

""""def artistasFecha(lista, inicio, final):
    artistasfechas = model.artistaFecha(lista, inicio, final)
    return artistasfechas"""
def sortArtistas(lista):
    return model.sortArtistas(lista)

def getNacion(lista):
    return model.getNacion(lista)  
      
def cA(catalog,inicio,final):
    return model.cArtistas(catalog,inicio,final)  

def obrasFecha(lista, inicio, final,metodo,sizesublista):
    if inicio:
        datel=inicio.split('-')
        inicio2=datetime.date(int(datel[0]),int(datel[1]),int(datel[2]))
    else:
        return(1)
    
    if final:
        datelst2=final.split('-')
        final2=datetime.date(int(datelst2[0]),int(datelst2[1]),int(datelst2[2]))
    else:
        #print('ERROR, FECHA NO VALIDA')
        return(2)
    
    if not(metodo=='MergeSort' or metodo=='QuickSort'or 
            metodo=='ShellSort'or metodo=='InsertionSort'):
        #print('ERROR, METODO NO VALIDO')
        return(3)
    return model.obrasCronologicoacq(lista,inicio2,final2,metodo,sizesublista)     

def obrasPorTecnica(catalog, nombre_artista):
    diccionario={}
    retorno={}
    return model.get_artistas_tecnica(catalog, nombre_artista,diccionario,retorno)