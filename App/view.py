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
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT.graph import gr
import threading
from DISClib.ADT import map as mp 
 
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req 1")
    print("3- Req 2")
    print("4- Req 3")
    print("5- Req 4")
    print("6- Req 5")
 
catalog = controller.GetIniciarDatos()
init = controller.GetIniciarDatos()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.GetcargarDatos(catalog)
        numVertDiri = gr.numVertices(catalog['gd_aero_ruta'])
        numArcoDiri = gr.numEdges(catalog['gd_aero_ruta'])
        numVertND = gr.numVertices(catalog['g_una_ruta'])
        numArcoND = gr.numEdges(catalog['g_una_ruta'])
        print('El numero de aeropuertos (vertices) en el grafo dirigido es: ' + str(numVertDiri))
        print('El numero de rutas aéreas (arcos) en el grafo dirigido es: ' + str(numArcoDiri))
        print('El numero de aeropuestos (vertices) en el grafo NO dirigido es: ' + str(numVertND))
        print('El numero de rutas aéreas (arcos) en el grafo NO dirigido es: ' + str(numArcoND))
        print('El primer aeropuerto del digrafo')
        catalog['gd_aero_ruta']
       # print(lt.size(catalog['rutas']))
        info=controller.GetcargarDatos(catalog)
        print('El total de ciudades es: ')
        print(info[1])
        print('El primer aeropuerto cargado en el digrafo es: ')
        pad=info[2]
        print(pad['Name'])
        print(pad['City'])
        print(pad['Country'])
        print(pad['Latitude'])
        print(pad['Longitude'])
        print('El ultimo aeropuerto cargado en el digrafo es: ')
        uad=info[3]
        print(uad['Name'])
        print(uad['City'])
        print(uad['Country'])
        print(uad['Latitude'])
        print(uad['Longitude'])
        print('El primer aeropuerto cargado en el grafo no dirigido es: ')
        pand=info[5]
        print(pand['Name'])
        print(pand['City'])
        print(pand['Country'])
        print(pand['Latitude'])
        print(pand['Longitude'])
        print('El ultimo aeropuerto cargado en el grafo no dirigido es: ')
        uand=info[4]
        print(uand['Name'])
        print(uand['City'])
        print(uand['Country'])
        print(uand['Latitude'])
        print(uand['Longitude'])
        print('La primera ciudad cargada es: ')
        pc=info[6]
        print(pc['city'])
        print(pc['population'])
        print(pc['lat'])
        print(pc['lng'])
        print('La ultima ciudad cargada es: ')
        uc=info[7]
        print(uc['city'])
        print(uc['population'])
        print(uc['lat'])
        print(uc['lng'])
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        aero1 = str(input("Airport-1 IATA code: "))
        aero2 = str(input("Airport-2 IATA code: "))
        tupla = controller.getconnectedComponents(catalog, aero1, aero2)
        print("el número de scc en la red de aeropuetos es: " +str(tupla[0]))
        print("La pareja de aeropuertos está dentro del mismo componente? "+ str(tupla[1]))
    elif int(inputs[0]) == 4:
        origen= input('Escriba la ciudad de origen: ')
        destino= input('Escriba la ciudad de destino: ')
        ciudades= controller.getrutamascorta(catalog, origen, destino)
        x=0
        if mp.size(ciudades[0]) > 1:
            for linea in ciudades[0]:
                x+=1
                print('Opcion ')+ str(x)
                print (linea)
                opcionCiudad=input('Digite la opcion que necesita:')
        opcionCiudad= int(opcionCiudad)-1
        y=0
        if mp.size(ciudades[1]) > 1:
            for linea in ciudades[1]:
                y+=1
                print('Opcion ')+ str(x)
                print (linea)
                opcionCiudad2=input('Digite la opcion que necesita:')
        opcionCiudad2= int(opcionCiudad2)-1
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
   
        pass
    else:
        sys.exit(0)
sys.exit(0)

    
