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
 
from DISClib.ADT.graph import gr
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Utils import error as error
assert cf
 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
 
# Construccion de modelos
def IniciarDatos():
    """ Inicializa el catalogo
 
   aeropuertos_gd: Tabla de hash para guardar los vertices del grafo dirigido
 
   gd_aero_ruta: Grafo dirigido para representar las rutas entre los aeropuertos
 
   components: Almacena la informacion de los componentes conectados de grafo dirigido
 
   minimo: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo dirigido
 
    g_una_ruta: Un grafo no dirigido en el cual se incluirán solamente
                los aeropuertos y las rutas que tengan tanto una ruta de
                ida entre los dos aeropuertos como uno de vuelta
 
    aeropuertos_g: Tabla de hash para guardar los vertices del grafo NO dirigido
 
    city: Tabla de hash para guardar las ciudades (llave) del archivo 'worldcities.csv' y como
          valor toda su info.
 
    """
    catalog = {
                    'aeropuertos_gd': None,
                    'gd_aero_ruta': None,
                    'components': None,
                    'minimo': None,
                    'g_una_ruta' :None,
                    'aeropuertos_g': None,
                    'city' : None
                    }
 
    catalog['aeropuertos_gd'] = mp.newMap(numelements=140000,
                                     maptype='PROBING',
                                     comparefunction=compare)
 
    catalog['gd_aero_ruta'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=140000,
                                              comparefunction=compare)
                                             
    catalog['aeropuertos_g'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compare)
 
    catalog['g_una_ruta'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=140000,
                                              comparefunction=compare)
                                             
    catalog['city'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compare2)
 
    return catalog
 
# Funciones para agregar informacion al catalogo
 
def addAirport(catalog, aeropuerto):
    """
    adiciona el codigo IATA del archivo airports_full.csv
    como vertice al grafo dirigido 'gd_aero_ruta'
    """
    if gr.containsVertex(catalog['gd_aero_ruta'], aeropuerto) == False:
        gr.insertVertex(catalog['gd_aero_ruta'], aeropuerto)
 
def addRouteConnections(catalog, origen, destino, peso):
    """
    Por cada vertice (cada aeropueto) se recorre la lista
    de rutas servidas en dicho aeropuerto y se crean
    arcos entre ellos.
    """
    if gr.getEdge(catalog['gd_aero_ruta'], origen, destino) == None:
        gr.addEdge(catalog['gd_aero_ruta'], origen, destino, peso)
 
def addRuta(catalog, ruta):
    """
    añade aeropuertos como vertices y las rutas como arcos al grafo dirigido
    """
    origen = ruta['Departure']
    destino = ruta['Destination']
    peso = float(ruta['distance_km'])
    addAirport(catalog, origen)
    addAirport(catalog, destino)
    addRouteConnections(catalog, origen, destino, peso)
 
def addAirportNoD(catalog, aeropuerto):
    """
    añade aeropuertos como vertices al grafo NO dirigido
    """
    if gr.containsVertex(catalog['g_una_ruta'], aeropuerto) == False:
        gr.insertVertex(catalog['g_una_ruta'], aeropuerto)
 
def addRutaNoD(catalog, origen, destino, peso):
    """
    añade rutas como arcos al grafo NO dirigido
    """
   
    if  gr.getEdge(catalog['g_una_ruta'], origen, destino) == None:
        gr.addEdge(catalog['g_una_ruta'], origen, destino, peso)
 
def addCity(catalog, linea):
 
    pass
 
# Funciones para creacion de datos
 
# Funciones de consulta
 
# Funciones utilizadas para comparar elementos dentro de una lista
 
# Funciones de ordenamiento
def compare(valor1, valor2):
    """
    comparacion de grafos
    """
    valor2= valor2['key']
    if (valor1 == valor2):
        return 0
    elif valor1 > valor2:
        return 1
    else:
        return -1
def compare2(valor1, valor2):
    """
    Comparación para las listas
    """
    if (valor1 == valor2):
        return 0
    elif valor1 > valor2:
        return 1
    else:
        return -1