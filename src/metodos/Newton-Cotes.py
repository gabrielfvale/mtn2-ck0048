import numpy as np

def integral_aberta(function, x_in, x_fin, grau_polinomio, error):
    def integ_n_aberta(function, a, b, grau_polinomio, N): #Não é possível acessar diretamente essa função
        I = 0
        delta = (b-a)/N

        if grau_polinomio == 1:
            h = delta/3
            for k in range (1, N+1):
                xi = a + (k-1) * delta 
                I += 3 * h * (function(xi + h) + function(xi + 2 * h))/2

        elif grau_polinomio == 2:
            h = delta/4
            for k in range (1, N+1):
                xi = a + (k-1) * delta 
                I += 4 * h * (2 * (function(xi + h) + function(xi + 3 * h)) - function (xi + 2 * h))/3

        elif grau_polinomio == 3:
            h = delta/5
            for k in range (1, N+1):
                xi = a + (k-1) * delta 
                I += 5 * h * (11 * (function(xi + h) + function(xi + 4 * h)) + function(xi + 2 * h) + function(xi + 3 * h))/24

        elif grau_polinomio == 4:
            h = delta/6
            for k in range (1, N+1):
                xi = a + (k-1) * delta 
                I += 3 * h * (11 * (function(xi + h) + function(xi + 5 * h)) - 14 * (function (xi + 2 * h) + function(xi + 4 * h)) + 26 * function(xi + 3 * h)) /10

        return I

    Iv, N, num_iteracoes = 0, 1, 0
    erro = np.Infinity
    while (erro > error):
        num_iteracoes += 1
        N *= 2
        In = integ_n_aberta(function, x_in, x_fin, grau_polinomio, N)
        erro = abs((In - Iv)/In)
        Iv = In

    return [Iv, num_iteracoes]

def integral_fechada(function, x_in, x_fin, grau_polinomio, error):
    def integ_n_fechada(function, a, b, grau_polinomio, N):
        I = 0
        delta = (b-a)/N

        if grau_polinomio == 1:
            h = delta
            for k in range (1, N+1):
                xi = a + (k-1) * delta
                xf = xi + delta
                I += h * (function(xi) + function(xf))/2

        elif grau_polinomio == 2:
            h = delta/2
            for k in range (1, N+1):
                xi = a + (k-1) * delta
                xf = xi + delta
                I += h * (function(xi) + function(xf) + 4 * function (xi + h))/3

        elif grau_polinomio == 3:
            h = delta/3
            for k in range (1, N+1):
                xi = a + (k-1) * delta
                xf = xi + delta
                I += 3 * h * (function(xi) + 3 * (function(xi + h) + function(xi + 2 * h)) + function(xf))/8

        elif grau_polinomio == 4:
            h = delta/4
            for k in range (1, N+1):
                xi = a + (k-1) * delta
                xf = xi + delta
                I += 2 * h * (7 * (function(xi) + function(xf)) + 32 * (function (xi + h) + function(xi + 2 * h)) + 12 * function(xi + 3 * h)) /45

        return I

    Iv, N, num_iteracoes = 0, 1, 0
    erro = np.Infinity
    while (erro > error):
        num_iteracoes += 1
        N *= 2
        In = integ_n_fechada(function, x_in, x_fin, grau_polinomio, N)
        erro = abs((In - Iv)/In)
        Iv = In

    return [Iv, num_iteracoes]

#É necessário criar a função desejada e passá-la como parâmetro para as funções em que se calcula a integral
def function_1(x): #Exemplo passado no Documento 8
    return (np.sin(2 * x) + 4 * (x**2) + 3 * x)**2

print('Abordagem Fechada:')
print('Grau 1: Integral: {:.2f} - Passos: {}'.format(integral_fechada(function_1, 0, 1, 1, 0.000001)[0], integral_fechada(function_1, 0, 1, 1, 0.000001)[1]))
print('Grau 2: Integral: {:.2f} - Passos: {}'.format(integral_fechada(function_1, 0, 1, 2, 0.000001)[0], integral_fechada(function_1, 0, 1, 2, 0.000001)[1]))
print('Grau 3: Integral: {:.2f} - Passos: {}'.format(integral_fechada(function_1, 0, 1, 3, 0.000001)[0], integral_fechada(function_1, 0, 1, 3, 0.000001)[1]))
print('Grau 4: Integral: {:.2f} - Passos: {}\n'.format(integral_fechada(function_1, 0, 1, 4, 0.000001)[0], integral_fechada(function_1, 0, 1, 4, 0.000001)[1]))

print('Abordagem Aberta:')
print('Grau 1: Integral: {:.2f} - Passos: {}'.format(integral_aberta(function_1, 0, 1, 1, 0.000001)[0], integral_aberta(function_1, 0, 1, 1, 0.000001)[1]))
print('Grau 2: Integral: {:.2f} - Passos: {}'.format(integral_aberta(function_1, 0, 1, 2, 0.000001)[0], integral_aberta(function_1, 0, 1, 2, 0.000001)[1]))
print('Grau 3: Integral: {:.2f} - Passos: {}'.format(integral_aberta(function_1, 0, 1, 3, 0.000001)[0], integral_aberta(function_1, 0, 1, 3, 0.000001)[1]))
print('Grau 4: Integral: {:.2f} - Passos: {}'.format(integral_aberta(function_1, 0, 1, 4, 0.000001)[0], integral_aberta(function_1, 0, 1, 4, 0.000001)[1]))
