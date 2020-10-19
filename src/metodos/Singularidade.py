import Newton-Cotes as nc
from math import cosh, sinh, tanh, pi
import numpy as np

def exponencial_simples(function, a, b, error):
    def x(s):
        return (a + b)/2 + ((b-a)/2) * tanh(s)
    def d_x(s):
        return ((b-a)/2) * (1/cosh(s)**2)
    
    def new_function(s):
        return function(x(s)) * d_x(s)

    erro = np.Infinity
    Iv, c = 0, 0

    try:
        while (erro > error):
            c += 1
            In = nc.integral_fechada(new_function, -c, c, 3, error)[0]
            erro = abs((In - Iv)/In)
            Iv = In
    except:
        return Iv
    return Iv

def exponencial_dupla(function, a, b, error):
    def x(s):
        return (a + b)/2 + ((b-a)/2) * tanh((pi/2) * sinh(s))
    def d_x(s):
        return ((b-a)/2) * ((pi * cosh(s))/(2 * (cosh((pi * sinh(s))/2)) ** 2))
    
    def new_function(s):
        return function(x(s)) * d_x(s)

    erro = np.Infinity
    Iv, c = 0, 0

    try:
        while (erro > error):
            c += 0.5
            In = nc.integral_fechada(new_function, -c, c, 3, error)[0]
            erro = abs((In - Iv)/In)
            Iv = In
    except:
        return Iv
    return Iv

def function_1(x):
    return 1/(x ** (2/3))

def function_2(x):
    return 1/((4 - (x ** 2)) ** 0.5)

def function_3(x):
    return 1/(x ** 0.5)

print(2 * exponencial_simples(function_1, 0, 1, 0.001))
print(2 * exponencial_dupla(function_1, 0, 1, 0.001))
print(exponencial_simples(function_2, -2, 0, 0.001))
print(exponencial_dupla(function_2, -2, 0, 0.001))
print(exponencial_simples(function_3, 0, 1, 0.001))
print(exponencial_dupla(function_3, 0, 1, 0.001))

            
