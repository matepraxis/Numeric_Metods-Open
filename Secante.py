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


def Secante(x0, x1, tol=1e-6, max_iteraciones=100):
   
  error = 0.0
  error_list = []
     
  i = 0

  while abs(f(x1)) > tol:
    
       x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
    
       
       error = abs(x2-x1)
       error_list.append(error)
       i = i+1
       x0 = x1
       x1 = x2
       
       print("%d \t %.8f \t %.8f \t %.8f \t %.8f" %(i, x0,x1,x2, error)) 

  plt.figure("Grafica del error")
  plt.plot(error_list, "bo-", label = "Metodo de la Secante")
  plt.xlabel("Intervalo")
  plt.yscale("log")
  plt.ylabel(u"$Error$")
  plt.grid(ls="dashed")
  plt.legend()



  return x2 


raiz = Secante( 0.1, 1.0, 0.0000001)
print("El valor aproximado para x es: ", raiz,)       
plt.show()       
