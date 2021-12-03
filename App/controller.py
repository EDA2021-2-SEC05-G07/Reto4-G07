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
from DISClib.ADT.graph import gr
 
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
 
 
def GetIniciarDatos():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    catalog = model.IniciarDatos()
    return catalog
 
 
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
 
 
def GetcargarDatos(catalog):
    """
    Carga los datos de los archivos CSV en el modelo.
    """
    routesfile = cf.data_dir + 'routes-utf8-large.csv'
    input_routfile = csv.DictReader(open(routesfile, encoding="utf-8"),
                                delimiter=",")
    input_routfile2 = csv.DictReader(open(routesfile, encoding="utf-8"),
                                delimiter=",")
    primero=0
    primeroaero=''
    ulyimoaero=''
    tam= len(input_routfile)
    for ruta in input_routfile:
        primero+=1
        if primero == 1:
            primeroaero=ruta
        if primero == tam-1:
            ultimoaero=ruta
        model.addRuta(catalog, ruta)
    
    ultimaruta=''
    primeroND=0
    primeroaeroND=''
    for linea in input_routfile2:
        origen2 = linea['Departure']
        destino2= linea['Destination']
        peso = float(ruta['distance_km'])
        model.addAirportNoD(catalog, origen2)
        model.addAirportNoD(catalog, destino2)
        ida = gr.getEdge(catalog['gd_aero_ruta'], origen2, destino2)
        vuelta = gr.getEdge(catalog['gd_aero_ruta'], destino2, origen2)
        if ida != None and vuelta != None:
            primeroND+=1
            ultimaruta= linea
        if primeroND == 1:
            primeroaeroND=linea
            model.addRutaNoD(catalog, origen2, destino2, peso)
 
    citiesfile = cf.data_dir + 'worldcities.csv'
    input_citiesfile = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    contador=0
    primerC=0
    primerCiudad=''
    ultimaCiudad=''
    tam= len(input_routfile)
    for linea in input_citiesfile:
        primerC+=1
        if primerC == 1:
            primerCiudad= linea
        ultimaCiudad=linea
        model.addCity(catalog, linea)
    return (catalog, contador, primeroaero, ultimoaero,ultimaruta, primeroaeroND, primerCiudad, ultimaCiudad)

#req 1
def getconnectedComponents(catalog):
    return model.connectedComponents(catalog)
#req2
def getconnectedComponents(catalog, aero1, aero2):
    tupla = model.connectedComponents(catalog,aero1, aero2)
    return tupla

#req3
def getrutamascorta(catalog, origen, destino):
    return model.rutamascorta(catalog, origen, destino)
# Inicialización del Catálogo de libros
 
# Funciones para la carga de datos
 
# Funciones de ordenamiento
 
# Funciones de consulta sobre el catálogo
 