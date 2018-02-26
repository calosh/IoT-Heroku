import matplotlib.pyplot as plt
import numpy as np


lista1 = [23,24,17,32,33,32,40,39]
plt.xlabel("Hora")
plt.ylabel("Temperatura")

indice = np.arange(8)   # Declara un array
plt.xticks(indice, ("10:11", "11:12", "11:13", "11:14", "11:15", "11:16", "11:17", "11:18"))
plt.plot(lista1)
plt.show()


'''
plt.figure()  # Comenzamos un nuevo grAfico (figura)
lista1 = [11,2,3,15,8,13,21,34]
plt.title("TItulo")
plt.xlabel("abscisa")
plt.ylabel("ordenada")
indice = np.arange(8)   # Declara un array
plt.xticks(indice, ("A", "B", "C", "D", "E", "F", "G", "H"))   
plt.yticks(np.arange(0,51,10))
plt.plot(lista1)
'''


