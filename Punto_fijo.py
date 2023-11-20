# -*- coding: utf-8 -*-
"""
Created on Fri Sep  15 23:17:23 2023

@author: Alejandro Marulanda
"""


# El Xi de este ejercicio es: 18.0 y el valor de los parametros es: k = 5.0, l = 5.0 , A = 5.0

import numpy as np 
import matplotlib.pyplot as plt

k = float(input("Ingrese la constante de las propiedades del material   "))
l = float(input("Ingrese la longitud de la viga  "))
A = float(input("Ingrese el área tranversal de la sección de la viga  "))

const = ((k*l)/A)

def f(x):
    Pc = const - (np.sqrt(x)**3) - 4*x
    return Pc

def g(x):
    return (const + 4*x)**(2/3)

tol=1e-6
xi = 18.0
error = np.abs(g(xi)-xi)
i = 0
error_list = []

while error > tol:
    if i > 0:
        error = np.abs(g(xi)-xi)
        error_list.append(error)

    xi = (g(xi))
    i = i+1
    print("%d \t %.8f \t %.8f \t %.8f" %(i, xi, g(xi), error))

print("El valor aproximado para x es: ", xi, "y el error es: ", "%.8f" %(error ))   
plt.figure("Grafica del error")
plt.plot(error_list, "bo-", label = "Metodo del punto fijo")
plt.xlabel("Intervalo")
plt.yscale("log")
plt.ylabel(u"$Error$")
plt.grid(ls="dashed")
plt.legend()
plt.show()