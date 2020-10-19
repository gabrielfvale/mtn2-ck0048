import math
import numpy as np

def x(xi, xf, alfa_k): # Função que relaciona a variavel x à variável alfa
    return (xi + xf)/2 + ((xf - xi) * alfa_k)/2

def quadratura_dois_pontos(function, a, b, N):
    # Array com os valores de Alfa 1 e Alfa 2 
    alfa = [- ((1/3) ** 0.5), ((1/3) ** 0.5)]

    # Array com os valores dos pesos w1 e w2
    w = [1, 1] 

    I, somatorio = 0, 0
    delta = (b-a)/N

    for k in range (1, N+1):
        xi = a + (k-1) * delta

        for i in range (2):
            somatorio += w[i] * function(x(xi, xi + delta, alfa[i]))
        
        I += (delta/2) * somatorio
        somatorio = 0


    return I

def quadratura_tres_pontos(function, a, b, N):
     # Array com os valores de Alfa 1, Alfa 2 e Alfa 3 
    alfa = [- ((3/5) ** 0.5), 0, ((3/5) ** 0.5)]

    # Array com os valores dos pesos w1, w2 e w3
    w = [5/9, 8/9, 5/9] 
    
    I, somatorio = 0, 0
    delta = (b-a)/N

    for k in range (1, N+1):
        xi = a + (k-1) * delta

        for i in range (3):
            somatorio += w[i] * function(x(xi, xi + delta, alfa[i]))

        I += ((delta)/2) * somatorio
        somatorio = 0

    return I

def quadratura_quatro_pontos(function, a, b, N):
    # Array com os valores de Alfa 1, Alfa 2, Alfa 3 e Alfa 4
    alfa = [(((3 + 2 * ((6/5)) ** 0.5)/7) ** 0.5), - (((3 + 2 * ((6/5)) ** 0.5)/7) ** 0.5), (((3 - 2 * ((6/5)) ** 0.5)/7) ** 0.5), - (((3 - 2 * ((6/5)) ** 0.5)/7) ** 0.5)] 
   
    # Array com os valores dos pesos w1, w2, w3 e w4
    w = [(18 - (30) ** 0.5)/36, (18 - (30) ** 0.5)/36, (18 + (30) ** 0.5)/36, (18 + (30) ** 0.5)/36] 
    
    I, somatorio = 0, 0
    delta = (b-a)/N
    
    for k in range (1, N+1):
        xi = a + (k-1) * delta

        for i in range (4):
            somatorio += w[i] * function(x(xi, xi + delta, alfa[i]))

        I += ((delta)/2) * somatorio
        somatorio = 0

    return I

def integ_quadratura(function, quantidade_pontos, xi, xf, error):
    Iv, N, num_iteracoes = 0, 1, 0
    erro = np.Infinity

    while (erro > error):
        num_iteracoes += 1
        N *= 2
        if quantidade_pontos == 2:
            In = quadratura_dois_pontos(function, xi, xf, N)
        elif quantidade_pontos == 3:
            In = quadratura_tres_pontos(function, xi, xf, N)
        elif quantidade_pontos == 4:
            In = quadratura_quatro_pontos(function, xi, xf, N)
        else:
            return 'Quantidade de pontos inválida'
        erro = abs((In - Iv)/In)
        Iv = In

    return [Iv, num_iteracoes]

#Função exemplificada no documento 11
def function_1(x):
    return (math.sin(2 * x) + 4 * (x ** 2) + 3 * x) ** 2

for i in range (2,5):
    print('Quadratura com {} Pontos: \nIntegral: {:.8f} - Iterações: {}\n'.format(i, integ_quadratura(function_1, i, 0, 1, 0.000001)[0], integ_quadratura(function_1, i, 0, 1, 0.000001)[1]))
