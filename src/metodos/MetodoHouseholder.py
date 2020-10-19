import numpy as np
from functools import reduce
from PotenciaRegular import *
from PotenciaInversaDeslocamento import potencia_deslocamento, potencia_inversa1

def comprimento_vetor(vector):
    return np.sqrt(reduce(lambda acumulador, coordenada: acumulador + coordenada**2, vector, 0))

#Função para fazer arredondamentos nas matrizes criadas pelo NumPy
def mascara(matriz, casas_decimais):
    matriz_com_mascara = [[0] * len(matriz) for i in range (len(matriz))]
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_com_mascara[i][j] = round(matriz[i][j], casas_decimais)
    
    return matriz_com_mascara

def matriz_de_householder_por_coluna(matriz, coluna):
    
    #Criando dois vetores nulos
    w = np.zeros(len(matriz))
    w_linha = np.zeros(len(matriz))
    
    #Copiando os elementos abaixo da diagonal da coluna i da matriz A
    for i in range (coluna, len(matriz)-1):
        w[i+1] = matriz[i+1][coluna]

    comp_w = comprimento_vetor(w)

    #Copiando comprimento de w para a posição coluna + 1 do vetor w'
    w_linha[coluna+1] = comp_w

    #Calculando e normalizando N
    N = w - w_linha
    n = normalizar(N)

    #Montando matriz de Householder
    H =  np.identity(len(matriz)) - 2*np.outer(n,n)
    
    return mascara(H,3)  

def metodo_de_householder(matriz):
    n = len(matriz)
    #Inicializando Matrizes
    H = mascara(np.identity(n, dtype=float),1)
    matriz_velha = matriz

    for i in range (0, n-2):
        #Matriz de Householder 
        H_novo = matriz_de_householder_por_coluna(matriz_velha, i)
        
        #Transformação de Similaridade
        matriz_nova = mascara(np.dot(np.dot(H_novo,matriz_velha),H_novo),2)
        
        #Salvando Matriz
        matriz_velha = matriz_nova

        #Matriz de Acumulação
        H = mascara(np.dot(H, H_novo),4)
    
    return (matriz_nova, H)

A = [[40,8,4,2,1], [8,30,12,6,2], [4,12,20,1,2], \
    [2,6,1,25,4], [1,2,2,4,5]]

(matriz_tridiagonal, matriz_acumulada) = metodo_de_householder(A)

#1) a)
for i in matriz_tridiagonal: 
    print(i)

print('\n\n--------------------------------------------------------------------\n\n')

#b)
for i in matriz_acumulada: 
    print(i)


print('\n\n--------------------------------------------------------------------\n\n')

#3)

autovalor1 = potencia_regular(matriz_tridiagonal, [1,1,1,1,1], 0.00001)[0]
autovetor1 = potencia_regular(matriz_tridiagonal, [1,1,1,1,1], 0.00001)[1]

autovalor2 = potencia_inversa1(matriz_tridiagonal, [1,1,1,1,1], 0.00001)[0]
autovetor2 = potencia_inversa1(matriz_tridiagonal, [1,1,1,1,1], 0.00001)[1]

autovalor3 = potencia_deslocamento(matriz_tridiagonal, 15, [1,1,1,1,1], 0.00001)[0]
autovetor3 = potencia_deslocamento(matriz_tridiagonal, 15, [1,1,1,1,1], 0.00001)[1]

autovalor4 = potencia_deslocamento(matriz_tridiagonal, 20, [1,1,1,1,1], 0.00001)[0]
autovetor4 = potencia_deslocamento(matriz_tridiagonal, 20, [1,1,1,1,1], 0.00001)[1]

autovalor5 = potencia_deslocamento(matriz_tridiagonal, 30, [1,1,1,1,1], 0.00001)[0]
autovetor5 = potencia_deslocamento(matriz_tridiagonal, 30, [1,1,1,1,1], 0.00001)[1]

autovalores_matriz_tridiagonal = [autovalor1, autovalor2, autovalor3, autovalor4, autovalor5]
autovetores_matriz_tridiagonal = [autovetor1, autovetor2, autovetor3, autovetor4, autovetor5]

for autovetor in autovetores_matriz_tridiagonal:
    print(autovetor)

print('\n\n--------------------------------------------------------------------\n\n')

#4)
autovetores_matriz_original = [produto_matriz_vetor(matriz_acumulada, autovetor) for autovetor in autovetores_matriz_tridiagonal]

for autovetor in autovetores_matriz_original:
    print(autovetor)

print('\n\n--------------------------------------------------------------------\n\n')

#5)
for autovalor in autovalores_matriz_tridiagonal:
    print(autovalor)