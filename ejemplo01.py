"""
    Ejemplo del manejo de hilos
"""

import time
# se importa la librería
import threading

# se genera la función
def worker(nombre):
    print("Iniciando %s %s" % (threading.current_thread().getName(), nombre ))
    # tiempo de espera
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

# lista para nombrar los hilos
lista = ["Ecuador", "Perú", "Colombia", "Venezuela"]
for i in lista:
    # se crea el hilo
    # el nombre del hilo, será el valor de i en la iteración
    # con target se llama a la función (def worker)
    # args, tiene los argumentos de la función; en el ejemplo
    # se envía el valor de i
    t = threading.Thread(name="paises", target=worker, args=(i,))
    # se inicia el hilo
    t.start()
