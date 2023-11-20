# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:17:23 2023

@author: Alejandro Marulanda
"""

import matplotlib.pyplot as plt
import numpy as np



def f(x):

    value = (np.sin(x**2)) * (np.exp(x**3)) + (np.log(x))/(np.sqrt(x+1))
    return value 

def g(x):
  
        return (np.cos(x**2)) * (2*x) * (np.exp(x**3)) + (np.exp(x**3)) * (3*(x**2)) * (np.sin(x**2)) + (2*(x+1) - x*np.log(x)) / (2*x*(x+1)*np.sqrt(x+1))

def newton(x0, tol=1e-6):
  
    x1 = 0

    if abs(x0-x1)<= tol and abs((x0-x1)/x0)<= tol:
        return x0

    
    iteraciones = 0
    error = 0.0
    error_list = []

    while abs(f(x0)) > tol:

        x1 = x0 - (f(x0)/g(x0))
       
        if abs(x0-x1)<= tol and abs((x0-x1)/x0)<= tol:
            return x1
        error = abs(x1-x0)
        error_list.append(error)
        iteraciones = iteraciones + 1
        x0 = x1
        
        
        

        print("%d \t %.8f \t %.8f \t %.8f" %(iteraciones, x0,x1, error)) 
        

    plt.figure("Grafica del error")
    plt.plot(error_list, "bo-", label = "Metodo de la Secante")
    plt.xlabel("Intervalo")
    plt.yscale("log")
    plt.ylabel(u"$Error$")
    plt.grid(ls="dashed")
    plt.legend()




    return x1  


raiz = newton(0.1)
print("The approximate value of x is: ", raiz)

plt.show()