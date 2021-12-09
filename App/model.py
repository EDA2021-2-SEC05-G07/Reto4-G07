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
 
from math import trunc
from DISClib.ADT.graph import gr
from DISClib.DataStructures.arraylist import addLast
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Utils import error as error
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import dfs
assert cf
from DISClib.ADT import orderedmap as om
 
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
                                     comparefunction=compareMap)
 
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
    if mp.contains(catalog['city'], linea['city']):
        valor= mp.get(catalog['city'], linea['city'])
        info= me.getValue(valor)
        lt.addLast(info, linea)
    else:
        info=lt.newList()
        lt.addLast(info, linea)
        mp.put(catalog['city'], linea['city'], info)
    
    

# Req 1----------------------------------------------------------------------------------------------------------
"""
Como analista de vuelos deseo encontrar el (los) aeropuerto(s) que sirven como punto de
interconexión a más rutas aéreas en la red en cada uno de los grafos.
Para dar respuesta a este requerimiento el equipo de desarrollo no necesita ninguna entrada, y
como respuesta debe presentar en consola la siguiente información:
• Lista de los aeropuertos más interconectados (IATA, nombre, ciudad, país).
• Número de aeropuertos interconectados.
"""
def inter_dirigido(catalog):
    lst_vertices = gr.vertices(catalog['gd_aero_ruta'])
    mapa = mp.newMap(1153, 
                    maptype='PROBING',
                    loadfactor=0.6, 
                    comparefunction=compareMap)
    for element in lt.iterator(lst_vertices):
        arcos_llegada = int(gr.indegree(catalog['gd_aero_ruta'], element))
        arcos_salida = int(gr.degree(catalog['gd_aero_ruta'], element))
        suma = int(arcos_llegada + arcos_salida)
        mp.put(mapa, element, suma)
        pareja = om.get(catalog['gd_aero_ruta'], element)
        valor = me.getValue(pareja)
    


#req 2---------------------------------------------------------------------------------------------------------
"""
Como analista de vuelos deseo encontrar la cantidad de clústeres (componentes fuertemente
conectados) dentro de la red de tráfico aéreo y si dos aeropuertos pertenecen o no al mismo clúster.
Las entradas de este requerimiento son:
• Código IATA del aeropuerto 1.
• Código IATA del aeropuerto 2.
Y como respuesta debe presentar en consola la siguiente información:
• Número total de clústeres presentes en la red de transporte aéreo.
• Informar si los dos aeropuertos están en el mismo clúster o no.
"""
def connectedComponents(catalog, aero1, aero2):
    """
    Calcula los componentes conectados del grafo dirigido
    Se utiliza el algoritmo de Kosaraju
    """
    catalog['components'] = scc.KosarajuSCC(catalog['gd_aero_ruta'])
    numscc = int(scc.connectedComponents(catalog['components']))
    print(numscc)
    aeros_cluster = (scc.stronglyConnected(catalog['components'], aero1, aero2))
    if aeros_cluster == False:
        mnjs = str(print("Los aeropuertos no pertenecen al mismo componente"))
    else:
        mnjs = str(print("Si pertenecen al mismo componente"))
    tupla = numscc, mnjs
    return tupla

#req 3-----------------------------------------------------------------------------------------------------------
"""
Como analista de vuelos deseo encontrar la ruta mínima en distancia para viajar entre dos ciudades,
los puntos de origen y de destino serán los nombres de las ciudades.
Las entradas de este requerimiento son:
• Ciudad de origen.
• Ciudad de destino.
"""
def rutamascorta(catalog, origen, destino):
    orig= mp.get(catalog['city'], origen)
    dest=mp.get(catalog['city'], destino)
    return (orig, dest)
def selecruta(catalog, opcionCiudad, opcionCiudad2):
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
def compareMap(var1, pareja2):
    pareja2= me.getKey(pareja2)
    if (var1) == (pareja2):
        return 0
    elif (var1) > (pareja2):
        return 1
    else:
        return -1