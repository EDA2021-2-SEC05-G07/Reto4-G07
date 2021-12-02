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
       # print(lt.size(catalog['rutas']))
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
       numscc = controller.getconnectedComponents(catalog)
       print("el número de scc es:" +str(numscc))
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
   
        pass
    else:
        sys.exit(0)
sys.exit(0)

    
