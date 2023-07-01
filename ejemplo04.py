"""
    Ejemplo del manejo de hilos
    para sistema operativo Windows
"""

import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    # del archivo se necesita obtener la cadena de búsqueda para cuando
    # se busque en youtube
    # ejemplo:
    # De la línea: '7|metodologías de desarrollo', se necesita solo la
    # cadena metodologías de desarrollo
    #
    with open("datos/informacion.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            # row es una lista
            # con esta estructura ['7|metodologías de desarrollo']
            # row[0] tendrá: '7|metodologías de desarrollo'
            # row[0].split("|"), será: ["7", "metodologías de desarrollo"]
            # row[0].split("|")[1], será: "metodologías de desarrollo"
            cadena = row[0].split("|")[1]
            # A la cadena se le reemplaza los espacios vacios con el símbolo
            # +, para que quede listo para la búsqueda
            cadena = cadena.replace(" ", "+")
            lista.append(cadena)
    # se retorna la lista con la información que se necesita
    return lista

def worker(url, cadena_busqueda):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # se arma el comando
    # para el ejemplo se usa google-chrome
    # comando debe variar según el sistema operativo que se use
    # se debe formar la siguiente cadena de búsqueda
    # https://www.youtube.com/results?search_query=loja+ciudad+cultural
    programa = 'chrome'
    comando = '%s/results?search_query=%s' % (url, cadena_busqueda)
    # se ejecuta el comando, a través Popen
    # el comando debe levantar un navegador con la url y la cadena de búsqueda,
    # dada como argumento.
    subprocess.Popen(['start', programa, comando], shell=True)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # args, tiene el argumento, será la url para abrir con el comando y
    # la cadena de búsqueda
    # en la función
    hilo1 = threading.Thread(name='navegando2',
                            target=worker,
                            args=("www.youtube.com", c))
    hilo1.start()
