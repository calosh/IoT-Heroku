import os
import time
import numpy as np
import matplotlib.pyplot as plt

import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


con_bd = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))
con_bd.row_factory = sqlite3.Row


while(True):
    cursor_agenda = con_bd.cursor()

    cursor_agenda.execute("SELECT * FROM app_temperatura ORDER BY date(date) DESC LIMIT 8")
    '''
    registro = cursor_agenda.fetchone()
    print("Nombre", registro['date'])
    print("Correo", registro['temperatura'])
    '''
    lista1 = []
    #registro = cursor_agenda.fetchone()
    for i in cursor_agenda:
        print i[1]
        lista1.append(int(i[1]))

    print lista1
    cursor_agenda.close()

    #lista1 = [23,24,17,32,33,32,40,39]
    plt.xlabel("Hora")
    plt.ylabel("Temperatura")

    indice = np.arange(8)   # Declara un array
    plt.xticks(indice, ("10:11", "11:12", "11:13", "11:14", "11:15", "11:16", "11:17", "11:18"))
    plt.plot(lista1)
    # plt.show()
    plt.savefig(os.path.join(BASE_DIR, 'static/myfig'))
    plt.close()
    time.sleep(5)
