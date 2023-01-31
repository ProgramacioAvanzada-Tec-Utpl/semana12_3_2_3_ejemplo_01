"""
    Ejemplo del manejo de hilos
"""

import time
import threading
# librería de python que permite ejecutar comandos
import subprocess

def worker(url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # se arma el comando
    # para el ejemplo se usa chromium-browser
    # comando debe variar según el sistema operativo que se use
    comando = "chromium-browser %s" % (url)
    # se ejecuta el comando, a través Popen
    # el comando debe levantar un navegador con la url, dada como argumento.
    subprocess.Popen(comando, shell=True)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

# Se crea los hilos
# args, tiene el argumento, será la url para abrir con el comando
# en la función
hilo1 = threading.Thread(name='navegando', target=worker, args=("www.youtube.com",))
hilo2 = threading.Thread(name='navegando', target=worker, args=("www.utpl.edu.ec",))

# inicio de cada hilo
hilo1.start()
hilo2.start()
